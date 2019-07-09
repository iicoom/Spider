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
# url='https://www.zhipin.com/i100020-c101030100/e_108/?ka=sel-city-101030100' 天津
# url='https://www.zhipin.com/i100020-c101190100/e_108/?ka=sel-exp-108'  南京
# url='https://www.zhipin.com/i100020-c101210100/e_108/?ka=sel-city-101210100' 杭州
# url='https://www.zhipin.com/i100020-c101200100/e_108/?ka=sel-city-101200100' 武汉
# url='https://www.zhipin.com/i100020-c101230200/e_108/?ka=sel-city-101230200' 厦门
# url='https://www.zhipin.com/i100020-c101040100/e_108/?ka=sel-exp-108' 重庆
# url='https://www.zhipin.com/i100020-c101070100/e_108/?ka=sel-exp-108' 沈阳
# url='https://www.zhipin.com/i100020-c101060100/e_108/?ka=sel-exp-108' 长春
# url='https://www.zhipin.com/i100020-c101180100/e_108/?ka=sel-exp-108' 郑州
# url='https://www.zhipin.com/i100020-c101110100/e_108/?ka=sel-exp-108' 西安
# url='https://www.zhipin.com/i100020-c101120100/e_108/?ka=sel-exp-108' 济南
# url='https://www.zhipin.com/i100020-c101190400/e_108/?ka=sel-exp-108' 苏州
# url='https://www.zhipin.com/i100020-c101270100/e_108/?ka=sel-exp-108' 成都
# url='https://www.zhipin.com/i100020-c101120200/e_108/?ka=sel-exp-108' 青岛
# url='https://www.zhipin.com/i100020-c101070200/e_108/?ka=sel-exp-108' 大连
# url='https://www.zhipin.com/i100020-c101250100/e_108/?ka=sel-city-101250100' 长沙


########## 在线教育 i100012-c101010100 ############################################################
# url='https://www.zhipin.com/i100012-c101010100/e_108/?page=2&ka=page-2' 北京
# url='https://www.zhipin.com/i100012-c101020100/e_108/?page=1&ka=page-1' 上海
# url='https://www.zhipin.com/i100012-c101280600/e_108/?ka=sel-city-101280600' 深圳
# url='https://www.zhipin.com/i100012-c101030100/e_108/?ka=sel-city-101030100' 天津
# url='https://www.zhipin.com/i100012-c101190100/e_108/?ka=sel-exp-108' 南京
# url='https://www.zhipin.com/i100012-c101210100/e_108/?ka=sel-city-101210100' 杭州
# url='https://www.zhipin.com/i100012-c101200100/e_108/?ka=sel-city-101200100' 武汉
# url='https://www.zhipin.com/i100012-c101200100/e_108/?ka=sel-city-101230200' 厦门
# url='https://www.zhipin.com/i100012-c101040100/e_108/?ka=sel-exp-108' 重庆
# url='https://www.zhipin.com/i100012-c101070100/e_108/?ka=sel-exp-108' 沈阳
# url='https://www.zhipin.com/i100012-c101180100/e_108/?ka=sel-exp-108' 郑州
# url='https://www.zhipin.com/i100012-c101110100/e_108/?ka=sel-exp-108' 西安
# url='https://www.zhipin.com/i100012-c101120100/e_108/?ka=sel-exp-108' 济南
# url='https://www.zhipin.com/i100012-c101190400/e_108/?ka=sel-city-101190400' 苏州
# url='https://www.zhipin.com/i100012-c101270100/e_108/?ka=sel-city-101270100' 成都
# url='https://www.zhipin.com/i100012-c101120200/e_108/?ka=sel-exp-108' 青岛
# url='https://www.zhipin.com/i100012-c101070200/e_108/?ka=sel-exp-108' 大连
# url='https://www.zhipin.com/i100012-c101250100/e_108/?ka=sel-city-101250100'


########## 互联网金融 ############################################################
# url='https://www.zhipin.com/i100206-c101010100/e_108/?page=1&ka=page-1' 北京
# url='https://www.zhipin.com/i100206-c101020100/e_108/?page=1&ka=page-1'  上海
# url='https://www.zhipin.com/i100206-c101280600/e_108/?ka=sel-city-101280600' 深圳
# url='https://www.zhipin.com/i100206-c101210100/e_108/?ka=sel-city-101210100' 杭州
# url='https://www.zhipin.com/i100206-c101030100/e_108/?ka=sel-city-101030100' 天津
# url='https://www.zhipin.com/i100206-c101270100/e_108/?ka=sel-city-101270100'
# url='https://www.zhipin.com/i100206-c101040100/e_108/?ka=sel-exp-108' 重庆
# url='https://www.zhipin.com/i100206-c101180100/e_108/?ka=sel-exp-108' 郑州
# url='https://www.zhipin.com/i100206-c101110100/e_108/?ka=sel-exp-108' 西安
# url='https://www.zhipin.com/i100206-c101120100/e_108/?ka=sel-exp-108' 济南
# url='https://www.zhipin.com/i100206-c101190400/e_108/?ka=sel-exp-108' 苏州
# url='https://www.zhipin.com/i100206-c101270100/e_108/?ka=sel-city-101270100' 成都
# url='https://www.zhipin.com/i100206-c101070200/e_108/?ka=sel-exp-108' 大连


########## 媒体 ############################################################
# url='https://www.zhipin.com/i100003-c101010100/e_108/?ka=sel-exp-108'
# url='https://www.zhipin.com/i100003-c101020100/e_108/?ka=sel-city-101020100'
# url='https://www.zhipin.com/i100003-c101280100/e_108/?ka=sel-city-101280100'
# url='https://www.zhipin.com/i100003-c101270100/e_108/?ka=sel-city-101270100'
# url='https://www.zhipin.com/i100003-c101030100/e_108/?ka=sel-exp-108' 天津
# url='https://www.zhipin.com/i100003-c101180100/e_108/?ka=sel-exp-108' 郑州
# url='https://www.zhipin.com/i100003-c101110100/e_108/?ka=sel-exp-108' 西安
# url='https://www.zhipin.com/i100003-c101270100/e_108/?ka=sel-city-101270100' 成都
# url='https://www.zhipin.com/i100003-c101070200/e_108/?ka=sel-exp-108' 大连

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