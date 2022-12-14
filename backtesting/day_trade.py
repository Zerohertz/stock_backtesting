import pandas as pd
import pandas_ta as ta

df = pd.DataFrame() # Empty DataFrame

# Load data
df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\TQQQ_1d_2019-01-14_2022-12-12.csv", sep=",")
inverse_df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\SQQQ_1d_2019-01-14_2022-12-12.csv", sep=",")

# 스토캐스틱 알고리즘
def stochastic_trade(df, wallet):
    cnt = 0
    for i in range(942,len(df['STOCHk_14_3_3'])):
        # print("보유금액", wallet)
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20):
            print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=70 and cnt >= 1):
            print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
    return wallet

# 인버스 적용한 스토캐스틱 알고리즘
def inverse_stochastic_trade(df, inverse_df, wallet):
    cnt = 0
    inverse_cnt = 0
    for i in range(942,len(df['STOCHk_14_3_3'])):
        # print(wallet)
        # print("보유금액", wallet)
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20 and inverse_cnt >= 0):
            print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            wallet = wallet + (inverse_df['Open'][i]*inverse_cnt)
            cnt=cnt+1
            inverse_cnt = 0

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=70 and cnt >= 0):
            print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            wallet = wallet - inverse_df['Open'][i]
            cnt=0
            inverse_cnt = inverse_cnt+1
    return wallet

# rsi 구매 알고리즘
def rsi_trade(df, wallet):
    cnt = 0
    for i in range(0,len(df['STOCHk_14_3_3'])):
        # print("보유금액", wallet)
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=80 and cnt >= 1):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
    return wallet

if __name__ == '__main__':
    # Create your own Custom Strategy
    DayStochasticTradeStrategy = ta.Strategy(
        name="stochastic",
        description="stochastic",
        ta=[
            {"kind": "stoch"},
        ]
    )

    # (2) Run the Strategy
    df.ta.strategy(DayStochasticTradeStrategy)

    wallet = 0
    print(stochastic_trade(df, wallet))
    # print(inverse_stochastic_trade(df, inverse_df, wallet))
    # print(rsi_trade(df, wallet))