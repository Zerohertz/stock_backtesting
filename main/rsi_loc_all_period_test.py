import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common

"""
RSI 알고리즘 시에 전체 기간에서 지표 몇에서 매수 매도 하는 것이 좋은지 테스트
"""
if __name__ == '__main__':

    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    start_date = '2015-01-05'
    end_date = '2023-05-15'

    # 하루 최대 투자 금액(달러)
    surplus_cash = 500

    # 알고리즘, 종목 정하기
    test_case = "rsi"
    stock = "UPRO"

    df = common.load_ta_csv(stock, start_crawl_date, end_crawl_date, interval_time="1d")

    start_index = common.get_index_by_date(df, start_date)
    end_index = common.get_index_by_date(df, end_date)

    result_df = pd.DataFrame(columns = ['rsi_sell_loc', 'rsi_buy_loc', 'profit', 'profit_rate', 'capital_needs'])

    index = 0
    for rsi_sell_loc in range(50, 80):
        for rsi_buy_loc in range(30, 60):

            wallet = 0
            print(rsi_sell_loc, rsi_buy_loc)
            tmp_result = day_trade.rsi_trade(df, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)

            #[profit, profit_rate, capital_needs]

            tmp_result.insert(0, rsi_sell_loc)
            tmp_result.insert(1, rsi_buy_loc)

            result_df.loc[index] = tmp_result
            index += 1

    result_df = result_df.sort_values(by = ['profit'], ascending=False)
    result_df.to_csv("result_data/rsi_all_period_test_data/{0}_{1}_{2}_{3}.csv".format(start_date, end_date, stock, test_case), encoding="utf8")