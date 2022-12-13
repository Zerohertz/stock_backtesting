import yfinance as yf

start_date = '2022-12-05'
end_date = '2022-12-12'
interval_time = "1m"
company = "TQQQ"

#다운로드
data = yf.download(tickers = company, interval=interval_time, start=start_date, end=end_date)

# 저장
data.to_csv("./data/{0}_{1}_{2}.csv".format(company, start_date, end_date), mode = "w")