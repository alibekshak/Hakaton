# 1.1
# for i in range(1, 10+1):
#     print(i)

# #1.2

# num1 = int(input("Число: "))
# num2 = int(input("Число: "))
# print(f"{num1}+{num2}= {num1+num2}")

#1.3 

# num1 = int(input("Число: "))
# for i in range(1, num1+1):
#     if i % 3 == 0 or i %5 == 0:
#         print(i) 

#1.4
# a = input("Слово:")
# print(f"Длина слова {len(a)}")


#1.5

# fib1 = fib2 = 1

# n = int(input("Введите число: "))

# print(fib1, fib2, end=' ')

# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')


#1.6
# a = input("Слово:")
# print(a[::-1])


#1.7
# num = int(input("Введите число: "))
# for i in range(1, num+1):
#     for j in range(1, num+1):

#         print(f"{i} * {j} ={i * j}")


#1.8
# num = int(input("Введите число: "))

# lst=[]
# for i in range(2, num+1):
#     for j in lst:
#         if i % j == 0:
#             break
#     else:
#         lst.append(i)
# print (lst)


#1.9 
# num = 0
# a = input("Слово:")
# for i in a:
#     if "а" in i:
#         num += 1
# print(f"Количестов буквы а - {num}")


#1.10

# n = int(input("Введите число:"))
# count = 0
# while(n > 0):
#     count += 1
#     n = n // 10
# print("Количество цифр равно:", count)


#_________________________________________________________________________________________________

#2.1
# a = []
# n = int(input("Введите число:"))
# while n+1 >1:
#     n -= 1
#     a.append(n)
# print(a)


#2.2

# a = input("Слово:")
# if a:
#     b = a[::-1]
#     print(b)


#2.3
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# if num1 > num2:
#     print(f"{num1} больше {num2}")

# elif num1 < num2:
#     print(f"{num2} больше {num1}")

# else:
#     print("Числа равны")


# #2.4 
# n1 = int(input("Введите число:"))
# n2 = int(input("Введите число:"))
# if n1 != n2:
#     a = []
#     a.append(n1)
#     a.append(n2)
#     sum_lst = sum(a) 
#     lst_avg = sum_lst/len(a) 

#     print(round(lst_avg,3))
# else:
#     print("Выбирете другие значения")


#2.5
# a = input("Слово:")
# b = input("Слово:")
# num = 0
# for i in a:
#     for j in b:
#         if i == j:
#             print(f"{i}, {j}")  


#2.6
# a = input("Слово:")
# lis = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]
# for i in a:
#     if i in lis:
#         print(i)    


#2.7
# n1 = int(input("Введите число:"))
# for i in range(1, n1):
#     if i % 3 == 0:
#         print(i)


#2.8
# n1 = int(input("Введите число:"))
# n2 = int(input("Введите число:"))

# a = []
# a.append(n2)
# sum_lst = sum(a) 
# lst_avg = sum_lst/len(a) 

# print(round(lst_avg,3))

# for i in range(1, n1+1):
#     for j in range(1, n2+1):
#         if i % lst_avg == 0 and j % lst_avg == 0:
#             print(i, j)


#2.9
# a = input("Слово:")
# b = input("Слово:")
# num = 0
# for i in a:
#     for j in b:
#         if i == j:
#             print(f"{i}")  


#2.10
# lis1 = ["abs", "bca", 1, 5, 8]
# lis2 = ["abs", 'fff', 3, 4, 8] 
# for i in lis1:
#     for j in lis2:
#         if i == j:
#             print(i, j)


#___________________________________________________________________________________________

#3.1

# def fib():
#     fib1 = fib2 = 1
#     n = int(input("Введите число: "))
#     print(fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print (fib2, end=' ')

# fib()



#3.2
# def num():
#     n1 = int(input("Введите число: "))
#     n2 = int(input("Введите число: "))
#     return f"{n1} + {n2} = {n1 + n2}"
# print(num())



#3.3

# def max_min ():
#     num1 = int(input("Введите число: "))
#     num2 = int(input("Введите число: "))
#     if num1 > num2:
#         return (f"{num1} больше {num2}")

#     elif num1 < num2:
#         return(f"{num2} больше {num1}")
# print(max_min())


#3.4

# def srt1():
#     b = input("Слово:")
#     num = 0
#     for i in b:
#         num+=1
#     return(f"{b} - {num} буквы")

# print(srt1())


#3.5

# def num():
#     a = []
#     n = int(input("Введите число:"))
#     while n+1 >1:
#         n -= 1
#         a.append(n)
#     return(a)

# print(num())


#3.6

# def lis():
#     a = input("Слово:")
#     if a:
#         b = a[::-1]
#         return(b)
# print(lis())


#3.7

# def delit():
#     n = int(input("Введите число:"))
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             print(i)

# delit()


#3.8

# def delit1():
#     n1 = int(input("Введите число:"))
#     for i in range(1, n1):
#         if i % 3 == 0:
#             print(i)
# delit1()


#3.9
# def avg():
#     n1 = int(input("Введите число:"))
#     n2 = int(input("Введите число:"))

#     a = []
#     a.append(n2)
#     sum_lst = sum(a) 
#     lst_avg = sum_lst/len(a) 

#     print(round(lst_avg,3))

#     for i in range(1, n1+1):
#         for j in range(1, n2+1):
#             if i % lst_avg == 0 and j % lst_avg == 0:
#                 print(i, j)

# avg()


#3.10
# def aver():
#     a = input("Слово:")
#     b = input("Слово:")
#     num = 0
#     for i in a:
#         for j in b:
#             if i == j:
#                 print(f"{i}")  

# aver()


#___________________________________________________________________________________________

#4.1

class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        return  f"Привет {self.name}"

    def __str__(self) -> str:
        return f"Имя:{self.name}, возрост:{self.age}"

man = Man("Jon", 26)
print(man.hi())
print(man)


#4.2
class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        return  f"Привет {self.name}"

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


class Student(Man):
    def __init__(self, name, age, student_book,):
        super().__init__(name, age)
        self.student_book = student_book
        l = [4, 5, 5, 3]
        self.b= sum(l) / len(l)

    def ocenk(self):
        l = [4, 5, 5, 3]
        return f"Оценки: {l}"
    
    def aver(self):
        return f"Имя {self.name}, номер студенческого билета: {self.student_book}, среднии балл {self.b}"

ocen = Student("Jon", 12, 1234)
print(ocen.ocenk())
print(ocen.aver())


#3 
class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def square(self):
        return f"Площадь равна {self.height * self.width}"

rect = Rectangle(3, 5)
print(rect.square())


#4.4 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return f"Площадь круга {3.14 * self.radius ** 2}"

cir = Circle(2)
print(cir.square())


#4.5

class Bank:

    def __init__(self, balans, percent):
        self.balans = balans
        self.percent = percent

    def add(self, amount):
        self.amount = amount
        self.balans += self.amount
        return f"Вам перевели {self.amount}, на считу : {self.balans}"

    def take(self, giv):
        self.giv = giv
        self.balans -= self.giv
        return f"Снятие денег на сумму {self.giv}, на считу осталось: {self.balans}"

    def benefit(self, month):
        self.month = month
        self.balans *= self.percent * 0.01 * self.month
        return f"{self.percent} процентов на срок {self.month} месяцев - ваш счет увеличется до {self.balans} "

bank = Bank(100, 10)

print(bank.add(1000))
print(bank.take(500))
print(bank.benefit(24))

