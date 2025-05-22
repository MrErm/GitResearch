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



class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.lengh = length

    def area(self):
        return self.width * self.lengh

    def perimeter(self):
        return 2 * (self.lengh + self.width)
    
obj1 = Rectangle(5, 6)
print(obj1.area())
print(obj1.perimeter())



