# 평단가 구하는 메소드(잘못된듯, wallet으로 구하면 안되고 팔기 이후로 구해야함....)
def get_avg_price(tmp_avg_price, cnt):
    if(cnt>0):
        avg_price = tmp_avg_price//cnt
    else:
        avg_price = tmp_avg_price
    return avg_price

def get_result(wallet, df, cnt):
    result = []
    result.append(wallet + cnt*df['Open'][len(df['STOCHk_14_3_3'])-1])
    result.append(wallet)
    result.append(df['Open'][len(df['STOCHk_14_3_3'])-1])
    result.append(cnt)
    return result

# 실현손익
def get_revenue(tmp_sum_price, sell_price, cnt):
    return (tmp_sum_price - (sell_price * cnt))

# 스토캐스틱 알고리즘
def stochastic_trade(df, wallet, start_index, end_index):
    print("스토캐스틱 알고리즘")
    cnt = 0
    for i in range(start_index, end_index):
        # print("보유금액", wallet)
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=30):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=70 and cnt >= 1):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
    result = get_result(wallet, df, cnt)
    return result

# 인버스 적용한 스토캐스틱 알고리즘
def inverse_stochastic_trade(df, inverse_df, wallet, start_index, end_index):
    print("인버스 적용 스토캐스틱 알고리즘")
    cnt = 0
    inverse_cnt = 0
    for i in range(start_index, end_index):
        # print(wallet)
        # print("보유금액", wallet)
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20 and inverse_cnt >= 0):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            wallet = wallet + (inverse_df['Open'][i]*inverse_cnt)
            cnt=cnt+1
            inverse_cnt = 0

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=70 and cnt >= 0):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            wallet = wallet - inverse_df['Open'][i]
            cnt=0
            inverse_cnt = inverse_cnt+1
    result = get_result(wallet, df, cnt)
    return result

# rsi 구매 알고리즘
def rsi_trade(df, wallet, start_index, end_index):
    print("RSI 알고리즘")
    result = []
    cnt = 0
    tmp_avg_price = 0
    for i in range(start_index, end_index):
        # print("보유금액", wallet)
        # 40이상이면 사기
        if(df['RSI_14'][i] <40):
            # print("사!", i, df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_avg_price = tmp_avg_price + df['Open'][i]
        # 60 이상이면 팔기
        elif(df['RSI_14'][i] >=60 and cnt >= 1):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_avg_price=0
    avg_price = get_avg_price(tmp_avg_price, cnt)
    result = get_result(wallet, df, cnt)
    return result

# MACD 추가해야함
def macd_trade(df, wallet, start_index, end_index):
    print("MACD 알고리즘")
    result = []
    cnt = 0
    tmp_avg_price = 0
    for i in range(start_index, end_index):
        # print("보유금액", wallet)
        # 40이상이면 사기
        if(df['RSI_14'][i] <40):
            # print("사!", i, df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_avg_price = tmp_avg_price + df['Open'][i]
        # 60 이상이면 팔기
        elif(df['RSI_14'][i] >=60 and cnt >= 1):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_avg_price=0
    avg_price = get_avg_price(tmp_avg_price, cnt)
    result = get_result(wallet, df, cnt)
    return result


# rsi 평단가 판매 알고리즘
def rsi_sell_by_avg_price(df, wallet, start_index, end_index):
    print("스토캐스틱 알고리즘, 판매가중치")
    result = []
    cnt = 0
    tmp_avg_price = 0
    for i in range(start_index, end_index):
        # print("보유금액", wallet)
        # 40이상이면 사기
        if(df['RSI_14'][i] <40):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_avg_price = tmp_avg_price + df['Open'][i]
        # 60 이상이면 팔기
        elif(cnt >= 1 and (df['Open'][i] >= (get_avg_price(tmp_avg_price, cnt)*1.15) )):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_avg_price=0
    avg_price = get_avg_price(tmp_avg_price, cnt)
    result = get_result(wallet, df, cnt)
    return result

# 스토캐스틱 알고리즘 평단가 판매가중치
def stochastic_sell_by_avg_price(df, wallet, start_index, end_index):
    print("스토캐스틱 알고리즘, 판매가중치")
    result = []
    cnt = 0
    tmp_avg_price = 0
    for i in range(start_index, end_index):
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_avg_price = tmp_avg_price + df['Open'][i]

        # 평단가 기준으로 팔기
        elif(cnt >= 1 and df['Open'][i] >= (get_avg_price(tmp_avg_price, cnt)*1.1)):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_avg_price=0
    result = get_result(wallet, df, cnt)
    return result

# 라오어 알고리즘
def laor_algorithm(df, wallet, start_index, end_index):
    print("라오어 알고리즘 결과")
    result = []
    cnt = 0
    tmp_avg_price = 0
    for i in range(start_index, end_index):
        # print("보유금액", wallet)
        # print("사!", df['Open'][i])
        wallet = wallet - df['Open'][i]
        cnt=cnt+1
        tmp_avg_price = tmp_avg_price + df['Open'][i]

        if(cnt >= 1 and df['Open'][i] >= (get_avg_price(tmp_avg_price, cnt)*1.1)):
            # print("팔아!", df['Open'][i])
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_avg_price=0
    result = get_result(wallet, df, cnt)
    return result

if __name__ == '__main__':

    # Load data
    df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\TQQQ_1d_2012-01-14_2022-12-12.csv", sep=",")
    inverse_df = pd.read_csv(r"C:\Users\eunhak\Documents\project\stock_backtesting_platform\data\SQQQ_1d_2019-01-14_2022-12-12.csv", sep=",")
    # Create your own Custom Strategy
    DayStochasticStrategy = ta.Strategy(
        name="stochastic",
        description="stochastic",
        ta=[
            {"kind": "stoch"},
        ]
    )

    DayRsiStrategy = ta.Strategy(
        name="rsi",
        description="rsi",
        ta=[
            {"kind": "rsi"},
        ]
    )

    MyStrategy = ta.Strategy(
        name="rsi",
        description="rsi",
        ta=[
            {"kind": "rsi"},
            {"kind": "stoch"},
            {"kind": "macd"}
        ]
    )

    # 전략설정
    df.ta.strategy(MyStrategy)

    # 보유금액
    wallet = 0

    # 평단가
    avg_price = 0

    period = 300

    # 주기적 반복
    # print("전체 결과", "보유금액", "현재가격", "보유 개수")
    # for i in range(0,len(df['Open']),period):
    #     print(i)
    #     #시작
    #     start_index = i
    #     #끝
    #     end_index = i+period

    #     print(rsi_sell_by_avg_price(df, wallet, start_index, end_index))

    # 시작
    start_index = 750 #len(df['Open'])-365

    #끝
    end_index = 985 #len(df['Open'])

    print("전체 결과", "보유금액", "현재가격", "보유 개수")
    print(rsi_trade(df, wallet, start_index, end_index))
    print(inverse_stochastic_trade(df, inverse_df, wallet, start_index, end_index))
    print(rsi_sell_by_avg_price(df, wallet, start_index, end_index))
    print(stochastic_trade(df, wallet, start_index, end_index))
    print(stochastic_sell_by_avg_price(df, wallet, start_index, end_index))
    print(laor_algorithm(df, wallet, start_index, end_index))