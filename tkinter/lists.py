list_in_list=[["1","2","3"],["4","5","6"],["7","8","9"]]

# for i in list_in_list:
#     for j in i:
#         print(j, type(j), end=" ")

print()

list_in_list_int=[]

for i in list_in_list:
    for j in i:
        list_in_list_int.append(int(j))
        print(int(j), end=" ")




