import pandas as pd
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
    company = "TQQQ"
    interval_time = "1d"
    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-15'
    stock_code = "{0}_{1}_{2}_{3}".format(company, interval_time, start_crawl_date, end_crawl_date)

    # 데이터 로드
    df = common.load_csv(stock_code)

    # 현재 재산
    wallet = 0

    # 주식장 열리는 날을 제외하고 입력해야함
    start_date = '2017-01-05'
    end_date = '2023-05-04'

    # 하루 최대 투자 금액(달러)
    surplus_cash = 750

    # 어떤 알고리즘으로 테스트할 건지 테스트 케이스 정의
    test_case = "RSI_가중치_매수"

    start_index = common.get_index_by_date(df, start_date)
    end_index = common.get_index_by_date(df, end_date)
    rsi_sell_loc = 60
    rsi_buy_loc = 50

    print()
    print("종목", company)
    print("기간", start_date, "~", end_date)
    common.find_test_case(df, test_case, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)