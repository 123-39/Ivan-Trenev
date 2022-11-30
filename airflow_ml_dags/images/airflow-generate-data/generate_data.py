""" Generation synthetic data """
import os
from typing import NoReturn
import click
import numpy as np

from sklearn.datasets import load_breast_cancer


@click.command("generate")
@click.option("--out_path")
def generate_data_cancer(out_path: str) -> NoReturn:
    """ Data generation function """

    n_rand = np.random.randint(50, 550)

    data, target = load_breast_cancer(return_X_y=True, as_frame=True)

    os.makedirs(out_path, exist_ok=True)

    data[:n_rand].to_csv(os.path.join(out_path, 'data.csv'))
    target[:n_rand].to_csv(os.path.join(out_path, 'target.csv'))


if __name__ == '__main__':
    generate_data_cancer()
