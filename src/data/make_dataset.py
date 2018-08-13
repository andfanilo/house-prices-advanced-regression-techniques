import pandas as pd


class Dataset:
    def __init__(self, nrows=None):
        train = pd.read_csv('../data/raw/train.csv', nrows=nrows)
        test = pd.read_csv('../data/raw/test.csv', nrows=nrows)
        
        quantitative_cols = [f for f in train.columns if train.dtypes[f] != 'object']
        quantitative_cols.remove('SalePrice')
        quantitative_cols.remove('Id')
        
        self.data = (train, test)
        self.quantitative_cols = quantitative_cols
        self.qualitative_cols = [f for f in train.columns if train.dtypes[f] == 'object']