import pandas as pd

apple_list = [['ipad', 1, 2], ['airpot', 3, 4]]
apple_pd = pd.DataFrame(apple_list)
print(apple_pd)
print(type(apple_pd))

apple_pd = pd.DataFrame(apple_list, columns=['name', 'pro', 'air'], index=['a', 'b'])
print(apple_pd)
print(apple_pd.columns)
print(apple_pd.index)
print(apple_pd.dtypes)