import requests
from bs4 import BeautifulSoup

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
      <a href="/gongsi/2e64a887a110ea9f1nRz.html" ka="search_list_company_1_custompage" target="_blank">
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
soup = BeautifulSoup(html_doc)

# print(soup.prettify())

# print(soup.find('div', 'job-title').string)
# print(soup.find('span', 'red').string)

# print(soup.select('h3.name > a')[0].get('data-jobid'))

print(soup.select('div.info-primary h3 > a')[0].attrs['href'])
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
##################################################
find( name , attrs , recursive , text , **kwargs )
##################################################




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


"""



