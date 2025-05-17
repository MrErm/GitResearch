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

import string

# print(string.ascii_letters)
# print(string.digits)


simbols = 'r4bp78fd'
digits = []
letters = []

for c in simbols:
    if (c in string.digits):
        digits.append(c)

    if (c in string.ascii_letters):
        letters.append(c)
    
print(digits)  
print(letters)

