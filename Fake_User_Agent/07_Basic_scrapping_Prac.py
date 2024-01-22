# 07_Basic_scrapping_Prac.py

# Daum Stock Info

import json
import urllib.request as req

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

# Request Code
# def Request(url, data=None, headers={},..
# headers={} 에서 dict 을 대입하여 User-agent, Referer 모두 브라우저의 header 값과 동일하게 한다.
# url 은 ajax 로 받는 Stock Info 요청 url 을 입력
res = req.urlopen(req.Request(url, headers=headers)).read().decode("UTF-8")

# Requested Data Check (Json Data)
print("res :", res)

# Requested Data String -> Json Trans and Data Print

rank_json = json.loads(res)["data"]

# Mid Check
print("Mid Check : ", rank_json, "\n")


class RankJson:
    for elm in rank_json:
        # print('순위 : {}, 금액 : {}, 사명 : {}, 변동 양상 : {}'.format(elm['rank'], elm['tradePrice'], elm['name'], elm['change']))
        # # print('')

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
