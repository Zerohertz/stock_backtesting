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

    """
    수집 데이터 정의
    """
    interval_time = "1d"
    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    """
    데이터 수집 및 기술적 지표 추가
    """
    # # 데이터 수집
    # crawling.crawl_all_stock_data(start_crawl_date, end_crawl_date, interval_time="1d")

    # # 통계적 지표 추가
    # technical_analysis.add_ta_to_all_df(start_crawl_date, end_crawl_date, interval_time="1d")

    # 주식장 열리는 날을 제외하고 입력해야함
    start_date = '2021-08-19'
    end_date = '2023-05-15'

    # # 하루 최대 투자 금액(달러)
    surplus_cash = 500


    """
    복합 테스트
    """
    test.all_stocks_all_algorithm_test(surplus_cash, start_crawl_date, end_crawl_date, start_date, end_date)