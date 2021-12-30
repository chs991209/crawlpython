# 5th pyfile - urlopen method

# 05_urlopen_etc.py

# Get 타입 Data Contact

import urllib.request
from urllib.parse import urlparse

# Basic Request_01 (Encar)

url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

# urlopen 으로 대입한 여러 info
print("type : {}".format(type(mem)))
print("geturl : {}".format(mem.geturl()))
print("status : {}".format(mem.status))
print("headers : {}".format(mem.getheaders()))
print("getcode : {}".format(mem.getcode()))
print("read : {}".format(mem.read(100).decode("utf-8")))
print("parse : {}".format(urlparse("http://www.encar.co.kr?test=test")))
# test Parameter 에 test 대입 >> urlparse().query 에서 test param 의 대입값 불러오기
# http://url?~ ~ 값을 .query 요청 값으로 가져옴
print("parse : {}".format(urlparse("http://www.encar.co.kr?test=test").query))


# Basic Request_02 (ipfy)

API = "https://api.ipify.org"

# Get 방식 Parameter
values = {"format": "json"}
# jsonp >>calback({..}), text, ..
print("before param : {}".format(values))
params = urllib.parse.urlencode(values)
print("after param : {}".format(params))

# Generating Requesting URL
URL = API + "?" + params
print("Requested URL is {}".format(URL))

# Reading URL data
data = urllib.request.urlopen(URL).read()

# Decoding URL data

text = data.decode("UTF-8")
print("response : {}".format(text))
