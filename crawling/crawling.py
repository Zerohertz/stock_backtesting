import yfinance as yf

stocks = ["QQQ", "QLD", "TQQQ", "PSQ", "SQQQ", "DIA", "DDM", "UDOW", "ARKK", "IVV", "SSO", "UPRO", "FNGU", "BULZ"]

start_date = '2012-01-03'
end_date = '2023-05-04'
interval_time = "1d"
company = "UPRO"

# 불러오기
data = yf.download(tickers = company, interval=interval_time, start=start_date, end=end_date)

# 저장
data.to_csv("./data/{0}_{1}_{2}_{3}.csv".format(company, interval_time,start_date, end_date), mode = "w")