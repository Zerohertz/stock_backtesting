import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common

"""
기간별 반복하며 승률 테스트
"""
if __name__ == '__main__':

    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    start_date = '2017-01-03'
    end_date = '2023-05-15'

    # # 하루 최대 투자 금액(달러)
    surplus_cash = 350

    # 알고리즘, 종목 정하기
    test_case = "rsi"
    stock = "UPRO"

    # # # 반복 주기 테스트 분기기간(일), 280이 약 1년
    day_period = 280

    rsi_sell_loc = 72
    rsi_buy_loc = 49

    test.win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc)