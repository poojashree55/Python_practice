list1= [23, 8, 69, 9, 99, 5, 2]
for i in range(len(list1)-1):
    min_val= list1[i]
    for j in range(i+1, len(list1)):
        if list1[j] < min_val:
            min_val = list1[j]
    min_ind = list1.index(min_val, i)
    if list1[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind], list1[i]

print(list1)








