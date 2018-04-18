# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd

path = './infos/crime_rate.csv'

crime = pd.read_csv(path)
crime.Year = pd.to_datetime(crime.Year, format='%Y')  # 将Year的数据类型装换为datetime64
crime = crime.set_index('Year', drop=True)

crimes = crime.resample('10AS').sum()
population = crimes['Population'].resample('10AS').max()
crimes['Population'] = population
print(crime.idxmax(0))
