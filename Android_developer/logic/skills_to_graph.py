import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

df = pd.read_csv('vacancies_correct.csv')
df_skills = df['skills']
df['published'] = df['published'].apply(lambda x: int(str(x)[:4]))
years = df['published'].unique()
all_skills = []
for year in years:
    all_skills = []

for index, row in df.iterrows():
    skills = str(row['skills']).split('\n')
    year = int(str(row['published'])[:4])
    if skills[0] != 'nan':
        all_skills.extend(skills)

frequency = dict()

for skill in all_skills:
    try:
        skill = str(skill).replace('\r', '')
        frequency[skill] += 1
    except:
        frequency[skill] = 1

# noinspection PyTypeChecker
frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
# noinspection PyTypeChecker
frequency = dict(list(frequency.items())[:10])

fig = plt.figure()
plt.rcParams.update({'font.size': 8})
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#669900", "#669900", "0.7"])
ax = fig.add_subplot()
ax.tick_params(axis="both", labelsize=8)
ax.grid(True, axis="x")
ax.barh(list(frequency.keys()), list(frequency.values()), label="Популярные навыки в IT-вакансиях", align="center")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(f'all_skills.png')




