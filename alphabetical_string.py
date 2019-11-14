# string = "sabrrtuwacaddabra"
# alphabetical_string = ''
# my_string = ''
# i = 0
#
# while i < len(string) - 1:
#     if string[i] <= string[i + 1]:
#         my_string += string[i + 1]
#         print(my_string)
#
#     if len(my_string) > len(alphabetical_string):
#         alphabetical_string = my_string
#     else:
#         my_string = string[i + 1]
#     i += 1
# print(alphabetical_string)

text = "sabrrabcdefgjrrebra"
longest_string = ''
my_string = ''
i = 0

while i < len(text) - 1:
    if text[i] <= text[i + 1]:
        my_string += text[i + 1]


        if len(my_string) > len(longest_string):
            longest_string = my_string
    else:
        my_string = text[i + 1]
    i += 1

print(longest_string)

