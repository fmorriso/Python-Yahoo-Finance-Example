import sys
from importlib.metadata import version
from typing import Any

import pandas as pd
import yfinance as yf
from IPython.display import display
#FAILS: from pyspark.sql import SparkSession
from tabulate import tabulate

from rich.console import Console
from rich.table import Table

from prettytable import PrettyTable
from yfinance import Ticker


def get_package_version(package_name: str) -> str:
    return version(package_name)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def print_tableized(df):
    if not isinstance(df, pd.DataFrame):
        return
    df_columns = df.columns.tolist()
    max_col_len = max(len(col) for col in df_columns)
    formatted_table = []

    header_line = '+'.join(['-' * (max_col_len + 2)] * len(df_columns)).join(['+', '+'])
    formatted_table.append(header_line)
    formatted_table.append('|' + '|'.join(f" {col} " for col in df_columns) + '|')
    formatted_table.append(header_line)

    for _, row in df.iterrows():
        formatted_table.append('|' + '|'.join(f" {val} " for val in row) + '|')
        formatted_table.append(header_line)

    return "\n".join(formatted_table)


def print_rich(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        return

    console = Console()
    table = Table(df)
    for column in df.columns:
        table.add_column(column, justify='center')
    for index, row in df.iterrows():
        table.add_row(*(row.astype(str)))
    console.print(table)

""" FAILS with Spark 3.5.5 as of 2025-04
def print_spark(pandas_df: pd.DataFrame):
    spark = SparkSession.builder.appName("pandas to spark").getOrCreate()
    df = spark.createDataFrame(pandas_df)
    #df.createOrReplaceTempView('pandas_df')
    df.show()
"""

def print_tabulate(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        return
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))


def print_pretty_table(df, include_index=True):
    if not isinstance(df, pd.DataFrame):
        return
    table = PrettyTable()

    if include_index:
        df = df.copy()
        df.insert(0, 'Index', df.index)

    table.field_names = df.columns.tolist()

    # Format values and add rows
    for row in df.itertuples(index = False):
        formatted_row = []
        for col_name, value in zip(df.columns, row):
            col_dtype = df[col_name].dtype

            if pd.api.types.is_integer_dtype(col_dtype):
                formatted_row.append(f"{value:,}")
            elif pd.api.types.is_float_dtype(col_dtype):
                formatted_row.append(f"{value:,.2f}")
            else:
                formatted_row.append(str(value))
        table.add_row(formatted_row)

    # Align columns
    for col in df.columns:
        dtype = df[col].dtype
        if pd.api.types.is_numeric_dtype(dtype):
            table.align[col] = "r"
        elif pd.api.types.is_string_dtype(dtype):
            table.align[col] = "l"
        else:
            table.align[col] = "c"

    print(table)


def get_financial_information(stock_symbol: str) -> Ticker:
    tkr: Ticker = yf.Ticker(stock_symbol)
    print(f'{type(tkr) = }')

    print(f'{type(tkr.info) = }')
    print(tkr.info)

    print(f'{type(tkr.calendar) = }')
    print(tkr.calendar)

    # use Pandas to create a DataFrame out of some of the stock ticker dictionary
    #df = pd.DataFrame(tkr.calendar)
    #display(df)

    #print_tabulate(df)

    #UGLY print(print_tableized(df))
    #FAILS:  print_rich(df)
    #FAILS print_spark(df)
    # print_pretty_table(df)
    return tkr



def main():
    tkr: Ticker = get_financial_information('TSLA')
    print_pretty_table(pd.DataFrame(tkr.calendar))


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'YFinance version: {get_package_version("YFinance")}')
    print(f'NumPy version: {get_package_version("numpy")}')
    #print(f'tabulate version: {get_package_version("tabulate")}')
    print(f'pandas version: {get_package_version("pandas")}')
    #print(f'rich version: {get_package_version("rich")}')
    print(f'PrettyTable version: {get_package_version("prettytable")}')

    main()
