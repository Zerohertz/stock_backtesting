import yfinance as yf

start_date = '2019-01-14'
end_date = '2022-12-12'
interval_time = "1d"
company = "SQQQ"

# 불러오기
data = yf.download(tickers = company, interval=interval_time, start=start_date, end=end_date)

# 저장
data.to_csv("./data/{0}_{1}_{2}_{3}.csv".format(company, interval_time, start_date, end_date), mode = "w")