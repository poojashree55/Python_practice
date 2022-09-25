'''
list1= [23, 45, 8, 9, 22, 18, 12]
for i in range(len(list1)):
    min_val= min(list1[i:])
    min_ind= list1.index(min_val)
    list1[i],list1[min_ind] = list1[min_ind], list1[i]
print(list1)
'''

'''
list1= [23, 45, 8, 9, 22, 18, 12]
for i in range(len(list1)):
    max_val= max(list1[i:])
    max_ind= list1.index(max_val)
    list1[i],list1[max_ind] = list1[max_ind], list1[i]
print(list1)
'''

#duplicate numbers sorting
'''list1= [23, 8, 8, 9, 23, 18, 12]
for i in range(len(list1)-1): #last value no need to check
    min_val= min(list1[i:])
    min_ind= list1.index(min_val, i)
    list1[i],list1[min_ind] = list1[min_ind], list1[i]
print(list1)
'''


#All the iterations as output and modified 
list1= [23, 8, 69, 9, 99, 5, 2]
for i in range(len(list1)-1):
    min_val= min(list1[i:])
    min_ind= list1.index(min_val, i)
    if list1[i] != list1[min_ind]:
        list1[i],list1[min_ind] = list1[min_ind], list1[i]
        
    print(list1)
