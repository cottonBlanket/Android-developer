import csv

file_name = input("Введите название файла: ")

names_list = list()
print("Вводите построчно варианты названия профессии. Если вы перечислили все варианты, то введите пустую строку.")
while(True):
    name = input(f"{len(names_list) + 1} вариант: ")
    if name == "":
        print(f"Вы ввели {len(names_list)} вариантов.")
        break

    names_list.append(name)
print('\nНачинаю обработку. Пожалуйста, подождите...\n')
with open(file_name, "r", encoding="utf-8-sig") as data:
    reader = csv.reader(data)
    fields = next(reader)
    data = [row for row in reader if len(row) == len(fields)]

name_index = fields.index('name')
profession_data = []
for row in data:
    vacancy_name = row[name_index]
    for version in names_list:
        if version in vacancy_name:
            profession_data.append(row)
print('Обработка завершена.')
new_file_name = input("Введите название нового файла: ").strip().split('.')[0]
with open(f"{new_file_name}.csv", "a", encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(profession_data)

print(f"Файл сохранен с именем {new_file_name}.csv")



