list_a = [3, 7, 12, 7]
list_b = [x for x in list_a if  x % 2 == 0]
list_c = {x for x in list_a if x % 2 != 0}
print(list_b, list_c)

list_a = [3, 7, 12, 7]
list_b = [3, 7, 12, 7]


def list_test(array):
    temp_list = []
    return [x for x in list_a if x % 2 == 0]
print(list_test(list_a))
#     return [x for x in list_b if x % 2 != 0]
# print(list_test(list_b))

triples = {3, 7, 12}
new_dict = {}

for i in triples:
    if i % 3 == 0:
        new_dict[i] = 'True'
    else:
        new_dict[i] = 'False'

print(new_dict)

triples2 = {9, 1, 2, 5, 9, 33}
dict_triples = {}

for n in triples2:
    if n % 3 == 0:
        dict_triples[n] = 'True'
    else:
        dict_triples[n] = 'False'
print(dict_triples)

triples = {3, 7, 12}
new_dict = {}
new_dict = {x: True if x % 3 == 0 else False for x in triples}
print(new_dict)

triples2 = {9, 1, 2, 5, 9, 33}
new_dict2 = {}
new_dict2 = {i: True if i % 3 ==0 else False for i in triples2}
print(new_dict2)
triples = [3, 7, 12]
triples2 = [9, 1, 2, 5, 9, 33]


def triples_1(array):
    return {i: True if i % 3 == 0 else False for i in array}


print(triples_1(triples))
print(triples_1(triples2))
