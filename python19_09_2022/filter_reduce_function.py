'''
output = list(filter(lambda x:x%2==0,range(1,11)))
print(output)
'''

import functools
num = [1,2,3,4,5]
result = functools.reduce(lambda x,y:x+y,num)
print(result)
