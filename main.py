file_in = open('first_tour.txt', 'r')
file_out = open('second_tour.txt', 'w')

k = int(file_in.readline()) # подсчет проходного балла в финал
data = []
all_list = list()
new_list = list()

for line in file_in:
    data.append([str(x) for x in line.split()])
# создание спика участников и подсчет их количества

for i in range(len(data)):
    all_list.append({'surname': data[i][0], 'name': data[i][1], 'score': data[i][2]})
# создание спиcка участников в словарях

for i in range(len(data)):
    if int(all_list[i].get('score')) > k:
        new_list.append(all_list[i])
# создание списка финалистов в словарях

new_list = sorted(new_list, key=lambda d: d['score'], reverse=True)
# сортировка финалистов

with open('second_tour.txt') as file:
    file_out.write(f"{len(new_list)}\n")
    for i in range(len(new_list)):
        file_out.write(f"{i+1}) {(new_list[i].get('name'))[0]}. {(new_list[i].get('surname'))} {(new_list[i].get('score'))}\n")
# занесение финалистов в файл

file_in.close()
file_out.close()