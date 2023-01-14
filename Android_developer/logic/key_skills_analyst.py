import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

df = pd.read_csv('android_correct.csv')
df_skills = df['skills']
df['published'] = df['published'].apply(lambda x: int(str(x)[:4]))
years = df['published'].unique()
all_skills = {}
for year in years:
    all_skills[year] = []

for index, row in df.iterrows():
    skills = str(row['skills']).split('\n')
    year = int(str(row['published'])[:4])
    if skills[0] != 'nan':
        all_skills[year].extend(skills)

year_frequency = dict()
for year in all_skills.keys():
    year_frequency[year] = dict()

for year in all_skills.keys():
    for skill in all_skills[year]:
        try:
            skill = str(skill).replace('\r', '')
            year_frequency[year][skill] += 1
        except:
            year_frequency[year][skill] = 1

# noinspection PyTypeChecker
for year in year_frequency.keys():
    year_frequency[year] = dict(sorted(year_frequency[year].items(), key=lambda x: x[1], reverse=True))
    year_frequency[year] = list(year_frequency[year].keys())[:10]
# print('Год, Наиболее высокочастотные навыки')
# for year in year_frequency.keys():
#     if len(year_frequency[year]) > 0:
#         print(f'{year}, {year_frequency[year]}')

fig = plt.figure()
plt.rcParams.update({'font.size': 8})
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#669900", "#669900", "0.7"])
ax = fig.add_subplot()
ax.tick_params(axis="both", labelsize=8)
ax.grid(True, axis="x")
ax.barh(list(year_frequency.keys()), list(year_frequency.values()), label="Популярные навыки в IT-вакансиях", align="center")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(f'android_skills.png')




