from backtesting import day_trade
from simulation import test
import pandas as pd

def get_all_stocks():
    stocks = ["QQQ", "QLD", "TQQQ", "PSQ", "SQQQ", "DIA", "DDM", "UDOW", "ARKK", "IVV", "SSO", "UPRO", "FNGU", "BULZ"]
    return stocks

"""
날짜로 해당 인덱스 찾아주는 메소드
"""
def get_index_by_date(df, date):
    # 주어진 날짜에 해당하는 인덱스 반환
    for i in range(len(df['Date'])):
        if(df['Date'][i]==date):
            return i
    return len(df['Date'])-1


"""
CSV 데이터 불러오기
"""
def load_csv(stock, start_crawl_date, end_crawl_date, interval_time="1d"):
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\{0}_{1}_{2}_{3}.csv".format(stock, interval_time, start_crawl_date, end_crawl_date), sep=",")
    return df

"""
기술적 지표 포함된 csv 불러오기
"""
def load_ta_csv(stock, start_crawl_date, end_crawl_date, interval_time="1d"):
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\ta_data\ta_{0}_{1}_{2}_{3}.csv".format(stock, interval_time, start_crawl_date, end_crawl_date), sep=",")
    return df

"""
테스트 알고리즘 분기시켜 주는 메소드
"""
def find_test_case(df, test_case,  wallet, surplus_cash, start_index, end_index, rsi_sell_loc=60, rsi_buy_loc=50):

    if(test_case == "존버"):
        print("존버 알고리즘")
        return day_trade.just_stay(df, wallet, surplus_cash, start_index, end_index)
    elif(test_case == "RSI"):
        print("RSI 알고리즘")
        print("매도 지표", rsi_sell_loc)
        print("매수 지표", rsi_buy_loc)
        return day_trade.rsi_trade(df, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)
    elif(test_case == "RSI_가중치_매수"):
        return day_trade.rsi_buy_weight_trade(df, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)
    elif(test_case == "RSI_평단가매도"):
        print("RSI 알고리즘, 판매가중치")
        return day_trade.rsi_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index)
    elif(test_case == "스토캐스틱"):
        print("스토캐스틱 알고리즘")
        return day_trade.stochastic_trade(df, wallet, surplus_cash, start_index, end_index)
    elif(test_case == "스토캐스틱_평단가매도"):
        print("스토캐스틱 알고리즘, 판매가중치")
        return day_trade.stochastic_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index)
    elif(test_case == "라오어"):
        print("라오어 알고리즘 결과")
        return day_trade.laor_algorithm(df, wallet, surplus_cash, start_index, end_index)
    elif(test_case == "MACD"):
        print("MACD 알고리즘")
        return day_trade.macd_trade(df, wallet, start_index, end_index)
    elif(test_case == "전체"):
        print("전체 테스트")
        return day_trade.all_algorithm_test(df, wallet, surplus_cash, start_index, end_index)