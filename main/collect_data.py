import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test

import common

"""
데이터 수집 및 기술적 지표 추가
"""
if __name__ == '__main__':

    """
    수집 데이터 정의
    """
    interval_time = "1d"
    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    # 데이터 수집
    crawling.crawl_all_stock_data(start_crawl_date, end_crawl_date, interval_time="1d")

    # 통계적 지표 추가
    technical_analysis.add_ta_to_all_df(start_crawl_date, end_crawl_date, interval_time="1d")