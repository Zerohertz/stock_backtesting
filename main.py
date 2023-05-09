import pandas as pd
from backtesting import day_trade
from crawling import crawling, technical_analysis
from simulation import test
import common


if __name__ == '__main__':


    """
    수집 데이터 정의
    """
    company = "UPRO"
    interval_time = "1d"
    start_crawl_date = '2012-01-03'
    end_crawl_date = '2023-05-04'
    stock_code = "{0}_{1}_{2}_{3}".format(company, interval_time, start_crawl_date, end_crawl_date)

    """
    데이터 수집 및 기술적 지표 추가
    """
    # 데이터 수집
    # crawling.crawl_stock_data(start_date, end_date, company, interval_time="1d")

    # 통계적 지표 추가
    # technical_analysis.add_ta_to_df(stock_code)

    # 데이터 로드
    df = common.load_csv(stock_code)

    """
    단일 테스트
    """
    # 현재 재산
    wallet = 0
    start_date = '2023-01-03'
    end_date = '2023-05-04'

    # 하루 최대 투자 금액
    surplus_cash = 200

    # 어떤 알고리즘으로 테스트할 건지 테스트 케이스 정의
    test_case = "RSI"

    day_period = 180

    # 평단가
    # avg_price = 0

    start_index = common.get_index_by_date(df, start_date)
    end_index = common.get_index_by_date(df, end_date)

    print()
    print("종목", company)
    common.find_test_case(df, test_case, wallet, surplus_cash, start_index, end_index)

    """
    복합 테스트
    """
    # test.repeat_period_test(df, test_case, day_period, surplus_cash)
    # test.all_stocks_all_algorithm_test(surplus_cash, start_index, end_index)