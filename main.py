import sys
import numpy as np
import yfinance as yf

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_numpy_version() -> str:
    return np.__version__

def get_yfinance_version() -> str:
    return yf.__version__

def main():
    pass

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'YFinance version: {get_yfinance_version()}')
    print(f'NumPy version: {get_numpy_version()}')
    main()