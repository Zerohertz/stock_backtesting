import pandas as pd
from backtesting import day_trade
# 보유금액
wallet = 0
# 평단가
avg_price = 0
period = 300

file_name = "ta_TQQQ_1d_2012-01-03_2022-12-12"
df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\{}.csv".format(file_name), sep=",")

# print(df)

# 시작
start_index = len(df['Open'])-365
#끝
end_index = len(df['Open'])

print("최종 결과,", "현재 보유금액,", "현재 가격,", "보유 개수")
# print(rsi_trade(df, wallet, start_index, end_index))
# # print(inverse_stochastic_trade(df, inverse_df, wallet, start_index, end_index))
# print(rsi_sell_by_avg_price(df, wallet, start_index, end_index))
# print(stochastic_trade(df, wallet, start_index, end_index))
# print(stochastic_sell_by_avg_price(df, wallet, start_index, end_index))
# print(laor_algorithm(df, wallet, start_index, end_index))
print(day_trade.macd_trade(df, wallet, start_index, end_index))

# 주기적 반복
# print("전체 결과", "보유금액", "현재가격", "보유 개수")
# for i in range(0,len(df['Open']),period):
#     print(i)
#     #시작
#     start_index = i
#     #끝
#     end_index = i+period

#     print(rsi_sell_by_avg_price(df, wallet, start_index, end_index))
