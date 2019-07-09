import requests
from bs4 import BeautifulSoup

import peewee as pw

myDB = pw.MySQLDatabase(host='47.94.91.128', port=33306, user='mysql', passwd='123456', database='psych')
# myDB = pw.MySQLDatabase(host='47.94.91.128', port=33306, user='mysql', passwd='123456', database='maot')

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class Job(MySQLModel):
    id = pw.AutoField
    source = pw.IntegerField()
    jobid = pw.CharField()
    title = pw.CharField()
    salay = pw.CharField()
    addtime = pw.DateField()
    endtime = pw.DateField()
    fulltime = pw.CharField()
    education = pw.CharField()
    company_name = pw.CharField()
    category = pw.CharField()
    url = pw.CharField()
    area = pw.CharField()


myDB.connect()

# Job.create(source=1, jobid='12345', title='Java', salay= '12')

# data_source = [
#     { 'source': 1, 'jobid': '12345', 'title': 'java', 'salay': '123' },
#     { 'source': 1, 'jobid': '12345', 'title': 'java', 'salay': '123' },
#     { 'source': 1, 'jobid': '12345', 'title': 'java', 'salay': '123' },
#     { 'source': 2, 'jobid': '12345', 'title': 'java', 'salay': '123' },
# ]

# Job.insert_many(data_source).execute()

########## 互联网 ############################################################
# url='https://www.zhipin.com/i100020-c101010100/e_108/?page=2&ka=page-2' 北京
# url='https://www.zhipin.com/i100020-c101020100/e_108/?page=2&ka=page-2' 上海
# url='https://www.zhipin.com/i100020-c101280600/e_108/?page=2&ka=page-2' 深圳

########## 在线教育 ############################################################
# url='https://www.zhipin.com/i100012-c101010100/e_108/?page=2&ka=page-2' 北京
# url='https://www.zhipin.com/i100012-c101020100/e_108/?page=1&ka=page-1' 上海
# url='https://www.zhipin.com/i100012-c101280600/e_108/?ka=sel-city-101280600' 深圳

########## 互联网金融 ############################################################
# url='https://www.zhipin.com/i100206-c101010100/e_108/?page=1&ka=page-1' 北京
# url='https://www.zhipin.com/i100206-c101020100/e_108/?page=1&ka=page-1'  上海
# url='https://www.zhipin.com/i100206-c101280600/e_108/?ka=sel-city-101280600' 深圳

########## 媒体 ############################################################
# url='https://www.zhipin.com/i100003-c101010100/e_108/?ka=sel-exp-108'
# url='https://www.zhipin.com/i100003-c101020100/e_108/?ka=sel-city-101020100'
# url='https://www.zhipin.com/i100003-c101280100/e_108/?ka=sel-city-101280100'

url=''

headers={
  'user-agent':'Mozilla/5.0'
}

html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')

# print(soup.prettify())

targets = soup.find_all('div', 'job-primary')
# print(targets)
data_source = []

# 详情页url前缀
prefix = 'https://www.zhipin.com'

for item in targets:

      jobid = item.select('h3.name > a')[0].get('data-jobid')
      title = item.find('div', 'job-title').string
      salay = item.find('span', 'red').string
      print("item.select('div.info-primary p')[0].contents:", item.select('div.info-primary p')[0].contents)
      area = item.select('div.info-primary p')[0].contents[0][0:2]
      company_name = item.select('div.info-company h3 > a')[0].get_text()
      category = item.select('div.info-company p')[0].contents[0]
      url = prefix+item.select('div.info-primary h3 > a')[0].attrs['href']

      if len(item.select('div.info-primary p')[0].contents) < 6:
          fulltime = ''
          education = ''
      else:
          fulltime = item.select('div.info-primary p')[0].contents[2]
          education = item.select('div.info-primary p')[0].contents[6]

      data_source.append(
          {'source': 3, 'jobid': jobid, 'title': title, 'salay': salay, 'fulltime': fulltime, 'education': education
              , 'company_name': company_name, 'area': area, 'category': category, 'url': url})

print('data_source:', data_source)

Job.insert_many(data_source).execute()