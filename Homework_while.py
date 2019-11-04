# def vowels(string):
#  vowels = ['a', 'e', 'i', 'o', 'u']
#  # string ='hApPyHalLOweEn!'
#  numVowels = 0
#  i = 0
#
#  while i < len(string):
#
#   if (string[i].lower() in vowels):
#    numVowels += 1
#
#   i += 1
#
#  return numVowels
#
# assert vowels("apPyHalLoween!") == 5
# assert vowels("hApPyHalLOweEn!") == 5
# assert vowels("hpPHlLwn!") == 0
# assert vowels("") == 0
#
# # Задание 2: уникальный набор. УСЛОВИЕ: Реализовать код, который принимает список елементов и убирает из него все дубликаты
# # (формирует список уникальных элементов). Сделать вариант с сохранением порядка следования элементов и вариант,
# # в кот. сортировка элементов не принципиальна.
#
# # б) assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]
#
# ist1=["a", 5, 2, 5, (1, "a"), "a"]
#
# list_set = set(list1)
# unique_list = list(list_set)
#
# print(unique_list)

# Пример: а) assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")]

def unique_ordered(unique_list):
    unique_ordered = []
    i = 0

    while i < len(unique_list):
        if unique_list[i] not in unique_ordered:
            unique_ordered.append(unique_list[i])
        i += 1

    return unique_ordered


print(unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]))


