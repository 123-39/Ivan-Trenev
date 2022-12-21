""" Model prediction """
import os
import pickle
import click
import numpy as np
import pandas as pd


def load_obj_pkl(path: str):
    """ Load pickle object """

    with open(path, 'rb') as file:
        obj = pickle.load(file)
        return obj


@click.command('predict')
@click.option("--input_path")
@click.option("--pred_path")
@click.option("--scaler_path")
@click.option("--model_path")
def predict(
    input_path: str,
    pred_path: str,
    scaler_path: str,
    model_path: str
) -> None:
    """ Make predict function """

    model = load_obj_pkl(os.path.join(model_path, 'model.pkl'))
    transformrs = load_obj_pkl(os.path.join(scaler_path, 'transformer.pkl'))

    data = pd.read_csv(
        os.path.join(input_path, 'test.csv'),
        index_col=0
    )

    data = transformrs.transform(data)
    prediction = model.predict(data)

    os.makedirs(pred_path, exist_ok=True)
    np.savetxt(os.path.join(pred_path, 'predictions.csv'),
               prediction, delimiter=",")


if __name__ == '__main__':
    predict()
