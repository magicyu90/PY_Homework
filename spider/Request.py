import requests
r   = requests.get('http://www.baidu.com')

print(r.status_code)

print(r.headers)

print(r.text)