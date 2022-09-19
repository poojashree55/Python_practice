'''
a = [2,3,4]
def square(x):
    return(x*x)
output = list(map(square,a))
print(output)
'''

'''
a = [2,3,4]
output = list(map(lambda x:x*x,a))
print(output)
'''    

a = [2,3,4]
b = [5,1,6]
output = list(map(lambda x,y:x+y,a,b))
print(output)
