path = 'C:\\Users\\julia\\Logs\\'

lines = open(path + 'logs.txt').readlines()
number_of_occure = {x: 0 for x in set(lines)}
for x in lines:

    if x in number_of_occure:
        number_of_occure[x] += 1
duplicates = [x for x in number_of_occure.keys() if number_of_occure[x] > 1]
print(len(duplicates))

for x in duplicates:
    with open(r'C:\Users\julia\Logs\results\duplicates.txt', 'a') as a:
        a.write(x)

print(duplicates)



strings = open(path +'logs2.txt').readlines()
number_of_occure2 = {x: 0 for x in set(strings)}
for x in strings:
    if x in number_of_occure2:
        number_of_occure2[x] += 1
duplicates2 = [x for x in number_of_occure2.keys() if number_of_occure2[x] > 1]
print(len(duplicates2))

for x in duplicates2:
    with open(r'C:\Users\julia\Logs\results\duplicates2.txt', 'a') as a:
        a.write(x)

print(duplicates2)