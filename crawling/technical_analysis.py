import pandas as pd
import pandas_ta as ta
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import common

def add_ta_to_df(stock, start_crawl_date, end_crawl_date, interval_time="1d"):
    # Load data
    df = common.load_csv(stock)
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
    df.to_csv("./ta_data/ta_{0}_{1}_{2}_{3}.csv".format(stock, interval_time, start_crawl_date, end_crawl_date), mode = "w")

def add_ta_to_all_df(start_crawl_date, end_crawl_date, interval_time="1d"):

    all_stocks = common.get_all_stocks()
    for stock in all_stocks:
        add_ta_to_df(stock, start_crawl_date, end_crawl_date, interval_time="1d")