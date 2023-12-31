import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common

"""
RSI 두번 매수 알고리즘 시에 각 기간별로 지표 몇에서 매수 매도 하는 것이 좋은지 테스트, 최소 12시간 이상 소요..
"""
if __name__ == '__main__':

    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    start_date = '2015-01-05'
    end_date = '2023-05-15'

    # 하루 최대 투자 금액(달러)
    surplus_cash = 500

    # 알고리즘, 종목 정하기
    test_case = "rsi_buy_weight_trade"
    stock = "UPRO"

    # 반복 주기 테스트 분기기간(일), 280이 약 1년
    day_period = 400

    result_df = pd.DataFrame(columns = ['rsi_sell_loc', 'rsi_first_buy_loc', 'rsi_buy_loc', 'win_rate', 'profit', 'avg_profit_rate', 'max_profit_rate', 'min_profit_rate', 'capital_needs'])

    index = 0
    start = 70
    end = 78 # 78까지
    for rsi_sell_loc in range(start, end):
        for rsi_first_buy_loc in range(45, 60):
            for rsi_buy_loc in range(38, 55):
                print(rsi_sell_loc, rsi_first_buy_loc, rsi_buy_loc)
                tmp_result = test.win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc, rsi_first_buy_loc)

                tmp_result[0] = rsi_first_buy_loc
                tmp_result[1] = rsi_buy_loc
                tmp_result.insert(0, rsi_sell_loc)
                # print(tmp_result)
                result_df.loc[index] = tmp_result
                index += 1
            # [stock, test_case, win_rate, avg_profit, avg_profit_rate, max_profit_rate, min_profit_rate, capital_needs]

    result_df = result_df.sort_values(by = ['win_rate'], ascending=False)
    result_df.to_csv("result_data/rsi_buy_weight_win_rate_test_result/{0}_{1}_{2}_{3}_{4}_{5}_{6}.csv".format(start_date, end_date, stock, test_case, day_period, start, end), encoding="utf8")