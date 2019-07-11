"""
页面可以不直接包含数据，而是通过运行JavaScript代码，从服务器重新获取数据，再填充到页面上。

任何向服务器发起的请求都可以在Network面板找到信息，带了哪些参数params（Form Data)，带了什么样的headers，等等

json数据和字典对象用起来一样，从Request获取的文本text数据需要用json.load转换一下，
然后就可以用shuju['aa']['bb']的方法一层层找到我们需要的信息
"""

import json
import requests
import time

url = 'https://www.lagou.com/gongsi/searchPosition.json'

# 添加params和headers
# params就是Form Data

params = {
    'companyId': '16831',
    'positionFirstType': '全部',
    'schoolJob': 'false',
    'pageNo': '1',
    'pageSize': '10',
}
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=ABAAABAAAGFABEFBD9ED2DDDE780C0ED72E4A86093CF489; '
              'user_trace_token=20190708155642-3825b617-9eba-42dc-8bb3-f76bb313be5c; _ga=GA1.2.2086999768.1562572607; '
              'LGUID=20190708155649-f0a57847-a155-11e9-a4da-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; '
              '_gid=GA1.2.777210901.1562820430; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562572609,1562820430; '
              '_gat=1; LGSID=20190711135336-3951302c-a3a0-11e9-a4de-5254005c3644; PRE_UTM=; PRE_HOST=; '
              'PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2Fj94.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; '
              'TG-TRACK-CODE=index_checkmore; SEARCH_ID=ea9983005c0d4a5fa838db61315a0cd7; '
              'X_HTTP_TOKEN=59903d183b1da6c72854282651b1b490c52dd048bc; '
              'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562824604; '
              'LGRID=20190711135644-a94c1b50-a3a0-11e9-be-525400f775ce',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/gongsi/j16831.html',
    'X-Anit-Forge-Code': '5660122',
    'X-Anit-Forge-Token': '1a501558-6358-4383-ba16-7fcf0cpb331'
}

jsonData = requests.get(url, params=params, headers=headers)

data = json.loads(jsonData.text)

# print(json.dumps(data, indent=2, ensure_ascii=False))  # 格式化json

"""
jobs=data['content']['data']['page']['result']
for job in jobs:
    print(job['positionName'])
"""

hud = ['职位', '薪酬', '学历', '经验']
print('\t'.join(hud))

for i in range(1, 2):
    params['pageNo'] = i
    jsonData = requests.get(url, params=params, headers=headers)
    data = json.loads(jsonData.text)
    jobs = data['content']['data']['page']['result']
    for job in jobs:
        jobarr = []
        jobarr.append(job['positionName'])
        jobarr.append(job['salary'])
        jobarr.append(job['education'])
        jobarr.append(job['workYear'])
        print('\t'.join(jobarr))
    time.sleep(1)



