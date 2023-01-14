import math

import pandas as pd


class Data:
    def __init__(self):
        self.salary_by_years = dict()
        self.count_by_years = dict()
        # self.profession_salary = dict()
        # self.profession_count = dict()
        self.salary_by_cities = dict()
        self.count_by_cities = dict()

    def sorted_dicts(self):
        self.salary_by_years = dict(sorted(self.salary_by_years.items(), key=lambda x: x[0], reverse=False))
        self.count_by_years = dict(sorted(self.count_by_years.items(), key=lambda x: x[0], reverse=False))
        # self.profession_salary = dict(sorted(self.profession_salary.items(), key=lambda x: x[0], reverse=False))
        # self.profession_count = dict(sorted(self.profession_count.items(), key=lambda x: x[0], reverse=False))
        self.salary_by_cities = dict(sorted(self.salary_by_cities.items(), key=lambda x: x[1], reverse=True))
        self.count_by_cities = dict(sorted(self.count_by_cities.items(), key=lambda x: x[1], reverse=True))


class MultiprocessorHandler:
    def __init__(self):
        self.file_name = 'android_correct.csv'
        self.result_data = Data()
        self.df = pd.read_csv(self.file_name)
        self.df['published'] = self.df['published'].apply(lambda x: int(x[:4]))
        self.years = self.df['published'].unique()
        self.create_processes()
        self.csv_city_parser()
        self.result_data.sorted_dicts()

    def print_result(self):
        print('Динамика уровня зарплат по годам:', self.result_data.salary_by_years)
        print('Динамика количества вакансий по годам:', self.result_data.count_by_years)
        # print('Динамика уровня зарплат по годам для выбранной профессии:', self.result_data.profession_salary)
        # print('Динамика количества вакансий по годам для выбранной профессии:', self.result_data.profession_count)
        print('Уровень зарплат по городам (в порядке убывания):', self.result_data.salary_by_cities)
        print('Доля вакансий по городам (в порядке убывания):', self.result_data.count_by_cities)

    def create_processes(self):
        result_data = dict()
        for year in self.years:
            self.csv_year_parser(year, result_data)
        self.fill_data(result_data)

    def fill_data(self, data: dict):
        for year, value in data.items():
            self.result_data.salary_by_years[year] = value[0]
            self.result_data.count_by_years[year] = value[1]
            # self.result_data.profession_salary[year] = value[2]
            # self.result_data.profession_count[year] = value[3]

    def csv_year_parser(self, year: str, data: dict):
        this_df = self.df[self.df['published'] == year]
        # df_vacancy = this_df[this_df["name"].str.contains(self.profession)]
        # if df_vacancy.empty:
        data[year] = [this_df['salary'].mean(), len(this_df.index)]
        # else:
        #     data[year] = [this_df['salary'].mean(), len(this_df.index),
        #                   math.floor(df_vacancy['salary'].mean()), len(df_vacancy.index)]

    def csv_city_parser(self):
        total = len(self.df)
        self.df['count'] = self.df.groupby('city')['city'].transform('count')
        df_norm = self.df[self.df['count'] > 0.01 * total]
        df_area = df_norm.groupby('city', as_index=False)['salary'].mean().sort_values(by='salary', ascending=False)
        df_count = df_norm.groupby('city', as_index=False)['count'].mean().sort_values(by='count', ascending=False)
        cities = df_count['city'].unique()
        self.result_data.salary_by_cities = {city: 0 for city in cities}
        self.result_data.count_by_cities = {city: 0 for city in cities}
        for city in cities:
            self.result_data.salary_by_cities[city] = int(df_area[df_area['city'] == city]['salary'])
            self.result_data.count_by_cities[city] = round(int(df_count[df_count['city'] == city]['count']) / total, 4)


if __name__ == "__main__":
    MultiprocessorHandler().print_result()
