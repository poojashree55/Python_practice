#read 4 values from the user, if any 2 values are eual, print error, otherwise find the largest value of the 4 variables.
'''
a= int(input("enter the first value: "))
b= int(input("enter the first value: "))
c= int(input("enter the first value: "))
d= int(input("enter the first value: "))

if a==b or a==c or a==d or b==c or b==c or c==d:
    print("Error")
elif a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d:
    print("b is greater")
elif c>d:
    print("c is greater")
else:
    ("d is greater")
'''


'''
units = int(input("enter the consumed units: "))u90jko0o0o0t7w3w
if units<=100:
    print("You are free from charges")
elif units>100 and units<=150:
    x=units-100
    bill= x*4
    print("your bill amount is: ", bill)
elif units>150:
    a=units-100
    b=a-50
    c= (b*10) + (50*4)
    print("your bill amount is: ", c)
'''

def catalan(n):
   if n <=1 :
      return 1
   res = 0
   for i in range(n):
      res += catalan(i) * catalan(n-i-1)
   return res
for i in range(4):
   print (catalan(i))

    
