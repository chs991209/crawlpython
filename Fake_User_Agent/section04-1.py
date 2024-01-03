# section04-1.py

# Daum Stock Info
import requests
import json
import urllib.request as req

from fake_useragent import UserAgent

# Fake Headers Info
ua = UserAgent()
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

import time


def log_response_body(response_body):
    formatted_json = json.dumps(json.loads(response_body), indent=2)
    print('\nResponse body:', formatted_json, '\n')


def log_response_data_by_key(response_body, key_to_extract=None):
    json_data = json.loads(response_body)

    if key_to_extract:
        extracted_data = json_data.get(key_to_extract)
        if extracted_data:
            print(f"\nExtracted '{key_to_extract}': {extracted_data}\n")
        else:
            print(f"\n'{key_to_extract}' not found in the JSON data\n")
    else:
        formatted_json = json.dumps(json_data, indent=2)
        print('\nResponse body:', formatted_json, '\n')


# Headers Info


headers = {
    'User-agent': ua.chrome,
    'Referer': 'https://finance.daum.net/',
}

# Daum Stock Info requesting url
url = 'https://finance.daum.net/api/search/ranks?limit=10'

# Request Code
# def Request(url, data=None, headers={},..
# headers={} 에서 dict 을 대입하여 User-agent, Referer 모두 브라우저의 header 값과 동일하게 한다.
# url 은 ajax 로 받는 Stock Info 요청 url 을 입력
# res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')
res = requests.get(url, headers=headers).text

# Requested Data Check (Json Data)
log_response_body(res)
# Requested Data String -> Json Trans and Data Print

# Mid Check
print('The response body.data is :', end='\r')
time.sleep(1.5)
log_response_data_by_key(res, key_to_extract='data')


rank_json = json.loads(res)['data']


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def int_to_roman_lower(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num.lower()


class RankJson:
    index = 1
    for elm in rank_json:
        name = elm['name']
        rank = elm['rank']
        tradePrice = elm['tradePrice']
        change = elm['change']
        roman_index = int_to_roman_lower(index)

        print('{}: 순위 : {}, 금액 : {}, 사명 : {}, 변동 양상 : {}'.format(roman_index, rank, name, tradePrice, change))
        index += 1

        print('')
    print(f'{len(rank_json)} data received\n')

    print(type(elm))
