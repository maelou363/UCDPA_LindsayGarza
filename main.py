import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# API - not necessary to need to have both though for this dataset.
# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()
# api.competitions_list(category='all')

# Import csv
data = pd.read_csv("StudentsPerformance.csv")

# Going through and inspecting the dataset ###
# print(data.columns)
# print(data.info())
# print(data.shape)
# print(data.describe())
# print(data.values)
# print(data.index)
# print(data[['parental-education', 'gender', 'race', 'math-score']])
# print(data.iloc[2])

# Iterrating into each individual dataset
# for index, row in data.iterrows():
#     print(index, row)


# loc to find only high school education from parents
# print(data.loc[data['parental-education'] == 'high school'])
# print(data.describe())
# print(data.sort_values(['math-score', 'reading-score', 'writing-score'], ascending=False))

# Creating new column called Avg-Scores to average out the scores in an attempt to see the correlation
# between test scores and social dynamics #
data['Avg-Score'] = (data['math-score'] + data['reading-score'] + data['writing-score'])/3
# print(data.head(5))

# Dropping columns that does not pertain for this research
data_new = data.drop(columns=['gender', 'race', 'lunch', 'preparation-course', 'math-score', 'reading-score', 'writing-score'])
(data_new.sort_values(['parental-education', 'Avg-Score'], ascending=False))


fig, ax = plt.subplots(figsize=(10, 20))
ax.scatter(x = data_new['parental-education'], y = data_new['Avg-Score'])
plt.xlabel('Parental Education')
plt.ylabel('Childs Avg Score')
plt.title("Childs Avg Scores with Parents of Different Educational Backgrounds")
plt.show()






