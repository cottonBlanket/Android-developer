import matplotlib.pyplot as plt
import matplotlib as mpl
from Django_analyst.analyst import MultiprocessorHandler


class Graph:
    def __init__(self, dictionary_to_graph, sub_label, name):
        self.sub_label = sub_label
        self.data = dictionary_to_graph
        self.name = name

    def get_vertical_graph(self):
        fig = plt.figure()
        plt.rcParams.update({'font.size': 8})
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#669900", "#669900", "0.7"])
        ax = fig.add_subplot()
        ax.tick_params(axis="both", labelsize=8)
        ax.grid(True, axis="y")
        x_axis = range(len(self.data.keys()))
        ax.bar(x_axis, list(self.data.values()), width=0.4, label=self.sub_label)
        #ax.set_facecolor((1.0, 0.47, 0.42))
        ax.set_xticks(x_axis, list(self.data.keys()), rotation="vertical")
        ax.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f'{self.name}.png')

    def get_horizontal_graph(self):
        fig = plt.figure()
        plt.rcParams.update({'font.size': 8})
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#669900", "#669900", "0.7"])
        ax = fig.add_subplot()
        ax.tick_params(axis="both", labelsize=8)
        ax.grid(True, axis="x")
        ax.barh(list(self.data.keys()), list(self.data.values()), label=self.sub_label, align="center")
        ax.invert_yaxis()
        plt.tight_layout()
        plt.savefig(f'{self.name}.png')

    def add_pie_sublot(self):
        fig = plt.figure()
        plt.rcParams.update({'font.size': 8})
        ax = fig.add_subplot()
        ax.tick_params(axis="both", labelsize=8)
        keys = list(self.data.keys())
        values = list(self.data.values())
        ax.pie(values, labels=keys)
        plt.tight_layout()
        plt.savefig(f'{self.name}.png')


data = MultiprocessorHandler().result_data
# data.salary_by_years[2005] = (data.salary_by_years[2004] + data.salary_by_years[2006]) / 2
Graph(data.salary_by_years, "Средняя З/П android-разработчика", "android_salaries").get_vertical_graph()
Graph(data.count_by_years, "Количество вакансий android-разработчика", "android_count").get_vertical_graph()
Graph(data.salary_by_cities, "Уровень З/П android-разработчика", "city_android_salaries").get_horizontal_graph()
Graph(data.count_by_cities, "ффф", "city_android_count").add_pie_sublot()

