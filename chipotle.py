# -*- coding:utf-8 *-*
import pandas as pd
path = './infos/chipotle.tsv'
chipo = pd.read_csv(path, sep='\t')

chipo.info()    # 数据集有多少个观察值
chipo.columns() 
