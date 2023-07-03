import pandas as pd
import requests
import json

import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

# 查询小学电话接口
Telurl = "https://restapi.amap.com/v3/place/text?key=2c4e23c45c0c6f18f66f6470a0be5470&keywords="

# 查询北京区域中小学接口
request = "https://www.eol.cn/html/zhongxue/bjzxx/index.shtml#1"

# # urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
# # url="http://www.eol.cn/html/zhongxue/bjzxx/index.shtml#1"
tables = pd.read_html(request)
print(f'Total tables: {len(tables)}')
# print(tables)
# print('tables[1] is', tables[1])

df = pd.DataFrame(tables[23], columns=['学校名称', '学校地址', '联系电话'])
print('添加电话前：', df)


for idx, row in df.iterrows():
    df.loc[idx, '联系电话'] = 'abc'

print('添加abc后：', df)

for idx,row in df.iterrows():
    requestUrl = Telurl + row[0]
    response = requests.get(requestUrl)
    response_json = response.json()
    pois = response_json["pois"]
    if pois and pois[0]["tel"]:
        tel = response_json["pois"][0]["tel"]
    else:
        tel = []
    print('tel is:', tel)
    df.loc[idx, '联系电话'] = str(tel)
print('添加电话后：', df)

df.to_csv("./海淀区完全中学.csv", index=True)
