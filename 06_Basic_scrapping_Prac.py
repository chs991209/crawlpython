# 06_Basic_scrapping_Prac.py

# METHOD - GET data communication - RSS

import urllib.parse
import urllib.request

# 행정 안전부 홈페이지
# RSS API URL

API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

params = []

# for num in [[1001, 1005], 1012, 1013, 1014]:
for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# print(params)


# Request in a row
for c in params:
    # print(c)
    # urlencode -> dict or tuple 을 string(또는 bytes) 형의 query 문자열 ( key=value, ..) 로 변환
    #
    # string >> 한 가지 key 에 대한 value 값이 두 개 이상일 때, doseq = True 일 때 string 자료형으로 여러 개의 param 으로 바꿈
    # doseq = False 이면 bytes 형태로 바꿈
    param = urllib.parse.urlencode(c)

    url = API + "?" + param

    print('Url is : ' + url)
    print('')

#     Request
#     urlopen 은 여러 request 정보를 각 값의 종류에 맞게 params 에 대입해 줌
#     (url, data, timeout)
    res_data = urllib.request.urlopen(url).read()
    # Decode 이전에 읽은 data
    # print(res_data)

    contents = res_data.decode("UTF-8")

    print("-" * 50)
    print("-" * 50)
    print("-" * 50)
    print("-" * 50)
    print(contents)


# c = {'home':'Seoul'}
#
# for a, b in c.items():
#     print(a, b)

# shoppping_cart = ['salary', 'cucumber', 'apples']
# child_wish_list = {'breakfast': 'spaghetti'}
# shoppping_cart.append(child_wish_list)
# print(shoppping_cart)