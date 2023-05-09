import pandas as pd
from backtesting import day_trade
from crawling import crawling, technical_analysis
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import common


wallet = 0
# 평단가
avg_price = 0

"""
전 종목, 모든 알고리즘 테스트
"""
def all_stocks_all_algorithm_test(surplus_cash, start_index, end_index):
    stocks = common.all_stocks()
    result_df = pd.DataFrame(columns=['stock', 'just_stay', 'rsi', 'rsi_sell_by_avg', 'mfi', 'stochastic', 'stochastic_sell_by_avg', 'laor'])

    for i in range(len(stocks)):
        df = common.load_csv(stocks[i])
        result_df.loc[i] = [stocks[i],
                            day_trade.just_stay(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.rsi_trade(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.rsi_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.mfi_trade(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.stochastic_trade(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.stochastic_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.laor_algorithm(df, wallet, surplus_cash, start_index, end_index)[0]]
    return result_df

"""
과거 전체 기간동안 주어진 기간 반복하여 테스트
"""
def repeat_period_test(df, test_case, day_period, surplus_cash):
    for i in range(0,len(df['Open']), day_period):
        if(i>len(df['Open'])-day_period):
            break
        start_index = i
        end_index = i + day_period

        common.find_test_case(test_case, df, wallet, surplus_cash, start_index, end_index)