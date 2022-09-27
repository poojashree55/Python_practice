'''
x = []
if x:
    print(x,"True")
else:
    print(x,"False")#In python anything empty is treated as False, so this executes
'''

'''
a = (1,10)
b = 0
c = []
if a or b and c:
    print("True")
else:
    print("False")
#operator precedence: and operator has highest precedence, so first b & c will execute buth results in false and their result also false.
then a result is true as it contains values. true or false results in true.
'''

'''
list1 = ["ABC", "XYZ", "pqR"]
for i in list1:
    i.lower() # lower() method will not modify the original string, it will just return a string with lower case. we are not storing the variable any
print(list1)
'''

'''
list1 = ["ABC", "XYZ", "pqR"]
list2 = []
for i in list1:
    x= i.lower()# coverts to lower and result is stored in x. and results are stored to list2.
    list2.append(x)
print(list2)
'''

'''
list1 = ["abc", "123"]
for i in list1:
    list1.append(i)# forloop became infinite here, so it will not give output
print(list1)
'''

'''
for i in range(1,20):
    if i==5:
        break # when break statement executes control will come out of the group
    else:
        print(i)
else:
    print("hello")# it executes only when the loop not terminated by a break statement, here loop terminated by a break statement 
'''

'''
for i in range(1,20):
    if i==5:
        continue
    else:
        print(i)
else:
    print("hello")#everything is executed except 5. bcs loop is not terminated.
'''


list1 = ["a","b","c",["xmas","yummy"], "p", "q", "r", "s"]
print(list1[3:4]) # in slicing method, end is excluded and it results as list.
print(list1[3:4][0]) # it will return the list index of 0. complete list is considered as 1 element.
print(list1[3:4][0][1][2]) # list inside index and list inside index and list inside index
    
