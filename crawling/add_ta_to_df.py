import pandas as pd
import pandas_ta as ta

if __name__ == '__main__':

    file_name = "TQQQ_1d_2012-01-14_2022-12-12"
    # Load data
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\{}.csv".format(file_name), sep=",")
    # inverse_df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\SQQQ_1d_2019-01-14_2022-12-12.csv", sep=",")

    MyStrategy = ta.Strategy(
        name="rsi",
        description="rsi",
        ta=[
            {"kind": "rsi"},
            {"kind": "stoch"},
            {"kind": "macd"}
        ]
    )

    # 전략설정
    df.ta.strategy(MyStrategy)

    # 저장
    df.to_csv("./data/ta_{0}.csv".format(file_name), mode = "w")