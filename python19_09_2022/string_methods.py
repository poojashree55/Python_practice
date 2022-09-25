'''
string = "puja"
#if single arguement is passed it must be a dictionary
dict1 = {"p":"s", "u":"h", "j":"w", "a":"e"}
t = string.maketrans(dict1)
tra = string.translate(t)
print(tra)
'''

'''
string = "hello pooja, welcome"
#if 2 arguements then length must equal
str1 = "hpowm"
str2 = "12345"
table = string.maketrans(str1,str2)
output = string.translate(table)
print(output)
'''

string = "hello guys$& and welcome))"
#whatever passed in 3rd arguement, it will delete
str1 = "abcd"
str2 = "9876"
str3 = "$&)"
table = string.maketrans(str1,str2,str3)
output = string.translate(table)
print(output)
