''' num = [1,2,3,4]
l = [x*10 for x in num]
print(l)
'''

'''
words= ["hello", "a", "poo"]
l = [x.upper() for x in words]
print(l)
'''

'''
str1 = "pooja28031995"
l = [x for x in str1 if x.isdigit()]
print(l)
'''

'''
str1 = "pooja28031995"
l = [x for x in str1 if x.isalpha()]
print(l)
'''

'''
list1 = [[1,2,4],[3,5,8],['a','b','c']]
list2 = [x[1] for x in list1]
print(list2)
'''

'''
def square(x):
    return x*x
l = [square(x) for x in range(1,11)]
print(l)
'''

'''
a=[1,2,3]
b=[4,5]
list1=[x+y for x in a for y in b]
print(list1)
'''

'''
a=[1,7,3]
b=[4,5,9]
list1=[a[i]+b[i] for i in range(0,len(a))]
print(list1)
'''




