### 프로젝트
미국 주식 데이터를 활용하여 다양한 통계적 지표를 백테스팅할 수 있는 프로젝트

#### 과정
1. yfinance 라이브러리를 활용하여 종목코드의 주가 데이터를 csv로 수집 (interval 1min, 5min, 1day etc)
2. pandas 데이터 프레임으로 csv 파일 불러와서 최적의 알고리즘을 찾기 위해 다양한 통계적 지표 (RSI, stochastic etc) 테스트
3. 전체 과정 자동화

#### 종목코드
- dow jones : DIA, DDM, UDOW
- QQQ : QQQ, QLD, TQQQ
- inverse QQQ : PSQ , , SQQQ
- S&P500 : IVV, SSO, UPRO
- ARKK

#### 폴더 구조 설명
- backtesting 트레이딩 방식 구현 폴더
- crawling 미국 주가 데이터 수집 폴더
- data 수집 원본 데이터
- ta_data 기술적 지표 추가한 데이터
- commmon 공통으로 사용하는 것들 파일
- main 실행하는 파일

#### 데이터 크롤링 라이브러리
- [yfinance python guide](https://analyzingalpha.com/yfinance-python)
- yfinance에만 1분 단위 데이터를 가져올 수 있어서 yfinance 사용
- [investpy](https://github.com/alvarobartt/investpy)
- [financedatareader](https://github.com/financedata-org/FinanceDataReader)

#### 통계적 분석 pandas 라이브러리
- [pandas-ta](https://github.com/twopirllc/pandas-ta)

#### 해외주식 장시세
- 최고의 장
2020년 3월 25일 ~ 2021년 12월 29일
QQQ 기준 약 215불 수익

- 최악의 장
2022년 1월 4일 ~ 2022년 12월 23일