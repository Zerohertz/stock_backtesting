import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common

"""
RSI 알고리즘 시에 지표 몇에서 매수 매도 하는 것이 좋은지 테스트 하기 위함, 최소 1시간 이상 소요..
"""
if __name__ == '__main__':

    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    start_date = '2018-01-03'
    end_date = '2023-05-15'

    # 하루 최대 투자 금액(달러)
    surplus_cash = 500

    # 알고리즘, 종목 정하기
    test_case = "rsi"
    stock = "UPRO"

    # 반복 주기 테스트 분기기간(일), 280이 약 1년
    day_period = 500

    result_df = pd.DataFrame(columns = ['rsi_sell_loc', 'rsi_buy_loc', 'win_rate', 'profit', 'avg_profit_rate', 'max_profit_rate', 'min_profit_rate', 'capital_needs'])

    index = 0
    for rsi_sell_loc in range(50, 80):
        for rsi_buy_loc in range(30, 60):
            print(rsi_sell_loc, rsi_buy_loc)
            tmp_result = test.win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc)

            tmp_result[0] = rsi_sell_loc
            tmp_result[1] = rsi_buy_loc

            result_df.loc[index] = tmp_result
            index += 1
            # [stock, test_case, win_rate, avg_profit, avg_profit_rate, max_profit_rate, min_profit_rate, capital_needs]

    result_df = result_df.sort_values(by = ['win_rate'], ascending=False)
    result_df.to_csv("result_data/rsi_test_data/{0}_{1}.csv".format(stock, test_case), encoding="utf8")