import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common

"""
단일 종목 테스트
"""
if __name__ == '__main__':

    """
    수집 데이터 정의
    """
    stock = "UPRO"
    interval_time = "1d"
    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'

    # 데이터 로드
    df = common.load_ta_csv(stock, start_crawl_date, end_crawl_date, interval_time="1d")

    # 현재 재산
    wallet = 0

    # 주식장 열리는 날을 제외하고 입력해야함
    start_date = '2017-01-03'
    end_date = '2023-05-04'

    # 하루 최대 투자 금액(달러)
    surplus_cash = 1000

    # 어떤 알고리즘으로 테스트할 건지 테스트 케이스 정의
    test_case = "rsi"

    start_index = common.get_index_by_date(df, start_date)
    end_index = common.get_index_by_date(df, end_date)
    rsi_sell_loc = 72
    rsi_buy_loc = 50

    print()
    print("종목", stock)
    print("기간", start_date, "~", end_date)
    common.find_test_case(df, test_case, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)