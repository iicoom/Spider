# import jieba
import json
import jieba.analyse
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


# fc = jieba.cut('我爱你，我爱学习')
# print('/'.join(fc))


# AttributeError: module 'jieba' has no attribute 'cut'
# 原因是和当前文件名冲突，重命名文件

# 统计单个招聘信息的词频
def read_job_detail(path):
    with open(path, 'r') as f:
        job = json.load(f)
        details = job['details'].lower()
        # print('job-details:\n', details)
        details = details.replace(' ', '').replace('\xa0', '')
        return details


text = read_job_detail('../../Files/source/3442660.json')
# print('text:\n', text)
fc = jieba.cut(text)
print('/'.join(fc))

# 关键词提取 jieba提供了简单有效的分析提取工具analyse
'''
jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())，其中topK是列出最重要的20个

jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
'''

# for word, weight in jieba.analyse.extract_tags(text, withWeight=True):
#     print('%s %s' % (word, weight))

print('-' * 20)

# for word, weight in jieba.analyse.textrank(text, withWeight=True):
#     print('%s %s' % (word, weight))

keywords = []
weights = []
targets = ['药物', '算法', '量子化学', '晶型', '动力学', '分子', '研发部门', '研发', 'ai', '经验', '设计', '开发', '晶体结构', '模拟']

for word, weight in jieba.analyse.extract_tags(text, topK=100, withWeight=True):
    if word in targets:
        keywords.append(word)
        weights.append(weight)
print(keywords, weights)

# plotly.offline.init_notebook_mode(connected=False)

# plotly.offline.iplot({
#     "data": [go.Scatter(x=keywords, y=weights)],
#     "layout": go.Layout(title="拉勾网人工智能职业关键词分布")
# })

# data = [go.Scatter(x=keywords, y=weights)]  # 折线图
data = [go.Bar(x=keywords, y=weights)]  # 柱状图
# py.plot({
#     'data': [keywords, weights],
#     'layout': go.layout(title="拉勾网人工智能职业关键词分布")
# })


py.plot(data, filename='拉勾网人工智能职业关键词分布', auto_open=True)
