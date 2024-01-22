# REST API: GET, POST, DELETE, PUT
import requests

session = requests.Session()

response = session.get('https://api.github.com/events')

response.raise_for_status()

# print(response.text)
print(response.json)

jar = requests.cookies.RequestsCookieJar()

jar.set('name', 'HifiMan', domain='httpbin.org', path='/cookies')

response = requests.get('https://httpbin.org/cookies', cookies=jar)

print(response.text)

response = session.get('https://github.com', timeout=2)

print(response.text)

# POST
response = session.post('https://httpbin.org/post', data={'id': 'test', 'pw': '1234'}, cookies=jar)

# print(response.text)
print(response.headers)

payload1 = {'id': 'test', 'pw': '1234'}


response = session.post('https://httpbin.org/post', data=payload1)
print(response.json())
response_put = session.put('https://httpbin.org/put', data=payload1)
print(response_put.json())
response_delete = session.delete('https://httpbin.org/delete', data=payload1)
print(response_delete.json())
session.close()
