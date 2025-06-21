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
# test_list = ['car', 'hello']
# new_list = list()
# new_list.append('hi')
# new_list.append('bye')
# new_list.append('goodbye')
# print(new_list)

# new_list1 = new_list + test_list
# print(new_list1)

# new_list.extend(test_list)
# print(new_list)

# class BankAccount:

#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def add(self, plus):
#         self.balance = self.balance + plus
#         print(f"Зачислено {plus}")
    
#     def withdraw(self, minus):
        
#         if self.balance - minus >= 0:
#             self.balance = self.balance - minus
#             print(f"Снято {self.balance}")
#         else: 
#             print("На балансе недостаточно средств")

# count = BankAccount("256516", 100)

# count.add(35)
# print(f"Your balance {count.balance}")

# count.withdraw(20)
# print(f"Your balance {count.balance}")

# phones = ["Iphone 16", "Samsung", "Xiaomi","Iphone 16", "Samsung", "Xiaomi"]

# if "Xiaomi 1" in phones:
#     print("Xiaomi")
# else:
#     print("Такого телефона нет")


# sale = input("Введите сумму продажи: ")
# sale = int(sale)

# if sale <= 5000:
#     discount = sale * 5/100
#     print(f"Скидка: {discount}")

# elif sale <= 15000:
#     discount = sale * 12/100
#     print(f"Скидка: {discount}")

# elif sale <= 25000:
#     discount = sale * 20/100
#     print(f"Скидка: {discount}")

# else:
#     sale > 25000
#     discount = sale * 30/100
#     print(f"Скидка: {discount}")
    

# print(f"Сумма с учетом скидки: {sale - discount} ")




# amount = int(input("Введите сумму продажи: "))
# # вычисление скидки
# if amount > 0:
#     if amount>25000:
#         discount=amount * 0.3
#     elif amount>15000:
#         discount=amount * 0.2
#     elif amount>5000:
#         discount = amount*0.12
#     else:
#         discount = amount*0.05
#     print("Скидка: ", discount)
#     print("Сумма с учетом скидки : ", amount-discount)
# else:
#     print("Некорректная сумма")



# Просто задачки 

# a = float(input("Введите температуру в градусах Цельсия: "))

# f = (9/5)*(a) + 32

# print(f"{a} градусов Цельсия равны {f} градусам Фаренгейта")



# Цикл for

# for letter in "python":
#     print(letter.upper())


# string = "Как у вас дела?"

# for word in string.split():
#     print(f"Длина слова {word}: {len(word)}")


# scores = [6, 21, 19, 15, 13, 22]

# sum = 0
# for score in scores:
#     sum += score
# print(sum)

# print(sum/len(scores))






from Class import discounted


stock = [
    {'name': 'iPhone 16 Pro', 'stock': 24, 'price': 65475.4, 'discount': 15},
    {'name': 'Samsung Galaxy', 'stock': 8, 'price': 50000, 'discount': 10},
    {'name': 'Xiaomy', 'stock': 18, 'price': 80000, 'discount': 5}
]

for phone in stock:
    
    phone["finaly_price"] = discounted(phone["price"], phone["discount"], name = phone["name"])

print(stock)
    
