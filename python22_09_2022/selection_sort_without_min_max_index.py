num=int(input("How many numbers you want to enter: "))
list1= [int(input("Enter the number: "))for x in range(num)]
for i in range(len(list1)-1):
    min_ind = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[min_ind]:
            min_ind = j
    if list1[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind], list1[i]

print(list1)