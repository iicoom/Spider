import json
import os


def range2two(s, unit):
    s = s.replace(unit, '')
    s = s.replace(' ', '')
    range_arr = s.split('-')
    res = {
        'low': str(range_arr[0]),
        'high': str(range_arr[1]) if len(range_arr) > 1 else 'None'
    }
    # print(res)
    return res


def read_job(file_path):
    with open(file_path, 'r') as f:
        job = json.load(f)
        print(json.dumps(job, indent=2, ensure_ascii=False))


# read_job('../../Files/3442660.json')
range2two("15k-30k", "k")  # {'low': '15', 'high': '30'}

labels = ['positionId', 'positionName', 'workYear', 'education', 'createTime', 'salary', 'city', 'companyFullName',
          'companySize', 'financeStage', 'firstType', 'secondType', 'details']

labels2 = ['salary_low', 'salary_high', 'workYear_low', 'workYear_high', 'companySize_low', 'companySize_high']


def read_get(file_path):
    with open(file_path, 'r') as f:
        job = json.load(f)
        line = []
        for key in labels:
            line.append(str(job[key]).replace(',', '，'))

        salaries = range2two(job['salary'], 'k')
        work_years = range2two(job['workYear'], '年')
        company_sizes = range2two(job['companySize'], '人')
        line += [salaries['low'], salaries['high']]
        line += [work_years['low'], work_years['high']]
        line += [company_sizes['low'], company_sizes['high']]

        # return line
        return ','.join(line)


# test = read_get('../../Files/3442660.json')
# print(test)

# 读取并保存一个职位到csv文件

# with open('../../Files/jobs.csv', 'w', encoding='gb18030') as f:
#     text = ''
#     text += ','.join(labels + labels2)
#
#     text += '\n'
#     text += read_get('../../Files/source/3442660.json')
#     f.write(text)
#     f.close()
#     print('>>OK!')


# 读取全部职位存储到jobs.csv


files = os.listdir('../../Files/source/')
with open('../../Files/jobs.csv', 'w', encoding="gb18030") as f:
    text = ''
    text += ','.join(labels + labels2)

    for name in files:
        if name.find('.json') > -1:
            text += '\n'
            text += read_get('../../Files/source/' + name)

    f.write(text)
    f.close()
    print('>>OK!')

