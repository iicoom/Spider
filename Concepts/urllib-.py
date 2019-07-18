from urllib import request
from urllib import parse
# import urllib2

# with request.urlopen('https://book.douban.com/subject/34442090/?icn=index-latestbook-subject') as f:
#     data = f.read()
#     # print('Status:', f.status, f.reason)
#     # print(f.getheaders())
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))

url = 'https://pro.fnxy.net.cn/user/login'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/75.0.3770.100 Safari/537.36 '
values = {'username': 'mao', 'password': '123456'}
headers = {'User-Agent': user_agent, 'Referer': 'http://www.zhihu.com/articles'}
data = parse.urlencode(values).encode(encoding='UTF8')
res = request.urlopen(url, data, headers)  # 参数格式错误
print(res)

# ImportError: cannot import name 'request' from 'urllib' (/Users/guitar/Repo/Spider/Tools/urllib-.py)
# 文件名不能为模块名
