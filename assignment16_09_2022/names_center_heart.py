num =int(input("Enter the number: "))
msg =input("Enter any msg: ")
l =len(msg)
n = num//2
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    if num%2==0:
      for j in range(2*(n-i-1)):
          print(" ",end="")
    else:
      for j in range(2*(n-i-1)+1):
          print(" ",end="")
    for j in range(i+1): 
        print("* ",end="")
    print()

if num%2==0:
    if l%2==0:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*((num-l)//2))
    else:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*(((num-l)//2)+1))
else:
    if l%2==0:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*(((num-l)//2)+1))
    else:
        print("* "*((num-l)//2) + " ".join(msg) + " *"*((num-l)//2))
        
    
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print("* ",end="")
    print()
