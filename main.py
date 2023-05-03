import pandas as pd
from backtesting import day_trade
from crawling import crawling, technical_analysis
# from test import test
import common


if __name__ == '__main__':

    # 수집할 데이터 정의
    company = "UPRO"
    interval_time = "1d"
    start_date = '2012-01-03'
    end_date = '2023-05-04'
    stock_code = "{0}_{1}_{2}_{3}".format(company, interval_time, start_date, end_date)

    # 데이터 수집
    # crawling.crawl_stock_data(start_date, end_date, company, interval_time="1d")

    # 통계적 지표 추가
    # technical_analysis.add_ta_to_df(stock_code)

    # 데이터 로드
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\ta_data\ta_{}.csv".format(stock_code), sep=",")


    wallet = 0
    # 평단가
    # avg_price = 0
    # period = 190
    print("종목명", stock_code)
    print("최종 결과,", "현재 보유금액,", "현재 가격,", "보유 개수", "자본금")
    print(day_trade.just_stay(df, wallet, start_date, end_date))
    print(day_trade.rsi_trade(df, wallet, start_date, end_date))
    print(day_trade.rsi_sell_by_avg_price(df, wallet, start_date, end_date))
    print(day_trade.stochastic_trade(df, wallet, start_date, end_date))
    print(day_trade.stochastic_sell_by_avg_price(df, wallet, start_date, end_date))
    print(day_trade.laor_algorithm(df, wallet, start_date, end_date))
    # print(day_trade.macd_trade(df, wallet, start_date, end_date))

    # 테스트
    # repeat_period_test(period, file_name)