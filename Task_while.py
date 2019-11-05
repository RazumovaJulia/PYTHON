# list_tuple = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
# print(list_tuple[2:13:3])
# print(list_tuple[2::3])
def thirds(list_thirds):
    thirds = []
    i = 0

    while i < len(list_thirds):
        if (i + 1) % 3 == 0:
            thirds.append(list_thirds[i])
        i += 1
    return thirds

    assert thirds((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')) == (3, 6, 9, 'b')
# print(thirds([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c']))
