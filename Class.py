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

stock = [
    {"name": "iPhone", "stock": 24, "price": 120000,
     "recomended":["Iphone 16", "Samsung", "Xiaomi"]},
    {"name": "iPad", "stock": 8, "price": 99000, "discount": 2300},
    {"name": "Xiaomi", "stock": 41, "price": 35000.5,}
]
stock[0]["recomended"].append("Xiaomi Mi11")
stock[2]["price"] = stock[2]["price"] - 20000
pprint(stock)
