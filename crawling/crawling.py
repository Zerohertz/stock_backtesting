import yfinance as yf

stocks = ["QQQ", "QLD", "TQQQ", "PSQ", "SQQQ", "DIA", "DDM", "UDOW", "ARKK", "IVV", "SSO", "UPRO", "FNGU", "BULZ"]

# start_date = '2012-01-03'
# end_date = '2022-12-22'
interval_time = "1d"
company = "UDOW"

# 불러오기
data = yf.download(tickers = company, interval=interval_time, history="max")

# 저장
data.to_csv("./data/{0}_{1}_max.csv".format(company, interval_time), mode = "w")
