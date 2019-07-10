import time
import requests
from bs4 import BeautifulSoup

"""
1. Boss直聘 招聘信息爬取
"""
html_doc = """
<html>
 <head>
 </head>
 <body>
  <div class="job-primary">
   <div class="info-primary">
    <h3 class="name">
     <a class="" data-index="0" data-itemid="1" data-jid="ff96300c2dfee2a31XNz3t26F1I~" data-jobid="27950770" data-lid="1ArTXQVCETc.search" href="/job_detail/ff96300c2dfee2a31XNz3t26F1I~.html" ka="search_list_1" target="_blank">
      <div class="job-title">
       后台开发实习生
      </div>
      <span class="red">
       200-220/天
      </span>
     </a>
     <div class="info-detail" style="top: 0px;">
      <a>
       <div class="info-detail-top">
        <div class="detail-top-title">
         Python
        </div>
        <div class="detail-top-text">
         腾讯 · 招聘者： 过正
        </div>
        <div class="detail-top-right">
         <a class="link-like" data-url="/geek/tag/jobtagupdate.json?jobId=ff96300c2dfee2a31XNz3t26F1I~&amp;expectId=&amp;tag=4&amp;lid=1ArTXQVCETc.search" href="javascript:;" job-id="a3e42020b745dcdc1XJz0tS9FlI~" ka="popjob_interest_tosign_ff96300c2dfee2a31XNz3t26F1I~">
          感兴趣
         </a>
         <a class="btn btn-startchat" data-url="/wapi/zpgeek/friend/add.json?jobId=ff96300c2dfee2a31XNz3t26F1I~&amp;lid=1ArTXQVCETc.search" href="javascript:;" ka="popjob_greet_tosign_ff96300c2dfee2a31XNz3t26F1I~" redirect-url="/geek/new/index/chat?id=a3e42020b745dcdc1XJz0tS9FlI~" target="_blank">
          立即沟通
         </a>
        </div>
       </div>
      </a>
      <div class="detail-bottom">
       <div class="detail-bottom-title">
        职位描述
       </div>
       <div class="detail-bottom-text">
        2020年及以后毕业
        <br/>
        后台开发实习生（1名）【岗位职责】 1.参与腾讯新闻客户端数据运营体系开发工作； 2.参与腾讯新闻用户运营分析数据挖掘工作； 3.负责相关创新数据产品（平台）的开发和优化； 4.参与新业务核心功能开发。 【岗位要求】 1.熟悉PHP开发，同时熟悉python/java/shell等语言优先； 2.熟练使用 Mysql、Redis等数据库，有相应的项目开发经验优先； 3.熟悉linux操作系统，了解常用的算法，数据结构； 4.有较强的自我驱动能力，执行力强，对自己有高技术要求。 5.每周工作4-5天，实习至少6个月；
       </div>
      </div>
     </div>
    </h3>
    <p>
     北京 海淀区 知春路
     <em class="vline">
     </em>
     4天/周
     <em class="vline">
     </em>
     5个月
     <em class="vline">
     </em>
     本科
    </p>
   </div>
   <div class="info-company">
    <div class="company-text">
     <h3 class="name">
      <a href="/company/2e64a887a110ea9f1nRz.html" ka="search_list_company_1_custompage" target="_blank">
       腾讯
      </a>
     </h3>
     <p>
      互联网
      <em class="vline">
      </em>
      已上市
      <em class="vline">
      </em>
      10000人以上
     </p>
    </div>
   </div>
   <div class="info-publis">
    <h3 class="name">
     <img src="https://img.bosszhipin.com/beijin/mcs/useravatar/20170904/8809013a8eb68d943584180da41e7deb85a703152df778e80fd8ca58d725caef_s.jpg?x-oss-process=image/resize,w_40,limit_0"/>
     过先生
     <em class="vline">
     </em>
     招聘者
    </h3>
    <p>
    </p>
   </div>
   <a class="btn btn-startchat" data-url="/wapi/zpgeek/friend/add.json?jobId=ff96300c2dfee2a31XNz3t26F1I~&amp;lid=1ArTXQVCETc.search" href="javascript:;" redirect-url="/geek/new/index/chat?id=a3e42020b745dcdc1XJz0tS9FlI~">
    立即沟通
   </a>
  </div>
 </body>
</html>
"""

# soup = BeautifulSoup(html.text, 'html.parser')
# soup = BeautifulSoup(html_doc)

# print(soup.prettify())

# print(soup.find('div', 'job-title').string)
# print(soup.find('span', 'red').string)

# print(soup.select('h3.name > a')[0].get('data-jobid'))

# print(soup.select('div.info-primary h3 > a')[0].attrs['href'])
# for child in soup.select('div.info-primary p')[0].children:
#     print(child)

# print(soup.select('div.info-primary p')[0].contents)
# print(soup.select('div.info-primary p')[0].contents[2])
# print("soup.select('div.info-company h3 > a')[0].contents:", soup.select('div.info-primary p')[0].contents)
# print(len(soup.select('div.info-primary p')[0].contents))

# print(soup.select('div.info-primary p')[0].get_text())
# print(soup.select('div.info-primary p')[0].split('<em class="vline"></em>'))
# print(soup.select('div.info-company h3 > a')[0].get_text())


"""
2. 豆瓣电影
"""
# html = requests.get('https://movie.douban.com/top250?start=0')
# print('html:', html)
# html: <Response [200]>

# print('html.text:', html.text)
# 打印出html页面

# soup = BeautifulSoup(html.text, 'html.parser')
# print('soup:', soup)
# print('soup.prettify():', soup.prettify())
# 格式化后的HTML

# target = soup.find_all('div', 'info')
# print('target:', target)
# [<div class="info"></div>,..] 一个list

"""
<div class="info"> 
   <div class="hd"> 
    <a class="" href="https://movie.douban.com/subject/1292052/"> <span class="title">肖申克的救赎</span> <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span> <span class="other">&nbsp;/&nbsp;月黑高飞(港) / 刺激1995(台)</span> </a> 
    <span class="playable">[可播放]</span> 
   </div> 
   <div class="bd"> 
    <p class=""> 导演: 弗兰克&middot;德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆&middot;罗宾斯 Tim Robbins /...<br /> 1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情 </p> 
    <div class="star"> 
     <span class="rating5-t"></span> 
     <span class="rating_num" property="v:average">9.6</span> 
     <span content="10.0" property="v:best"></span> 
     <span>1479131人评价</span> 
    </div> 
    <p class="quote"> <span class="inq">希望让人自由。</span> </p> 
   </div> 
  </div>
"""
# 循环list
# for item in target:
#     title = item.div.a.span.string
#     year = item.find('div', 'bd').p.contents[2].string
#     year = year.replace(' ', '')  # 去掉这一行的空格
#     year = year.replace('\n', '')  # 去掉这一行的回车换行
#     year = year[0:4]  # 只取年份前四个字符
#     # print('year:\n', year)
#     print(title, '\t', year)

"""
肖申克的救赎 	 1994
霸王别姬 	 1993
这个杀手不太冷 	 1994
阿甘正传 	 1994
美丽人生 	 1997
泰坦尼克号 	 1997
千与千寻 	 2001
...
"""

"""
3. 招聘网站
"""
# Python默认发送的请求和浏览器发送的请求是有不同的。最主要的不同就是浏览器发送的请求除了http地址之外还包含了看不到的header头信息。

# 添加请求头
url = 'https://www.zhipin.com/c101190400/h_101190400/?query=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&page='
headers = {
    'user-agent': 'Mozilla/5.0'
}

page = 1
hud = ['职位名', '薪资范围', '地点', '经验', '学历', '公司名称', '公司行业', '融资阶段', '公司人数', '发布人']
print('\t\t'.join(hud))

for n in range(1, 3):
    # print('request-url:', url + str(page))
    html = requests.get(url + str(page), headers=headers)
    page += 1
    soup = BeautifulSoup(html.text, 'html.parser')
    # print('html:', html.text)
    target_list = soup.find_all('div', 'job-primary')
    # print('target_list:', target_list)
    for item in target_list:
        outPut = []
        outPut.append(item.find('div', 'job-title').string[0:5])

        salary = item.find('span', 'red').string
        outPut.append(salary)

        position = item.find('p').contents
        outPut.append('\t' + position[0].string if len(position) > 0 else 'None')  # 地点
        outPut.append(position[2].string if len(position) > 2 else 'None')         # 经验
        outPut.append('\t' + position[4].string if len(position) > 4 else 'None')  # 学历

        outPut.append('\t' + item.find('div', 'company-text').h3.a.get_text())  # 公司名称
        company = item.find('div', 'info-company').find('p').contents
        outPut.append('\t' + company[0].string if len(company) > 0 else 'None')  # 公司行业
        outPut.append('\t' + company[2].string if len(company) > 2 else 'None')  # 融资阶段
        outPut.append('\t\t' + company[4].string if len(company) > 4 else 'None')  # 公司人数

        outPut.append('\t' + item.find('div', 'info-publis').find('h3').contents[1].string)  # 发布人

        print('\t'.join(outPut))
        # break
    time.sleep(1)

"""
Beautiful Soup 4.0 常用方法

搜索文档树：
##################################################
find_all( name , attrs , recursive , text , **kwargs )
##################################################


##################################################
find( name , attrs , recursive , text , **kwargs )
##################################################

下面两行代码是等价的：
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>


##################################################
CSS选择器
##################################################




##################################################
标签文本获取 get_text()
##################################################

print(soup.select('div.info-primary p')[0].get_text('', strip=True).split(' '))

contents 与 children 提取

##################################################
提取标签属性值
##################################################

print(soup.select('div.info-primary h3 > a')[0].attrs['href'])


##################################################
子节点
##################################################
一个Tag可能包含多个字符串或其它的Tag,这些都是这个Tag的子节点.Beautiful Soup提供了许多操作和遍历子节点的属性.

.contents
tag的 .contents 属性可以将tag的子节点以列表的方式输出:

tag:
<p class="">
    导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
    1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
</p>

tag.contents 对提取包含文字和标签的元素很有用
['\n    导演: 弗兰克·德拉邦特 Frank Darabont\xa0\xa0\xa0主演: 蒂姆·罗宾斯 Tim Robbins /...', <br/>, '\n     1994\xa0/\xa0美国\xa0/\xa0犯罪 剧情\n ']


"""
