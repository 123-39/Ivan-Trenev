""" Training data """
import os
from typing import NoReturn
import pickle
import click
import pandas as pd
from sklearn.linear_model import LogisticRegression


def save_object_pkl(obj, path: str) -> NoReturn:
    """ Save pickle object """

    with open(path, 'wb') as file:
        pickle.dump(obj, file)


@click.command("train")
@click.option("--load_data_path")
@click.option("--save_model_path")
def train_model(load_data_path: str, save_model_path: str) -> NoReturn:
    """ Train model function"""

    data = pd.read_csv(
        os.path.join(load_data_path, 'train.csv'),
    )

    y_train = data.target.values
    x_train = data.drop(['target'], axis=1).values

    logreg = LogisticRegression(
        random_state=42,
        max_iter=1000,
    ).fit(x_train, y_train)

    os.makedirs(save_model_path, exist_ok=True)

    save_object_pkl(logreg, os.path.join(save_model_path, 'model.pkl'))


if __name__ == "__main__":
    train_model()
