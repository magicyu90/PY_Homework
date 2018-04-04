# -*- coding:utf-8 *-*
import pandas as pd
path = './infos/drinks.csv'
drinks = pd.read_csv(path)

# 哪个大陆(continent)平均消耗的啤酒(beer)更多？
avg_drinks = drinks.groupby('continent').beer_servings.mean()
print(avg_drinks)
# 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
print(drinks.groupby('continent').spirit_servings.agg(['mean', 'max', 'min']))
