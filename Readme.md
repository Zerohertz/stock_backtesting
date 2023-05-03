### 프로젝트
미국 주식 데이터를 활용하여 다양한 통계적 지표를 백테스팅할 수 있는 프로젝트

### 과정
1. yfinance 라이브러리를 활용하여 종목코드의 주가 데이터를 csv로 수집 (interval 1min, 5min, 1day etc)
2. pandas 데이터 프레임으로 csv 파일 불러와서 최적의 알고리즘(RSI, stochastic etc)을 찾기 위해 다양한 통계적 지표 테스트
3. 전체 과정 자동화

### 참고자료
- yfinance에만 1분 단위 데이터를 가져올 수 있어 yfinance 사용

#### 종목코드
- dow jones : DIA, DDM, UDOW
- QQQ : QQQ, QLD, TQQQ
- inverse QQQ : PSQ , , SQQQ
- S&P500 : IVV, SSO, UPRO
- ARKK
