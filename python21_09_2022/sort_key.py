list1= ["eeee", "aa", "bbb", "fffff", "g"]
list1.sort(key=len)
list1
['g', 'aa', 'bbb', 'eeee', 'fffff']


list2 = [[3,10], [1,5], [2,3]]
list2.sort()
list2
[[1, 5], [2, 3], [3, 10]]

def ListBySec(element):
    return element[1]

list2.sort(key=ListBySec)
list2
[[2, 3], [1, 5], [3, 10]]