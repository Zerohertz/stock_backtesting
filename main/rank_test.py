import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from simulation import test
import common

"""
기간별 반복하며 승률 순위 테스트, 약 15분 정도 걸림
"""
if __name__ == '__main__':

    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    start_date = '2015-01-05'
    end_date = '2023-05-15'

    # # 하루 최대 투자 금액(달러)
    surplus_cash = 400

    # # # 반복 주기 테스트 분기기간(일), 280이 약 1년
    day_period = 280

    rsi_sell_loc = 72
    rsi_first_buy_loc = 50
    rsi_buy_loc = 40


    result_df = test.win_rate_rank_test(start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc, rsi_first_buy_loc)

    print(result_df)
    result_df.to_csv("result_data/rank_test_data/{0}_{1}_{2}_{3}_{4}_{5}.csv".format(start_date, end_date, day_period, rsi_sell_loc, rsi_first_buy_loc, rsi_buy_loc), encoding="utf8")