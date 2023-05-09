import pandas as pd
from backtesting import day_trade
from crawling import crawling, technical_analysis
import common

stocks = common.stocks
wallet = 0
# 평단가
avg_price = 0

# 전체 결과 만들기 테스트
def make_all_result():
    result_df = pd.DataFrame(columns=['stock', 'just_stay', 'rsi', 'rsi_sell_by_avg', 'mfi', 'stochastic', 'stochastic_sell_by_avg', 'laor', 'macd'])

    for i in range(len(stocks)):
        file_name = "ta_{}_1d_max".format(stocks[i])
        df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\ta_data\{}.csv".format(file_name), sep=",")
        print(stocks[i])
        start_index = get_best_season(i)[0]#1
        end_index = get_best_season(i)[1]-1#len(df['Open'])-1
        result_df.loc[i] = [stocks[i], day_trade.just_stay(df, wallet, start_index, end_index)[0], day_trade.rsi_trade(df, wallet, start_index, end_index)[0], day_trade.rsi_sell_by_avg_price(df, wallet, start_index, end_index)[0], day_trade.mfi_trade(df, wallet, start_index, end_index)[0], day_trade.stochastic_trade(df, wallet, start_index, end_index)[0], day_trade.stochastic_sell_by_avg_price(df, wallet, start_index, end_index)[0], day_trade.laor_algorithm(df, wallet, start_index, end_index)[0], day_trade.macd_trade(df, wallet, start_index, end_index)[0]]

    return result_df

"""
과거 전체 기간동안 주어진 기간 반복하여 테스트
"""
def repeat_period_test(df, day_period, surplus_cash, test_case):
    for i in range(0,len(df['Open']), day_period):
        if(i>len(df['Open'])-day_period):
            break
        start_index = i
        end_index = i + day_period

        common.find_test_case(test_case, df, wallet, surplus_cash, start_index, end_index)

# print(make_all_result())