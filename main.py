import sys
from importlib.metadata import version

import pandas as pd
import yfinance as yf
from IPython.display import display
from tabulate import tabulate


def get_package_version(package_name: str) -> str:
    return version(package_name)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


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
    print(f'YFinance version: {get_package_version("YFinance")}')
    print(f'NumPy version: {get_package_version("numpy")}')
    print(f'tabulate version: {get_package_version("tabulate")}')
    print(f'pandas version: {get_package_version("pandas")}')

    main()
