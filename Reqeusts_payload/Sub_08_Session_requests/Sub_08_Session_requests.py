import requests

# With 사용 권장 -> File, DB, HTTP

with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    if r.ok:
        print('HTTP OK')

