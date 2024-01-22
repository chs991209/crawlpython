# 07_Basic_scrapping_Prac.py

# Daum Stock Info

import json
import requests
from fake_useragent import UserAgent

# Fake Headers Info
ua = UserAgent()
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# Headers Info


headers = {
    "User-agent": ua.ie,
    "Referer": "https://finance.daum.net/",
}

# Daum Stock Info requesting url
url = "https://finance.daum.net/api/search/ranks?limit=10"


response = requests.get(url, headers=headers)

if response.status_code == 200:
    res = response.text

    # Requested Data Check (Json Data)
    print("res:", res)

    # Requested Data String -> Json Trans and Data Print
    rank_json = json.loads(res)["data"]

    # Mid Check
    print("Mid Check:", rank_json, "\n")

    for elm in rank_json:
        name = elm["name"]
        rank = elm["rank"]
        tradePrice = elm["tradePrice"]
        change = elm["change"]

        print(
            "순위 : {}, 금액 : {}, 사명 : {}, 변동 양상 : {}".format(
                rank, name, tradePrice, change
            )
        )
        print("")

    print(type(elm))
else:
    print("Failed to retrieve data. Status code:", response.status_code)