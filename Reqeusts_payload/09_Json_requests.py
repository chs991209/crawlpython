import json

import requests

s = requests.Session()

# Request 100 Data
# stream=True 일 때, large text 를 직렬화 해서 불러온다
r = s.get("https://httpbin.org/stream/100", stream=True)

# Check if Received
print(r.text)

# Check Encoding
print("Encoding : {}".format(r.encoding))

# Encoding=None 일 때
if r.encoding is None:
    r.encoding = "UTF-8"

print("After Encoding : {}".format(r.encoding))


for line in r.iter_lines(decode_unicode=True):
    #     Print line and Check Type
    # print(line)
    # print(type(line))

    #     Json (Dict) Trans and Check Type
    b = json.loads(line)
    print(b)
    # print(type(b))

"""
b = [
    {"url": 1001},
    {
        "headers": {
            "User-agent": "MAC OS X",
            "Host": "httpbin.org",
            "User-agent": "MAC OS X",
            "origin": "218.51.205.133",
        }
    },
]


for k in b:
    query_string = urllib.parse.urlencode(k, doseq=True)
    print(str(query_string))
"""


"""
author = b['url']
uploading_env = self.dict['headers']['User-agent']
file_name = self.dict['headers']['origin']



class API:
    def __init__(self, dict):
        self.dict = b

    def APIreceive_(self, author, uploading_env, file_name):
        return author, uploading_env, file_name


class Board:
    # board_info

    board_info.APIreceive_(author=None, uploading_env=None, file_name=None)

board_info = {
    'author': b['url'],
    'uploading_env': b['headers']['User-agent'],
    'file_name': b['headers']['origin'],
              }
"""
