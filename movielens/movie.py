# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
movies_data = pd.read_csv('movies.csv')
ratings_data = pd.read_csv('ratings.csv')
data = pd.merge(movies_data, ratings_data)
data.drop('timestamp', 1, inplace=True)
print(data)
# 评价最多的20部电影
top20comment = data.title.value_counts()[:20]
# print(top20comment)


movie_ratings = data.groupby('title').agg({'rating': [np.size, np.mean]})


# 评分最高的TOP5

print(movie_ratings[movie_ratings[('rating', 'size')] > 150].sort_values([('rating', 'mean')], ascending=False).head(10))
