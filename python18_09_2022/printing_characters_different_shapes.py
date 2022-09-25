#printing character in square shape
'''
num = int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(num):
        print("$",end=" ")
    print()
'''

#another way of printing the above
'''
num = int(input("Enter the number of rows: "))
for i in range(num):
    print("$ "*num)
'''


#printing character in Right triangle shape
'''
num = int(input("Enter the number of rows: "))
for i in range(num):
    print("* "*(i+1))
'''

#printing character in Left triangle shape
'''
num = int(input("Enter the number of rows: "))
for i in range(1, num+1):
    print("  "*(num-i) + "* "*i)
'''

#printing character in Triangle shape
'''
num = int(input("Enter the number of rows: "))
for i in range(1, num+1):
    print(" "*(num-i) + "* "*i)
'''

#printing character in Reverse Triangle shape
'''
num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    print(" "*(num-i) + "* "*i)
'''

#printing character in Diamond shape

'''
num = int(input("Enter the number of rows: "))
for i in range(1, num+1):
    print(" "*(num-i) + "* "*i) 
for i in range(num-1,0,-1):
    print(" "*(num-i) + "* "*i)
'''

#printing character in Reverse Right triangle shape
'''
num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    print("  "*(num-i) + "* "*i)
'''


#printing character in Reverse Left triangle shape
'''
num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    print("* "*i)
'''

#printing character in Arrow shape
'''
num = int(input("Enter the number of rows: "))
for i in range(1, num+1):
    print("* "*i) 
for i in range(num-1,0,-1):
    print("* "*i)
'''

#printing character in Reverse Arrow shape

num = int(input("Enter the number of rows: "))
for i in range(1, num+1):
    print("  "*(num-i) + "* "*i) 
for i in range(num-1,0,-1):
    print("  "*(num-i) + "* "*i)
