import pandas as pd
from backtesting import day_trade

wallet = 0
# 평단가
avg_price = 0

stocks = ["QQQ", "QLD", "TQQQ", "PSQ", "SQQQ", "DIA", "ARKK"]

file_name = "ta_PSQ_1d_2012-01-03_2022-12-22"
df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\ta_data\{}.csv".format(file_name), sep=",")

start_index = len(df['Open'])-365
end_index = len(df['Open'])-1

# 최고의 장 2020년 3월 25일 ~ 2021년 12월 29일, 2071 ~ 2516 가만히 있어도 약 QQQ 기준215불 수익, ARK는 1357~1802
# best_season = [2071,2516]
# start_index = best_season[0]
# end_index = best_season[1]

# 최악의 장 2022년 1월 4일 ~ 2022년 12월 23일, 2520 ~ 2700, ARK는 1820~2049
# worst_season = [2520,2700]
# start_index = worst_season[0]
# end_index = worst_season[1]

# print("파일명", file_name)
# print("최종 결과,", "현재 보유금액,", "현재 가격,", "보유 개수")
# print(day_trade.just_stay(df, wallet, start_index, end_index))
# print(day_trade.rsi_trade(df, wallet, start_index, end_index))
# print(day_trade.rsi_sell_by_avg_price(df, wallet, start_index, end_index))
# print(day_trade.stochastic_trade(df, wallet, start_index, end_index))
# print(day_trade.stochastic_sell_by_avg_price(df, wallet, start_index, end_index))
# print(day_trade.laor_algorithm(df, wallet, start_index, end_index))
# print(day_trade.macd_trade(df, wallet, start_index, end_index))


# 전체 결과 만들기 테스트
def make_all_result():
    result_df = pd.DataFrame(columns=['stock', 'just_stay', 'rsi', 'rsi_sell_by_avg', 'stochastic', 'stochastic_sell_by_avg', 'laor', 'macd'])

    for i in range(len(stocks)):
        file_name = "ta_{}_1d_2012-01-03_2022-12-22".format(stocks[i])
        df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\ta_data\{}.csv".format(file_name), sep=",")
        # if(stocks[i]=="ARKK"):
        #     start_index = 1357
        #     end_index = 1802
        # else:
        #     start_index = 2071
        #     end_index = 2516
        start_index = 0
        end_index = len(df['Open'])-1
        result_df.loc[i] = [stocks[i], day_trade.just_stay(df, wallet, start_index, end_index)[0], day_trade.rsi_trade(df, wallet, start_index, end_index)[0], day_trade.rsi_sell_by_avg_price(df, wallet, start_index, end_index)[0], day_trade.stochastic_trade(df, wallet, start_index, end_index)[0], day_trade.stochastic_sell_by_avg_price(df, wallet, start_index, end_index)[0], day_trade.laor_algorithm(df, wallet, start_index, end_index)[0], day_trade.macd_trade(df, wallet, start_index, end_index)[0]]

    print(result_df)

# 주기적 반복
def repeat_period_test():
    stock = "DIA"
    period = 300
    file_name = "ta_{}_1d_2012-01-03_2022-12-22".format(stock)
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\ta_data\{}.csv".format(file_name), sep=",")
    print("전체 결과", "보유금액", "현재가격", "보유 개수")
    for i in range(0,len(df['Open']),period):
        if(i>len(df['Open'])-period):
            break
        start_index = i
        end_index = i+period

        # print(day_trade.just_stay(df, wallet, start_index, end_index))
        # print(day_trade.rsi_trade(df, wallet, start_index, end_index))
        # print(day_trade.rsi_sell_by_avg_price(df, wallet, start_index, end_index))
        # print(day_trade.stochastic_trade(df, wallet, start_index, end_index))
        # print(day_trade.stochastic_sell_by_avg_price(df, wallet, start_index, end_index))
        # print(day_trade.laor_algorithm(df, wallet, start_index, end_index))
        # print(day_trade.macd_trade(df, wallet, start_index, end_index))

# make_all_result()
repeat_period_test()