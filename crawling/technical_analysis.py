import pandas as pd
import pandas_ta as ta
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import common

def add_ta_to_df(stock_code):
    # Load data
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\{}.csv".format(stock_code), sep=",")

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
    df.to_csv("./ta_data/ta_{0}.csv".format(stock_code), mode = "w")

def add_ta_to_all_df():
    for stock in common.stocks:
        add_ta_to_df(stock)