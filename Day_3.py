# ----- OPERATORS -----
# - 1
age = 24

# - 2
height = 5.11

# - 3
cplx = 1 + 2j

# - 4
# Area of a triangle 0.5 * b * h
# base = input('Enter base of a traingle ')
# height = input('Enter height of a traingle ')

# area = 0.5 * int(base) * int(height)
# print(int(area))

# - 5
# Perimeter of Triangle
# a = input('Enter side a ')
# b = input('Enter side b ')
# c = input('Enter side c ')

# perimeter = int(a) + int(b) + int(c)
# print('The Area of the Triangle is %d' %perimeter)

# - 6
# width = int(input('Enter width of the triangle '))
# length = int(input('Enter length of the triangle '))

# area = width * length
# perimeter = 2 * width * length

# print(f'Area of the rectangle: {area}')
# print(f'Perimeter of the rectangle: {perimeter}')

# - 7
radius = int(input('Enter raidus '))
pi = 3.14

area = pi * radius * radius
circumference = 2 * pi * radius * radius



# - 9 & 10
import math
def euclidianDistance(a, b):
    x1, x2, y1, y2 = a[0], b[0], a[1], b[1]
    
    # Formula -> Math.Root((x2-x1)**2 + (y2-5y1)**2)
    x = (x2 - x1) ** 2
    y = (y2- y1) ** 2

    dist = math.sqrt((x + y))
    return dist
# print(euclidianDistance((2,2), (6,10)))


# - 11
# At what x value will y equal 0
# y = x^2 + 6x + 9 

x = 0
y = 1

# while y != 0:
#     print('Started')
#     y = (x ** 2) + (6 * x) + 9
#     x -= 1

# print('At x equal %d,'%x, ' y is equal to %d' %y)


# - 12
# print(len('dragon') != len('python'))

# - 13
# print('on' in 'dragon' and 'on' in 'python')

# - 14
string = 'I hope this course is not full of jargon.'
# print('jargon' in string) 

# - 15
# print(not('on' in 'python') and not('on' in 'dragon'))

# - 16
length_of_python = len('python')
# print('Length of python as number', length_of_python)
# print('Length of python as float', float(length_of_python))
# print('Length of python as number', str(length_of_python))

# - 17
# num = input('Enter number ')

# if int(num) % 2 == 0:
#     print('Number is even')
# else:
#     print('Number is odd')

# - 18
# print(7 // 3 == int(2.7))

# - 19
# print(type('10') == type(10))

# - 20
# print(int(float('9.8')) == 10)

# - 21
# hours = input('Enter working hours ')
# rate_per_hour = input('Enter rate per hour ')
# weekly_pay = 7 * int(hours) * int(rate_per_hour)

# print(weekly_pay)

# - 22
# number_years = input('Enter number years lived ')
# years_in_seconds = 60 * 60 * 24 * 365 * int(number_years)

# print(years_in_seconds)
# - 23
# write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")



# ---------- DONE ----------


