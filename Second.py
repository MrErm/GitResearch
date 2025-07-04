# from art import text2art

# from anytree import Node, RenderTree

# root = Node("Корень")
# child1 = Node("Дочерний 1", parent=root)
# child2 = Node("Сыновий 20", parent=root)
# subchild = Node("Поддочерний 1", parent=child1)
# stillchild = Node("Еще сыновий", parent=child2)
# stillchild2 = Node("И еще сыновий", parent=stillchild)

# for pre, fill, node in RenderTree(root):
#     print(f"{pre}{node.name}")


# ----------------------Exception -----------------------


# def cut_cake(people):
#     try:
#         parts = 1/people
#         print(f"Каждый человек получит {parts} пирога")
#     except (ArithmeticError, TypeError):
#         print("Не могу поделить!")


# cut_cake("вапивип")




while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(f"Сумма чисел: {a + b}")

    z = input("Нажмите Y или y для завершения программы: ")

    if (z =="Y" or z =="y"):
        break
    
        


   