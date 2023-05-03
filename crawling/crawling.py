import yfinance as yf

def crawl_stock_data(start_date, end_date, company, interval_time="1d"):

    # 불러오기
    data = yf.download(tickers = company, interval=interval_time, start=start_date, end=end_date)

    # 저장
    data.to_csv("./data/{0}_{1}_{2}_{3}.csv".format(company, interval_time,start_date, end_date), mode = "w")