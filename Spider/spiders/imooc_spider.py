import requests
import time
# from lxml import etree
from bs4 import BeautifulSoup
# import MySQLdb  # 只支持Python2版本
from multiprocessing.dummy import Pool as ThreadPool


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

urls = []

for i in range(200000, 200001):
    profile_url = 'http://www.imooc.com/u/' + str(i)
    urls.append(profile_url)


def getsource(url):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    print('selector:', soup)

    user_id = int(url.replace('http://www.imooc.com/u/', ''))
    user_name = soup.find('h3', 'user-name clearfix').span.string
    print('username', user_name)

    # try:
    #     conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset='utf8')
    #     cur = conn.cursor()
    #     conn.select_db('python')
    #     cur.execute('INSERT INTO imooc_user VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    #                 [user_id, user_name, user_sex, user_place, user_job, user_head, user_word,
    #                  user_time, user_score, user_exp, user_learn_number, user_time_number])
    # except MySQLdb.Error as e:
    #     print(e)
    #     "Mysql Error %d: %s" % (e.args[0], e.args[1])


pool = ThreadPool(8)  # 创建线程池，线程数为8

try:
    results = pool.map(getsource, urls)
except Exception as e:
    print(e)
    time.sleep(300)
    results = pool.map(getsource, urls)

pool.close()
pool.join()

