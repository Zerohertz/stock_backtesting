import pandas as pd
import pandas_ta as ta
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


import common

def add_ta_to_all_df():
    for stock in common.stocks:
        file_name = "{}_1d_2006-06-21_2022-12-22".format(stock)
        # Load data
        df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\{}.csv".format(file_name), sep=",")
        # inverse_df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\SQQQ_1d_2019-01-14_2022-12-12.csv", sep=",")

        MyStrategy = ta.Strategy(
            name="rsi",
            description="rsi",
            ta=[
                {"kind": "rsi"},
                {"kind": "stoch"},
                {"kind": "macd"},
                {"kind": "mfi"},
            ]
        )

        # 전략설정
        df.ta.strategy(MyStrategy)

        # 저장
        df.to_csv("./ta_data/ta_{0}.csv".format(file_name), mode = "w")

if __name__ == '__main__':
    stock = "UPRO"
    file_name = "{}_1d_max".format(stock)
    # Load data
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\{}.csv".format(file_name), sep=",")
    # inverse_df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\SQQQ_1d_2019-01-14_2022-12-12.csv", sep=",")

    MyStrategy = ta.Strategy(
        name="rsi",
        description="rsi",
        ta=[
            {"kind": "rsi"},
            {"kind": "stoch"},
            {"kind": "macd"},
            {"kind": "mfi"},
        ]
    )

    # 전략설정
    df.ta.strategy(MyStrategy)

    # 저장
    df.to_csv("./ta_data/ta_{0}.csv".format(file_name), mode = "w")
