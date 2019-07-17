import requests
import json

# r = requests.get('http://cuiqingcai.com')
# print('type(r):', type(r))
# print('r.status_code:', r.status_code)
# print('r.encoding:', r.encoding)
# print('r.cookies:', r.cookies)
# print('r.headers:', r.headers)
# print(r.text)

# get
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print('r.url:', r.url)


# post
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print('r.text:\n', r.text)

'''
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "23",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.21.0"
  },
  "json": null,
  "origin": "218.240.249.26, 218.240.249.26",
  "url": "https://httpbin.org/post"
}
'''

# data json
# url = 'http://httpbin.org/post'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# print('r.text:', r.text)

'''
{
  "args": {},
  "data": "{\"some\": \"data\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "16",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.21.0"
  },
  "json": {
    "some": "data"
  },
  "origin": "218.240.249.26, 218.240.249.26",
  "url": "https://httpbin.org/post"
}
'''

# 配置代理
proxies = {
  # "http": "http://104.207.142.12:8070",
  "https": "https://104.207.142.12:8070",
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print('r.text:\n', r.text)

