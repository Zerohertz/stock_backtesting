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

    start_date = '2018-01-03'
    end_date = '2023-05-15'

    # # 하루 최대 투자 금액(달러)
    surplus_cash = 500

    # # 어떤 알고리즘으로 테스트할 건지 테스트 케이스 정의
    test_case = "RSI"
    stock = "UPRO"

    # # # 반복 주기 테스트 분기기간(일), 280이 약 1년
    day_period = 270

    rsi_sell_loc = 60
    rsi_buy_loc = 50

    test.win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc)