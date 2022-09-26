def linear_search(list_a, key):
    list_b = []
    flag = False
    for i in range(len(list_a)):
        if key == list_a[i]:
            flag = True
            list_b.append(i)   
    if flag==True:
        print("key element is found at the index:")
        for i in list_b:
            print(i)
    else:
        print("element is not found")
            

list_a = [34, 4, 2, 4, 7, 8, 2, 40, 50, 60]
key = int(input("enter the element: "))
linear_search(list_a,key)
