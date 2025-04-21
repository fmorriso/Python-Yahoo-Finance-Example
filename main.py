import sys

import numpy as np
import yfinance as yf
import pandas as pd
import tabulate as tbl
from tabulate import tabulate
from IPython.display import display
from importlib.metadata import version


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_numpy_version() -> str:
    return np.__version__


def get_yfinance_version() -> str:
    return yf.__version__

def get_tabulate_version():
    return version('tabulate')

def get_financial_information(stock_symbol: str):
    tkr = yf.Ticker(stock_symbol)
    print(f'{type(tkr) = }')

    print(f'{type(tkr.info) = }')
    print(tkr.info)

    print(f'{type(tkr.calendar) = }')
    print(tkr.calendar)

    df = pd.DataFrame(tkr.calendar)
    display(df)

    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))


def main():
    get_financial_information('TSLA')





if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'YFinance version: {get_yfinance_version()}')
    print(f'NumPy version: {get_numpy_version()}')
    print(f'NumPy version: {get_tabulate_version()}')
    main()
