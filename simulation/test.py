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
def all_stocks_all_algorithm_test(surplus_cash, start_crawl_date, end_crawl_date, start_date, end_date):
    stocks = common.get_all_stocks()
    result_df = pd.DataFrame(columns=['stock', 'just_stay', 'rsi', 'rsi_buy_weight_trade',  'rsi_sell_by_avg', 'mfi', 'stochastic', 'stochastic_sell_by_avg', 'laor'])

    for i in range(len(stocks)):
        df = common.load_ta_csv(stocks[i], start_crawl_date, end_crawl_date)
        # print(df)
        start_index = common.get_index_by_date(df, start_date)
        end_index = common.get_index_by_date(df, end_date)
        result_df.loc[i] = [stocks[i],
                            day_trade.just_stay(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.rsi_trade(df, wallet, surplus_cash, start_index, end_index),
                            day_trade.rsi_buy_weight_trade(df, wallet, surplus_cash, start_index, end_index, rsi_sell_loc=60, rsi_buy_loc=40),
                            day_trade.rsi_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index),
                            day_trade.mfi_trade(df, wallet, surplus_cash, start_index, end_index),
                            day_trade.stochastic_trade(df, wallet, surplus_cash, start_index, end_index),
                            day_trade.stochastic_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index),
                            day_trade.laor_algorithm(df, wallet, surplus_cash, start_index, end_index)
                            ]

    print(result_df)
    return result_df

"""
과거 전체 기간동안 주어진 기간 반복하여 테스트
"""
def repeat_period_test(test_case, start_crawl_date, end_crawl_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc):

    stocks = common.get_all_stocks()
    df = common.load_ta_csv(stocks[0], start_crawl_date, end_crawl_date)
    stocks.insert(0, "Date")
    result_df = pd.DataFrame(columns = stocks)

    for i in range(0, len(df['Open']), day_period):
        if(i>len(df['Open'])):
            break
        start_index = i
        end_index = i + day_period
        tmp = [df['Date'][start_index]]

        for j in range(1, len(stocks)):
            tmp_df = common.load_ta_csv(stocks[j], start_crawl_date, end_crawl_date)
            tmp.append(common.find_test_case(tmp_df, test_case, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc))

        result_df.loc[i] = tmp
    print(result_df)

"""
과거 전체 기간동안 매일 계산하며 승률 테스트
"""
def win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc):

    df = common.load_ta_csv(stock, start_crawl_date, end_crawl_date)
    profits = []
    total_profit = 0
    win_cnt = 0
    lose_cnt = 0
    tmp_win_sum = 0
    tmp_lose_sum = 0

    start_index = common.get_index_by_date(df, start_date)
    end_index = common.get_index_by_date(df, end_date)

    for i in range(start_index, end_index):
        if(i>len(df['Open']) - day_period):
            break
        start_index = i
        end_index = i + day_period
        result = common.find_test_case(df, test_case, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)

        if(result >= 0):
            win_cnt += 1
            tmp_win_sum += result
        else:
            lose_cnt+=1
            tmp_lose_sum += result
        total_profit += result
        profits.append(result)

    print()
    print("현황", profits)
    print("승률", round(((win_cnt) / (win_cnt+lose_cnt) * 100), 2), "%")
    print("평균 총 수익", total_profit // (win_cnt+lose_cnt), "$")
    print("평균 승리 수익", tmp_win_sum // win_cnt, "$")
    print("평균 패배 손실", tmp_lose_sum // lose_cnt, "$")
    print("승수", win_cnt)
    print("패수", lose_cnt)