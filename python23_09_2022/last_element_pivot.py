# To get the correct position of the pivot element
def pivot_place(list1,first,last):
    pivot=list1[last]
    left=first
    right=last-1
    while True:
        while left <= right and list1[left] >= pivot:
            left = left + 1
        while left <= right and list1[right] <= pivot:
            right = right - 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[last], list1[left] = list1[left], list1[last]
    return left

def quicksort_devide(list1,first,last):
    if first < last:
        p = pivot_place(list1, first, last)
        quicksort_devide(list1, first, p - 1)
        quicksort_devide(list1, p + 1, last)

list1=[1,3,67,44,76,34,56]
n=len(list1)
quicksort_devide(list1,0,n-1)
print(list1)





