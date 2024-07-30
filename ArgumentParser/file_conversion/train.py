import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

import lightning as L
from lightning.pytorch.trainer import Trainer
from lightning.pytorch.callbacks.early_stopping import EarlyStopping



batch_size = 128
epochs = 50
learning_rate = 1e-3
hidden_dim = 64



data = pd.read_csv('day04/data.csv')
data = data.set_index('DATE')
data = data.sort_index()
data = data.replace(to_replace=',', value='', regex=True)
data = data.astype(float)
data['target'] = data.A_CP.shift(-1)
data = data.dropna()






train = data.iloc[:800]
valid = data.iloc[800:800+400]
test = data.iloc[800+400:]



standard_scaler = StandardScaler()

train.iloc[:] = standard_scaler.fit_transform(train)
valid.iloc[:] = standard_scaler.transform(valid)
test.iloc[:] = standard_scaler.transform(test)


class StockDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        x = self.data.iloc[index, :-1]
        y = self.data.iloc[index, -1:]

        x = torch.Tensor(x)
        y = torch.Tensor(y)

        return {
            'X': x,
            'y': y,
        }
    

train_dataset = StockDataset(train)
valid_dataset = StockDataset(valid)
test_dataset = StockDataset(test)



class StockDataModule(L.LightningDataModule):
    def __init__(
        self,
        batch_size: int,
        *args,
        **kwargs,
    ):
        super().__init__()
        self.batch_size = batch_size
    
    def prepare(
        self,
        train: Dataset,
        valid: Dataset,
        test: Dataset,
        ):
        self.train = train
        self.valid = valid
        self.test = test
    
    def setup(self, stage: str = None):
        if stage == 'fit':
            self.train_data = self.train
            self.valid_data = self.valid
        
        if stage == 'test':
            self.test_data = self.test
    
    def train_dataloader(self):
        return DataLoader(
            dataset=self.train_data,
            batch_size=self.batch_size,
            shuffle=False,
        )

    def val_dataloader(self):
        return DataLoader(
            dataset=self.valid_data,
            batch_size=self.batch_size,
            shuffle=False,
        )

    def test_dataloader(self):
        return DataLoader(
            dataset=self.test_data,
            batch_size=self.batch_size,
            shuffle=False,
        )


class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x


model = MLP(len(train.columns)-1, hidden_dim, 1)

class StockLightningModule(L.LightningModule):
    def __init__(
        self,
        model: torch.nn,
        learning_rate: float,
        *args,
        **kwargs,
    ):
        super().__init__()
        self.model = model
        self.learning_rate = learning_rate

        self.total_train_loss = 0
        self.total_valid_loss = 0
        self.total_test_loss = 0
        self.batch_count = 0
    
    def training_step(
        self,
        batch,
        batch_idx,
        *args,
        **kwargs,
        ):
        if batch_idx == 0:
            self.total_train_loss = 0
            self.batch_count = 0

        X = batch.get('X')
        y = batch.get('y')

        y_pred = self.model(X)

        loss = self.mse_loss(y_pred, y)
        self.total_train_loss += loss
        self.batch_count += 1

        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)

        return loss

    def on_train_epoch_end(self, *args, **kwargs):
        print(f'train epoch end: {self.total_train_loss/self.batch_count}')
    
    def validation_step(
        self,
        batch,
        batch_idx,
        *args,
        **kwargs,
    ):
        if batch_idx == 0:
            self.total_valid_loss = 0
            self.batch_count = 0

        X = batch.get('X')
        y = batch.get('y')
        
        y_pred = self.model(X)

        loss = self.mse_loss(y_pred, y)
        self.total_valid_loss += loss
        self.batch_count += 1

        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)

        return loss
    
    def on_valid_epoch_end(self, *args, **kwargs):
        print(f'valid epoch end: {self.total_valid_loss/self.batch_count}')

    def test_step(
        self,
        batch,
        batch_idx,
        *args,
        **kwargs,
    ):
        if batch_idx == 0:
            self.total_test_loss = 0
            self.batch_count = 0

        X = batch.get('X')
        y = batch.get('y')
        
        y_pred = self.model(X)

        loss = self.mse_loss(y_pred, y)
        self.total_test_loss += loss
        self.batch_count += 1

    def on_test_epoch_end(self, *args, **kwargs):
        print(f'test epoch end: {self.total_test_loss/self.batch_count}')

    def configure_optimizers(self):
        optimizer = optim.Adam(
            self.model.parameters(),
            lr=self.learning_rate,
        )

        return {'optimizer': optimizer}

    def mse_loss(self, y_pred, y):
        return F.mse_loss(y_pred, y)
    

trainer = Trainer(
    max_epochs=epochs,
    callbacks=[
        EarlyStopping(monitor='val_loss', mode='min', patience=5)
    ],
    log_every_n_steps=1,
)


stock_data_module = StockDataModule(batch_size)
stock_data_module.prepare(train_dataset, valid_dataset, test_dataset)

stock_lightning_module = StockLightningModule(model, learning_rate)

trainer.fit(
    model=stock_lightning_module,
    datamodule=stock_data_module,
)