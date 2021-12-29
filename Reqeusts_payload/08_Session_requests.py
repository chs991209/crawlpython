# 08_Session_requests.py
# requests 사용 Scrapping - Session

import requests

# # Activate Session
# s = requests.Session()
# r = s.get('https://www.naver.com')
#
# # Data
# # print(r.text)
#
# # Request Status Code
# print('STATUS CODE : {}'.format(r.status_code))
#
# # Check
# #
# # print('Ok? : {}'.format(r.ok))
# if r.ok:
#     print('HTTP Connection OK')
#
#
# # Deactivate Session
# # s.close()

s = requests.Session()

r1 = s.get('https://httpbin.org/cookies', cookies={'name': 'Kim1'})
print(r1.text)

# SET Cookies

r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'Kim2'})
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {
    'user-agent': 'iPad',

}

# Headers Info Transfer
# .get() method >> (self), url, kwargs
# url 은 request url, kwargs 는 headers 와 같은 key arguments
# 같은 경로의 request method 의 method arguments 를 'GET' 으로 반환해, GET request 를 보낸다.
# request 의 url, kwargs 는 get 에서 대입한 값을 가져간다.
r3 = s.get(url, headers=headers, cookies={'name': 'Kim2'})

print(r3.text)
s.close()


