import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test

import common

"""
전 종목 전 알고리즘 테스트
"""
if __name__ == '__main__':

    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    # 주식장 열리는 날을 제외하고 입력해야함
    start_date = '2022-01-04'
    end_date = '2022-12-23'

    # 하루 최대 투자 금액(달러)
    surplus_cash = 500

    """
    복합 테스트
    """
    test.all_stocks_all_algorithm_test(surplus_cash, start_crawl_date, end_crawl_date, start_date, end_date)