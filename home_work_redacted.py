#1. Преобразовать строку "ecnalubma" в её зеркальное отражение(реверсировать). Сделать это двумя способами.
# input: 'ecnalubma'
# output: 'ambulance'
text = "ecnalubma"
print(text[::-1])

# text2 = 'ecnalubma'
# result = list(text2)
# result.reverse()
# print(''.join(result))
#
# stringResult = 'one two three four'
# stringResult2 = []
# stringList = stringResult.split()
# stringList.reverse()
#
# print(stringList)
# for i in stringList[::-1]:
#     stringResult2.append(i)
#
# print(stringResult2)
#
# items = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
# changedItem =[]
# for i in items:
#     if i > 0:
#         changedItem.append(1)
#     elif i < 0:
#         changedItem.append(-1)
#     else:
#         changedItem.append(0)
#
# print(items)
# print(changedItem)