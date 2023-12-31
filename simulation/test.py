import pandas as pd
from backtesting import day_trade
from crawling import crawling, technical_analysis
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import common


wallet = 0
# 평단가
avg_price = 0

"""
전 종목, 모든 알고리즘 테스트
"""
def all_stocks_all_algorithm_test(surplus_cash, start_crawl_date, end_crawl_date, start_date, end_date):
    stocks = common.get_all_stocks()
    algorithms = common.get_all_algorithms()
    result_df = pd.DataFrame(columns = ['stock', 'just_stay', 'rsi', 'rsi_buy_weight_trade',  'rsi_sell_by_avg', 'mfi', 'stochastic', 'stochastic_sell_by_avg', 'laor'])

    for i in range(len(stocks)):
        df = common.load_ta_csv(stocks[i], start_crawl_date, end_crawl_date)
        start_index = common.get_index_by_date(df, start_date)
        end_index = common.get_index_by_date(df, end_date)
        result_df.loc[i] = [stocks[i],
                            day_trade.just_stay(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.rsi_trade(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.rsi_buy_weight_trade(df, wallet, surplus_cash, start_index, end_index, rsi_sell_loc=60, rsi_buy_loc=40)[0],
                            day_trade.rsi_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.mfi_trade(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.stochastic_trade(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.stochastic_sell_by_avg_price(df, wallet, surplus_cash, start_index, end_index)[0],
                            day_trade.laor_algorithm(df, wallet, surplus_cash, start_index, end_index)[0]
                            ]

    print(result_df)
    return result_df

"""
과거 전체 기간동안 주어진 기간 반복하여 테스트
"""
def repeat_period_test(test_case, start_crawl_date, end_crawl_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc):

    stocks = common.get_all_stocks()
    df = common.load_ta_csv(stocks[0], start_crawl_date, end_crawl_date)
    stocks.insert(0, "Date")
    result_df = pd.DataFrame(columns = stocks)

    for i in range(0, len(df['Open']), day_period):
        if(i>len(df['Open'])):
            break
        start_index = i
        end_index = i + day_period
        tmp = [df['Date'][start_index]]

        for j in range(1, len(stocks)):
            tmp_df = common.load_ta_csv(stocks[j], start_crawl_date, end_crawl_date)
            tmp.append(common.find_test_case(tmp_df, test_case, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc)[0])

        result_df.loc[i] = tmp
    print(result_df)

"""
과거 전체 기간동안 전체 알고리즘, 전체 종목에 대하여 기간별로 계산하며 승률 테스트
"""
def win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc, rsi_first_buy_loc=50):

    df = common.load_ta_csv(stock, start_crawl_date, end_crawl_date)
    profits = []
    total_profit = 0
    win_cnt = 0
    lose_cnt = 0
    tmp_win_sum = 0
    tmp_lose_sum = 0

    avg_profit_rate = 0
    max_profit_rate = 0
    min_profit_rate = 9999

    sum_profit_rate = 0
    profit_rate_cnt = 0

    capital_needs = 0

    start_index = common.get_index_by_date(df, start_date)
    end_index = common.get_index_by_date(df, end_date)

    for i in range(start_index, end_index):
        if(i>len(df['Open']) - day_period):
            break
        start_index = i
        end_index = i + day_period
        result = common.find_test_case(df, test_case, wallet, surplus_cash, start_index, end_index, rsi_sell_loc, rsi_buy_loc, rsi_first_buy_loc)

        tmp_profit = result[0]
        tmp_profit_rate = result[1]
        tmp_capital_needs = result[2]

        if(tmp_profit > 0):
            win_cnt += 1
            tmp_win_sum += tmp_profit
        else:
            lose_cnt+=1
            tmp_lose_sum += tmp_profit
        total_profit += tmp_profit
        profits.append(tmp_profit)

        sum_profit_rate += tmp_profit_rate
        profit_rate_cnt += 1

        if(tmp_profit_rate > max_profit_rate):
            max_profit_rate = tmp_profit_rate

        if(tmp_profit_rate < min_profit_rate):
            min_profit_rate = tmp_profit_rate

        if(tmp_capital_needs > capital_needs):
            capital_needs = tmp_capital_needs

    if(profit_rate_cnt!=0 and (win_cnt+lose_cnt)!=0):
        avg_profit_rate = round(sum_profit_rate / profit_rate_cnt, 2)
        win_rate = round(((win_cnt) / (win_cnt+lose_cnt) * 100), 2)
        avg_profit = total_profit // (win_cnt+lose_cnt)
    else:
        avg_profit_rate = 0
        win_rate = 0
        avg_profit = 0
    # print()
    # print("현황", profits)
    # print("승률", win_rate, "%")
    # print("평균 총 수익", avg_profit, "$")
    # print("평균 수익률", avg_profit_rate, "%")
    # if(win_cnt!=0 and lose_cnt!=0):
    #     print("평균 승리 수익", tmp_win_sum // win_cnt, "$")
    #     print("평균 패배 손실", tmp_lose_sum // lose_cnt, "$")
    # print("승수", win_cnt)
    # print("패수", lose_cnt)
    # print("총 투자 필요 금액", capital_needs)

    return [stock, test_case, win_rate, avg_profit, avg_profit_rate, max_profit_rate, min_profit_rate, capital_needs]


"""
과거 전체 기간동안 매일 계산하며 승률 테스트
"""
def win_rate_rank_test(start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc, rsi_first_buy_loc):

    # 주식과 알고리즘
    stocks = common.get_all_stocks()
    algorithms = common.get_all_algorithms()

    result_df = pd.DataFrame(columns = ['stock', 'test_case', 'win_rate', 'profit', 'avg_profit_rate', 'max_profit_rate', 'min_profit_rate', 'capital_needs'])

    index=0
    for i in range(len(stocks)):
        for j in range(len(algorithms)):

            stock = stocks[i]
            test_case = algorithms[j]
            tmp = win_rate_test(stock, test_case, start_crawl_date, end_crawl_date, start_date, end_date, day_period, surplus_cash, rsi_sell_loc, rsi_buy_loc, rsi_first_buy_loc)

            result_df.loc[index] = tmp
            index += 1

    result_df = result_df.sort_values(by = ['win_rate'], ascending=False)
    return result_df