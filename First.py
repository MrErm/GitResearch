# S = "hello"
# L = list(S)
# print(L)
# L[0] = "H"
# print(L)

# stringFromList = ''.join(L)
# print(type(stringFromList))
# print(stringFromList)

# str = "Привет"

# print(str.ascii_letters)

# import string

# print(string.ascii_letters)
# print(string.digits)


# simbols = 'r4bp78fd'
# digits = []
# letters = []

# for c in simbols:
#     if (c in string.digits):
#         digits.append(c)

#     if (c in string.ascii_letters):
#         letters.append(c)
    
# print(digits)  
# print(letters)

# lis = []
# num = [1,2,3,4,5,6,7,8]

# print(test_list)
# print(num[::-1])


# num.reverse()
# print(num)

# list1 = list('Python')
# print(list1)

# list2 = ''.join(list1)
# print(list2) 

# print(list1[3])
test_list = ['car', 'hello']
new_list = list()
new_list.append('hi')
new_list.append('bye')
new_list.append('goodbye')
print(new_list)

new_list1 = new_list + test_list
print(new_list1)

new_list.extend(test_list)
print(new_list)