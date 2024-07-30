import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
import lightning as L


class StockDataset(Dataset):
    def __init__(self, data: pd.DataFrame):
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


class StockDataModule(L.LightningDataModule):
    def __init__(
        self,
        batch_size: int,
        *args,
        **kwargs,
    ):
        super().__init__()
        self.batch_size = batch_size
        self.save_hyperparameters()
    
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


