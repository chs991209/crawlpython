import json
import requests
import time


def print_type(var):
    print(type(var))


session = requests.Session()

# docker run -p 80:80 kennethreitz/httpbin
response = session.get(
    'http://localhost:80/stream/3', stream=True
)  # docker server by localhost

# print(response.text)

print('Default Encoding : {}'.format(response.encoding), end='\r')
time.sleep(0.5)

if response.encoding is None:
    response.encoding = 'utf-8'

# print('After Encoding : {}'.format(response.encoding))

# response_dict = [
#     json.loads(line.lower())
#     for line in response.iter_lines(decode_unicode=True)
#     if json.loads(line.lower())['headers']['connection'] == 'keep-alive'
#     # if json.loads(line.lower())['connection'] == 'keep-alive'
# ]
# print(response_dict)
# print_type(response_dict)
# print(response.headers)
# response_headers = []


for line in response.iter_lines():
    lower_line = json.loads(line.lower())

    # print(dir(line))
    # print(json.loads(lower_line))
    for k, v in lower_line.items():
        print('Key: {0}, Value: {1}'.format(k, v))

session.close()

# response = session.get('https://jsonplaceholder.typeicode.com/todos/1')
response = session.post('https://httpbin.org/post')

# if response.status_code == 200:
#     try:
#         # Attempt to parse the JSON data
#         data = response.json()
#
#         # Iterate over the JSON data
#         for k, v in data.items():
#             print('Key: {0}, Value: {1}'.format(k, v))
#
#     except json.decoder.JSONDecodeError as e:
#         # Handle the JSON decoding error
#         print('Error decoding JSON:', e)
# else:
#     # Print an error message for non-OK status codes
#     print('Request failed with status code:', response.status_code)


# print(response.headers['Content-Type'])
print()
print('Response Header Is : {}'.format(response.headers))
print('Response Text Is : {}'.format(response.text, '\n'))
print('Response Binary Content Is : {}'.format(response.content, '\n'))
print(response.json())

# print('Response String Data is: {}'.format(response.text))
# print('Response String Data length is: {}'.format(len(response.text)))
# print('Response Json is: {}'.format(response.json().keys()))

# print('Response Json is: {}'.format(response.json()))
