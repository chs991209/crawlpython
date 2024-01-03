import json
import requests
import time


def print_type(var):
    print(type(var))


session = requests.Session()

# docker run -p 80:80 kennethreitz/httpbin
response = session.get(
    "http://localhost:80/stream/100", stream=True
)  # docker server by localhost


print(response.text)

print("Default Encoding : {}".format(response.encoding), end="\r")
time.sleep(1)


if response.encoding is None:
    response.encoding = "utf-8"


print("After Encoding : {}".format(response.encoding))

response_dict = [
    json.loads(line.lower())
    for line in response.iter_lines(decode_unicode=True)
    if json.loads(line.lower())["headers"]["connection"] == "keep-alive"
    # if json.loads(line.lower())['connection'] == 'keep-alive'
]
print(response_dict)
print_type(response_dict)
print(response.headers)
response_headers = []


# for line in response.iter_lines():
#     lower_lines = line.lower()
#     # print(dir(line))
#     print(json.loads(lower_lines))
#     print_type(json.loads(line))
