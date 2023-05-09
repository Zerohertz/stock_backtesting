from backtesting import day_trade

stocks = ["QQQ", "QLD", "TQQQ", "PSQ", "SQQQ", "DIA", "DDM", "UDOW", "ARKK", "IVV", "SSO", "UPRO", "FNGU", "BULZ"]

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
테스트 알고리즘 분기시켜 주는 메소드
"""
def find_test_case(test_case, df, wallet, surplus_cash, start_index, end_index):
    print("현재 총 자산,", "현재 보유 금액,", "현재 주식 가격,", "주식 보유 개수,", "총 투자 필요금액(자본)")

    if(test_case == "all"):
        print(day_trade.just_stay(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "존버"):
        print(day_trade.just_stay(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "RSI"):
        print(day_trade.rsi_trade(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "RSI_평단가매도"):
        print(day_trade.rsi_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "스토캐스틱"):
        print(day_trade.stochastic_trade(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "스토캐스틱_평단가매도"):
        print(day_trade.stochastic_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "라오어"):
        print(day_trade.laor_algorithm(df, wallet, surplus_cash, start_index, end_index))
    elif(test_case == "MACD"):
        print(day_trade.macd_trade(df, wallet, start_index, end_index))