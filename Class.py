# class Person:
#     def __init__(self):
#         print("Это человек")
# tom = Person()        

# class Man:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# nik = Man("Ник", 22)

# print(nik.name)
# print("ему",nik.age)
# nik.company = "Yandex"
# print(f"Работает в", nik.company)



# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.lengh = length

#     def area(self):
#         return self.width * self.lengh

#     def perimeter(self):
#         return 2 * (self.lengh + self.width)
    
# obj1 = Rectangle(5, 6)
# print(obj1.area())
# print(obj1.perimeter())


# product = {
#     "name": "Iphone 16",
#     "stock": 24,
#     "price": 120000,
#     "country": "RU"
# }
    

# product["name"] = "Ipad Air"

# print(product.get("country", "CN"))

# del product["stock"]
# print(product)

from pprint import pprint

# product = {
#     "name": "Iphone 16",
#     "stock": 24,
#     "price": 120000,
#     "country": "RU"
# }

# phones = ["Iphone 16", "Samsung", "Xiaomi"]

# product["recomended"] = phones
# pprint(product["recomended"][1])

# product["recomended"].append("Ipad")
# pprint(product)

# stock = [
#     {"name": "iPhone", "stock": 24, "price": 120000,
#      "recomended":["Iphone 16", "Samsung", "Xiaomi"]},
#     {"name": "iPad", "stock": 8, "price": 99000, "discount": 2300},
#     {"name": "Xiaomi", "stock": 41, "price": 35000.5,}
# ]
# stock[0]["recomended"].append("Xiaomi Mi11")
# stock[2]["price"] = stock[2]["price"] - 20000
# pprint(stock)






phone1 = {'name': 'iPhone 16 Pro', 'stock': 24, 'price': 65475.4, 'discount': 15}
phone2 = {'name': 'Samsung Galaxy', 'stock': 8, 'price': 50000, 'discount': 10}
phone3 = {'name': '', 'stock': 18, 'price': 80000, 'discount': 5}


def discounted(price, discount, max_discount = 20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большпая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)
    
apple_desc = discounted(phone1["price"], phone1["discount"], name=phone1["name"])
print(apple_desc)

android_desc = discounted(phone2["price"], phone2["discount"], name=phone2["name"])
print(android_desc)

noname = discounted(phone3["price"], phone3["discount"], name=phone3["name"])
print(noname)
