import requests
import json
from fake_useragent import UserAgent
import time

ua = UserAgent()

# URL and headers from the original request
url = 'http://finance.daum.net/api/quotes/A060570?summary=false&changeStatistics=true'
headers = {
    'Referer': 'http://finance.daum.net/quotes/A194480',
    'User-Agent': ua.chrome,
}

# Make the request
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Mapping dictionary for translations
    translations = {
        'openingPrice': '개장 시간',
        'highPrice': '최고 가격',
        'lowPrice': '최저 가격',
        'tradePrice': '거래 가격',
        'prevClosingPrice': '전일 종가',
        'change': '변동',
        'changePrice': '변동 가격',
        'changeRate': '변동률',
        'name': '종목명',
        'date': '날짜',
        'tradeDate': '거래 날짜',
        'tradeTime': '거래 시간',
        'exchangeDate': '거래소 날짜',
        'exchangeCountry': '거래 국가',
        'securityGroup': '보안 그룹',
        'isIndex': '지수 여부',
        'accTradePrice': '누적 거래 가격',
        'accTradeVolume': '누적 거래 건수',
        'prevAccTradeVolume': '이전 누적 거래 건수',
        'prevAccTradeVolumeChangeRate': '이전 누적 거래 건수 변동률',
        'marketCap': '시가 총액',
        'marketCapRank': '시가 총액 순위',
        'high52wPrice': '52주 최고 가격',
        'high52wDate': '52주 최고 가격 날짜',
        'low52wPrice': '52주 최저 가격',
        'low52wDate': '52주 최저 가격 날짜',
        'basePrice': '기준 가격',
        'upperLimitPrice': '상한가',
        'lowerLimitPrice': '하한가',
        'foreignRatio': '외국인 소유 비율',
        'prevForeignRatio': '이전 외국인 소유 비율',
        'foreignOwnShares': '외국인 소유 주식 수',
        'parValue': '액면 가치',
        'eps': '주당 순이익',
        'dps': '주당 배당금',
        'per': '주가 수익 비율',
        'bps': '주당 순자산 가치',
        'pbr': '주가 순자산 비율',
        'sectorCode': '업종 코드',
        'sectorName': '업종 이름',
        'sectorChangeRate': '업종 변동률',
        'wicsSectorCode': 'WICS 업종 코드',
        'wicsSectorName': 'WICS 업종 이름',
        'wicsSectorChangeRate': 'WICS 업종 변동률',
    }

    relevant_data = {key: data[key] for key in data if key != 'market'}
    print('Dreamus Company Finance Crawling Starts\n', end='\r')
    time.sleep(0.5)

    for key, value in relevant_data.items():
        translated_key = translations.get(key, key)
        if translated_key == '주당 배당금':
            break
        if translated_key == '누적 거래 간격' or translated_key == '보안 그룹' or translated_key == '누적 거래 가격':
            continue

        print(f'{translated_key}: {value}')

    json_relevant_data = json.dumps(relevant_data, indent=2)

else:
    print(f'Error: {response.status_code}')
