districts_list = {}
with open('norway_municipalities_2017.csv', 'r', encoding='utf-8') as municipalities_file:
    header = municipalities_file.readline().strip().split(',')
    for line in municipalities_file:
        _, district, population = line.split(',')
        districts_list[district] = districts_list.get(district, 0) + int(population)
print(f'{header[1]:20s}{header[2]:>s}')
print(30 * '-')
for district, population in sorted(districts_list.items(), key=lambda s: s[1], reverse=True):
    print(f'{district:20s}{population:10d}')

# right click on a variable, refactor and rename to change the name and apply that to all instances

