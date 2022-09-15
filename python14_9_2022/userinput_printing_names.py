str = "POO"
print_P = [[" " for i in range(6)] for j in range(6)]
print_O = [[" " for i in range(6)] for j in range(6)]


for row in range(6):
    for col in range(6):
        if col==0 or (col==4 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<4)):
            print_P[row][col]= "*"

for row in range(6):
    for col in range(6):
        if ((row==0 or row==5) and (col!=0 and col!=5)) or ((col==0 or col==5) and (row!=0 and row!=5)):
            print_O[row][col]= "*"

for i in range(6):
    for j in range(6):
        print(print_P[i][j],end=" ")
    print(end="  ") 
    for j in range(6):
        print(print_O[i][j],end=" ")
    print(end="  ") 
    for j in range(6):
        print(print_O[i][j],end=" ")
    print()

