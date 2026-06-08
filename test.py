# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# else:
#     print('outside the loop')

# sent = 'heyyou'
# print('hey' in sent)

# def add_nums(num1, num2):
#     print(num2)

# add_nums(num2=3, num1=4)

# def sum_all_nums(*nums):
#     # total = 0
#     # for num in nums:
#     #     total += num     # same as total = total + num 
#     return nums
# print(sum_all_nums(2, 3, 5)) # 10


# def add_num(num1, num2):
#     return num1 + num2

# def get_input(f):
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))

#     return f(num1, num2)

# print(get_input(add_num))


# ----- DECORATORS
# def greeting():
#     return 'Hello! Odili'

# def uppercase_decorator(fn):
#     def wrapper():
#         function = fn()
#         uppercase = function.upper()
#         return uppercase
#     return wrapper

# greet = uppercase_decorator(greeting)
# print(greet())



# def uppercase_decorator(fn):
#     def wrapper():
#         function = fn()
#         uppercase = function.upper()
#         return uppercase
#     return wrapper

# @uppercase_decorator
# def greeting():
#     return 'Hello! Odili'

# print(greeting())

# def decorator_with_parameter(fn):
#     def wrapper(param1, param2, param3):
#         fn(param1, param2, param3)
#         print(f'I live in {param3}')
#     return wrapper

# @decorator_with_parameter
# def aboutMe(param1, param2, param3):
#     print(f'I am {param1} {param2}')

# aboutMe('Eze', 'Odili', 'Nigeria')


# ----- HIGHER ORDER FUNCTION
# arr = [1, 2, 3, 4, 5]

# newArr = []
# for i in range(1, len(arr) +1):
#     newArr.append(f'{i}')

# print(newArr)

# stringArr = map(lambda x: str(x), arr)

# print(list(stringArr))


# Filter long name
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
# def is_name_long(name):
#     if len(name) > 7:
#         return True
#     return False

# long_names = filter(is_name_long, names)
# long_names = filter(lambda x: len(x) > 7, names)
# print(list(long_names))         # ['Asabeneh']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chain = list(map(lambda x: x ** 2, list(filter(lambda x: x > 1, numbers))))

# ----- DATE AND TIME
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
# print("Current year:", today.year)   # 2019
# print("Current month:", today.month) # 12
# print("Current day:", today.day)     # 5


class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
# print(p1.person_info())
new_skills = ['HTML', 'CSS', 'JavaScript']
p1.add_skill(new_skills)

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
# print(p1.skills)
# print(p2.skills)



# --------- Scattered -----------
import json
import os
# data = json.loads('./data/countries_data.json')

filename = './data/countries_data.json'

# print(data.countries_info[0])

# if os.path.exists(filename):
#   with open(filename, 'r', encoding='utf-8') as f:
#     countries_data = json.load(f)

# print(countries_data[0])

if None:
    x = 1
    print(x)
else:
  print('Nothing')
    
x = 0
# if x > 0:
#     result = "Positive"
# else:
#     result = "Non-Positive"

x += 1 if  x > 0 else 0
print(x)


lst = [(8999, ''), (766, 'the'), (583, 'I'), (555, 'and'), (533, 'to'), (487, 'of'), (460, 'a'), (341, 'in'), (334, 'is'), (318, 'you'), (310, 'my')]

# print('' in (type() == int, '') in lst)
# for i in range(len(lst)):
#     if '' in lst[i]:
#         continue
#     else:
#         print(lst[i])
    # print(lst[i])
# print((type(9)) == int)


string = 'do you know java is not my thing but javascript'

# import re

# print(re.findall(r'\bjava\b', string))


# import numpy
# lst  = [["num",2], ["num", 3]]
# arr = numpy.array(lst)

# for obj in lst:
#     for i in obj:
#       print(i)
        


men = ["odili", "fatai", "desmond"]
men.append("sultan")
print(men)





