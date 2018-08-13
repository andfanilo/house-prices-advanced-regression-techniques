import pandas as pd


def load_datasets(nrows=None):
    train = pd.read_csv('../data/raw/train.csv')
    test = pd.read_csv('../data/raw/test.csv')
    return (train, test)