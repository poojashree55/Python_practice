n= int(input("Enter the number of rows: "))
for row in range(n):
    val = row+1
    decrement = n-1
    for col in range(row+1):
        print(val, end=" ")
        val = val+decrement
        decrement= decrement-1
    print()
    
