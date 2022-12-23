import pandas as pd

# 평단가 구하는 메소드
def get_avg_price(tmp_sum_price, cnt):
    if(cnt>0):
        avg_price = tmp_sum_price/cnt
    else:
        avg_price = tmp_sum_price
    return avg_price

def get_round(num):
    return round(num, 2)

def get_result(wallet, df, cnt):
    result = []
    result.append(get_round(wallet + cnt*df['Open'][len(df['STOCHk_14_3_3'])-1]))
    result.append(get_round(wallet))
    result.append(get_round(df['Open'][len(df['STOCHk_14_3_3'])-1]))
    result.append(cnt)
    return result

# 실현손익
def get_revenue(tmp_sum_price, sell_price, cnt):
    return (sell_price * cnt - tmp_sum_price)

# 존버 알고리즘
def just_stay(df, wallet, start_index, end_index):
    wallet = wallet - df['Open'][start_index]
    wallet = wallet + df['Open'][end_index]
    return [get_round(wallet), get_round(wallet), get_round(df['Open'][end_index]), 0]

# 스토캐스틱 알고리즘
def stochastic_trade(df, wallet, start_index, end_index):
    print("스토캐스틱 알고리즘")
    cnt = 0
    for i in range(start_index, end_index):
        # 30 이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=30):
            wallet = wallet - df['Open'][i]
            cnt=cnt+1

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=70 and cnt >= 1):
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
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20 and inverse_cnt >= 0):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            wallet = wallet + (inverse_df['Open'][i]*inverse_cnt)
            cnt=cnt+1
            inverse_cnt = 0

        # 70 이상이면 팔기
        elif(df['STOCHk_14_3_3'][i] >=70 and cnt >= 0):
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
    tmp_sum_price = 0
    for i in range(start_index, end_index):
        # 40이상이면 사기
        if(df['RSI_14'][i] <40):
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_sum_price = tmp_sum_price + df['Open'][i]
        # 60 이상이면 팔기
        elif(df['RSI_14'][i] >=60 and cnt >= 1):
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_sum_price=0
    result = get_result(wallet, df, cnt)
    return result

# MACD 알고리즘 양수 돌파 매수, 음수 돌파 매도,
def macd_trade(df, wallet, start_index, end_index):
    print("MACD 알고리즘")
    result = []
    cnt = 0
    tmp_sum_price = 0
    for i in range(start_index, end_index):
        # 양수 돌파 매수
        if(df['MACD_12_26_9'][i-1] < 0 and df['MACD_12_26_9'][i] > 0):
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_sum_price = tmp_sum_price + df['Open'][i]
        # 음수 돌파 매도
        elif(df['MACD_12_26_9'][i-1] > 0 and df['MACD_12_26_9'][i] < 0):
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_sum_price=0
    result = get_result(wallet, df, cnt)
    return result

# MACD 알고리즘
def macd_3_days_trade(df, wallet, start_index, end_index):
    print("MACD 알고리즘")
    result = []
    cnt = 0
    tmp_sum_price = 0
    for i in range(start_index, end_index):
        # 양수 돌파 매수
        if(df['MACD_12_26_9'][i-1] < 0 and df['MACD_12_26_9'][i] > 0):
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_sum_price = tmp_sum_price + df['Open'][i]
        # 음수 돌파 매도
        elif(df['MACD_12_26_9'][i-1] > 0 and df['MACD_12_26_9'][i] < 0):
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_sum_price=0
    result = get_result(wallet, df, cnt)
    return result

# rsi 평단가 판매 알고리즘
def rsi_sell_by_avg_price(df, wallet, start_index, end_index):
    print("rsi 알고리즘, 판매가중치")
    result = []
    cnt = 0
    tmp_sum_price = 0
    for i in range(start_index, end_index):
        # 40이상이면 사기
        if(df['RSI_14'][i] <40):
            # print("사!", df['Open'][i])
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_sum_price = tmp_sum_price + df['Open'][i]
        # 60 이상이면 팔기
        elif(cnt >= 1 and (df['Open'][i] >= (get_avg_price(tmp_sum_price, cnt)*1.1) )):
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_sum_price=0
    result = get_result(wallet, df, cnt)
    return result

# 스토캐스틱 알고리즘 평단가 판매가중치
def stochastic_sell_by_avg_price(df, wallet, start_index, end_index):
    print("스토캐스틱 알고리즘, 판매가중치")
    result = []
    cnt = 0
    tmp_sum_price = 0
    for i in range(start_index, end_index):
        # 20이상이면 사기
        if(df['STOCHk_14_3_3'][i] <=20):
            wallet = wallet - df['Open'][i]
            cnt=cnt+1
            tmp_sum_price = tmp_sum_price + df['Open'][i]

        # 평단가 기준으로 팔기
        elif(cnt >= 1 and df['Open'][i] >= (get_avg_price(tmp_sum_price, cnt)*1.1)):
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_sum_price=0
    result = get_result(wallet, df, cnt)
    return result

# 라오어 알고리즘, 완전히 같지 않고 대략적으로 비슷함
def laor_algorithm(df, wallet, start_index, end_index):
    print("라오어 알고리즘 결과")
    result = []
    cnt = 0
    tmp_sum_price = 0
    for i in range(start_index, end_index):
        wallet = wallet - df['Open'][i]
        cnt=cnt+1
        tmp_sum_price = tmp_sum_price + df['Open'][i]

        if(cnt >= 1 and df['Open'][i] >= (get_avg_price(tmp_sum_price, cnt)*1.1)):
            # 가지고 있는 모든 개수 다팔기
            wallet = wallet + (df['Open'][i] * cnt)
            cnt=0
            tmp_sum_price=0
        result = get_result(wallet, df, cnt)

    return result

