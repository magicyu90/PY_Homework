# -*- coding:utf-8 *-*
import pandas as pd
path = './infos/chipotle.tsv'
chipo = pd.read_csv(path, sep='\t')

chipo.info()    # 数据集有多少个观察值
chipo.columns  # 打印全部列
chipo.index  # 索引情况
#print(chipo.item_name.value_counts().head(3))  # 被下单最多的商品
print(chipo.item_name.unique())  # 一共多少不重复商品
chipo.quantity.sum()  # 商品数量


def dollarizer(x): return float(x[1:-1])


chipo.item_price = chipo.item_price.apply(dollarizer)
#print(chipo.item_price.sum())  # 收入

# 每一单(order)对应的平均总价是多少？
order_grouped = chipo.groupby('order_id').sum()
#print(order_grouped.mean()['item_price'])


print(chipo.item_name.value_counts().count()) # 一共多少种不同商品