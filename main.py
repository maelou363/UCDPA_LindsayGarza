import pandas as pd

# API - not necessary to need to have both though for this dataset.
# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()
# api.competitions_list(category='all')

#Import csv
data = pd.read_csv("StudentsPerformance.csv")

### Going through and inspecting the dataset ###
# print(data.columns)
# print(data.info())
# print(data.shape)
# print(data.describe())
# print(data.values)
# print(data.index)
# print(data[['parental-education', 'gender', 'race', 'math-score']])
# print(data.iloc[2])

# for index, row in data.iterrows():
#     print(index, row)

# print(data.loc[data['parental-education'] == 'high school'])
# print(data.describe())
# print(data.sort_values(['math-score', 'reading-score', 'writing-score'], ascending=False))

#### Creating new column called Avg-Scores to average out the scores in an attempt to see the correlation between test scores and social dynamics ###
data['Avg-Score'] = data['math-score'] + data['reading-score'] + data['writing-score'] / 3
print(data.head())



