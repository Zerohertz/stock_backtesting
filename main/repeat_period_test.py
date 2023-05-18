import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common

"""
복수 종목 반복 테스트
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
    # 데이터 수집
    # crawling.crawl_all_stock_data(start_crawl_date, end_crawl_date, interval_time="1d")

    # 통계적 지표 추가
    # technical_analysis.add_ta_to_all_df(start_crawl_date, end_crawl_date, interval_time="1d")

    # 데이터 로드
    # df = common.load_csv(stock_code)


    # # 하루 최대 투자 금액(달러)
    surplus_cash = 500

    # # 어떤 알고리즘으로 테스트할 건지 테스트 케이스 정의
    test_case = "RSI"

    # # # 반복 주기 테스트 분기기간(일), 280이 약 1년
    day_period = 180

    rsi_sell_loc = 60
    rsi_buy_loc = 50

    test.repeat_period_test(test_case, start_crawl_date, end_crawl_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc)