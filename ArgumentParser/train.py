from src.data import StockDataset, StockDataModule
from src.training import StockLightningModule
from src.models.mlp import MLP

import pandas as pd
import argparse

from sklearn.preprocessing import StandardScaler

from lightning.pytorch.trainer import Trainer
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from lightning.pytorch.loggers import TensorBoardLogger


def main(**kwargs):
    batch_size = kwargs.get('batch_size')
    epochs = kwargs.get('epochs')
    learning_rate = kwargs.get('learning_rate')
    hidden_dim = kwargs.get('hidden_dim')
    data_path = kwargs.get('data_path')

    ### data preprocessing ###
    data = pd.read_csv(data_path)
    data = data.set_index('DATE')
    data = data.sort_index()
    data = data.replace(to_replace=',', value='', regex=True)
    data = data.astype(float)
    data['target'] = data.A_CP.shift(-1)
    data = data.dropna()

    ### train, valid, test ###
    train = data.iloc[:800]
    valid = data.iloc[800:800+400]
    test = data.iloc[800+400:]

    ### scaling ###
    standard_scaler = StandardScaler()
    train.iloc[:] = standard_scaler.fit_transform(train)
    valid.iloc[:] = standard_scaler.transform(valid)
    test.iloc[:] = standard_scaler.transform(test)

    ### stock dataset ###
    train_dataset = StockDataset(train)
    valid_dataset = StockDataset(valid)
    test_dataset = StockDataset(test)

    ### model define ###
    model = MLP(len(train.columns)-1, hidden_dim, 1)

    ### trainer define ###
    trainer = Trainer(
        max_epochs=epochs,
        callbacks=[
            EarlyStopping(monitor='loss/val_loss', mode='min', patience=5)
        ],
        log_every_n_steps=1,
        logger=TensorBoardLogger(
            "Tensorboard",
            name=f"MLP/batch_size={batch_size},lr={learning_rate}",
        )
    )

    ### data prepare ###
    stock_data_module = StockDataModule(batch_size)
    stock_data_module.prepare(train_dataset, valid_dataset, test_dataset)
    stock_lightning_module = StockLightningModule(model, learning_rate)

    ### trainer ###
    trainer.fit(
        model=stock_lightning_module,
        datamodule=stock_data_module,
    )


if __name__ == '__main__':
    #### argparse ####
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--learning_rate', type=float, default=1e-3)
    parser.add_argument('--hidden_dim', type=int, default=64)
    parser.add_argument('--data_path', type=str, default='./src/data/data.csv')
    args = parser.parse_args()

    #### Hyperparameters ####
    batch_size = args.batch_size
    epochs = args.epochs
    learning_rate = args.learning_rate
    hidden_dim = args.hidden_dim
    data_path = args.data_path

    #### train ####
    main(
        batch_size=batch_size,
        epochs=epochs,
        learning_rate=learning_rate,
        hidden_dim=hidden_dim,
        data_path=data_path,
        )
