def linear_search(list_a, key):
    for i in range(len(list_a)):
        if key == list_a[i]:
            print("key element is found at the index: ", i)
            break
    else:
        print("element is not found")
            

list_a = [34, 23, 56, 4, 7, 8, 2, 40, 50, 60]
key = int(input("enter the element: "))
linear_search(list_a, key)
