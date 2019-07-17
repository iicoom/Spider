import requests
from bs4 import BeautifulSoup
import peewee as pw
import time

myDB = pw.MySQLDatabase(host='45.77.oo8.XXX', port=3306, user='root', passwd='123000o.', database='spider')


class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = myDB


# 和数据库表名称相对应
class QiuShi(MySQLModel):
    id = pw.AutoField
    username = pw.CharField()
    age = pw.IntegerField()
    sex = pw.CharField()
    praise_num = pw.IntegerField()
    comment_num = pw.IntegerField()
    content = pw.CharField()
    avatar = pw.CharField()


myDB.connect()

headers = {
    'user-agent': 'Mozilla/5.0'
}

for i in range(1, 11):

    url = 'http://www.qiushibaike.com/hot/page/' + str(i)
    print('Start crawling page:', url)
    try:
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        # print('soup', soup)
        targets = soup.find_all('div', 'article')
        # print(targets)
        print(len(targets))
        data_source = []
        for item in targets:
            avatar = 'https:' + item.find('div', 'author').img['src']
            username = item.find('div', 'author').img['alt']
            # print(item.find('div', 'author').find('div', 'articleGender')['class'])
            # print(item.find('div', 'author').find('div', 'articleGender') is None)
            gender_tag = item.find('div', 'author').find('div', 'articleGender')
            if gender_tag is None:
                sex = 'None'
                age = 0
            elif gender_tag['class'][1] == 'womenIcon':
                sex = 'woman'
                age = gender_tag.string
            else:
                sex = 'man'
                age = gender_tag.string

            praise_num = 0 if item.find('span', 'stats-vote').i is None else item.find('span', 'stats-vote').i.string
            comment_num = 0 if item.find('span', 'stats-comments').i is None else item.find('span',
                                                                                            'stats-comments').i.string
            content = item.find('div', 'content').span.get_text().lstrip().rstrip()
            print
            data_source.append(
                {'avatar': avatar, 'username': username, 'age': age, 'sex': sex, 'praise_num': praise_num,
                 'comment_num': comment_num, 'content': content})

        print('data_source:', data_source)
        # 插入数据库
        QiuShi.insert_many(data_source).execute()

    except requests.exceptions.ConnectionError:
        print('ConnectionError -- please wait 3 seconds')

    time.sleep(1)


# 出现的问题
# peewee.ProgrammingError: (1146, "Table 'spider.qiu' doesn't exist") 需要和数据库表名相对应

# 'content': '多么痛的领悟，老婆刚拖好的地，我竟然忘了😣 😣😣
# pymysql.err.InternalError: (1366, "Incorrect string value:
# '\\xF0\\x9F\\x98\\xA3 \\xF0...' for column 'content' at row 24")

# 需要修改表的 CHARSET=utf8 => CHARSET=utf8mb4
# ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8 COMMENT='糗事百


# 面向对象设计模式
"""
class QSBK:

    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []  # 存放段子的变量，每一个元素是每一页的段子们
        self.enable = False  # 存放程序是否继续运行的变量

    # 传入某一页的索引获得页面代码
    def get_page(self, page_index):
        try:
            qiu_url = 'http://www.qiushibaike.com/hot/page/' + str(page_index)
            o_html = requests.get(qiu_url, headers=self.headers)
            o_soup = BeautifulSoup(o_html.text, 'html.parser')
            return o_soup
        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')

    # 获取页面item
    def get_page_item(self, page_index):
        o_soup = self.get_page(page_index)
        print(o_soup)
        # 进行页面元素的提取操作...
        return o_soup

    # 自动加载新页面
    def load_page(self):
        if self.enable:
            page_stories = self.get_page_item(self.pageIndex)
            if page_stories:
                self.stories.append(page_stories)
                self.pageIndex += 1

    # 开始方法
    def start(self):
        print(u"正在读取糗事百科,按回车查看新段子，Q退出")
        # 先加载一页内容
        self.load_page()


spider = QSBK()
spider.start()
"""
