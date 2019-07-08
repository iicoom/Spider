import requests
from bs4 import BeautifulSoup

import peewee as pw

myDB = pw.MySQLDatabase(host='47.94.91.128', port=33306, user='mysql', passwd='123456', database='maot')

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

Job.create(source=1, jobid='12345', title='Java', salay= '12')

data_source = [
    { 'source': 1, 'jobid': '12345', 'title': 'java', 'salay': '123' },
    { 'source': 1, 'jobid': '12345', 'title': 'java', 'salay': '123' },
    { 'source': 1, 'jobid': '12345', 'title': 'java', 'salay': '123' },
    { 'source': 2, 'jobid': '12345', 'title': 'java', 'salay': '123' },
]

# Job.insert_many(data_source).execute()

url='https://www.zhipin.com/job_detail/?query=&city=101010100&industry=100020&position='
headers={
  'user-agent':'Mozilla/5.0'
}

html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')

# print(soup.prettify())

targets = soup.find_all('div', 'job-primary')
# print(targets)
shuchu = []

for item in targets:

      # title = item.find('div', 'job-title').string
      # salay = item.find('span', 'red').string
      # company_name = item.select('h3 .name a').string

      shuchu.append({ 'title': item.find('div', 'job-title').string })  # 职位名

print(shuchu)

Job.insert_many(shuchu).execute()