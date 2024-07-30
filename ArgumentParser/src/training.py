import torch

import torch.nn.functional as F
import torch.optim as optim

import lightning as L


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

        self.save_hyperparameters()

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

        self.log('loss/train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)

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

        self.log('loss/val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)

        return loss
    
    # def on_valid_epoch_end(self, *args, **kwargs):
    #     print(f'valid epoch end: {self.total_valid_loss/self.batch_count}')

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

