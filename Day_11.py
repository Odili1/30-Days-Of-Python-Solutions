# ----- FUNCTIONS -----
# --- LEVEL 1 ---
# - 1
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 4))

# - 2
# area = π x r x r
from math import pi
def area_of_circle(r):
    return pi * r * r

print(area_of_circle(5))

# - 3
def add_all_nums(*args):
    sum = 0
    for i in args:
        if (isinstance(i, int)):
            sum += i
        else:
            return 'All arguments should be of number type'
    
    return sum

print(add_all_nums(1, 3, 5, 7, 9))

# - 4
# Celcsius to Farenheit => °F = (°C x 9/5) + 32
def convert_celsius_to_farenheit(c):
    f = (c * (9/5)) + 32
    return f'{f} F'

print(convert_celsius_to_farenheit(100))

# - 5
def check_season(month):
    month = month.lower()
    if month == 'september' or month == 'september' or month == 'september':
        return 'Autumn'
    if month == 'december' or month == 'january' or month == 'february':
        return ('Winter')
    if month == 'march' or month == 'april' or month == 'may':
        return ('Spring')
    if month == 'june' or month == 'july' or month == 'august':
        return ('Summer')


print(check_season('August'))

# - 6
# Slope of linear Equation m = (y2 - y1) / (x2 - x1)
from typing import List
def calculat_slope(x: List, y: List) -> int:
    x = x[0] - x[1]
    y = y[0] - y[1]

    return y/x

print(calculat_slope([1, 2], [1, 2]))

# - 7
# Quadratic Equation => ax² + bx + c = 0
# def solve_quadratic_eqn(a, b):




# - 8
def print_list(lst: List[int]) -> None:
    for i in lst:
        print(i)

print_list([1, 2, 3, 4, 5])


# - 9
def reverse_list(lst):
    reversed_list = []
    for index in range(1, len(lst) + 1):
        reversed_list.append(lst[-index])
    
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

# - 10
def capitalize_list_items(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i].capitalize())

    return new_lst

print(capitalize_list_items(["odili", "amara", "john", "azaman"]))


# - 11
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]


# - 12
def remove_item(lst, item):
    lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

# - 13
def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# - 14
def sum_of_odds(num):
    sum = 0
    for i in range(num + 1):
        sum += i if i % 2 == 0 else 0
        # if i % 2 == 0:
        #     sum += i
        # else:
        #     continue
        
    return sum

print(sum_of_odds(10))


# - 15
def sum_of_even(num):
    sum = 0
    for i in range(num + 1):
        sum += i if i % 2 != 0 else 0
        # if i % 2 == 0:
        #     sum += i
        # else:
        #     continue
        
    return sum

print(sum_of_even(10))



# --- LEVEL 2 ---
# - 1
def evens_and_odds(num):
    odd = 0
    even = 0

    for i in range(num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    
    return f'The number of odds are {odd}. \nThe number if evens are {even}'

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

# - 2
def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i

    return fact

print(factorial(10))


# - 3
def is_empty(param):
    if param:
        return 'Empty'
    else:
        return 'not empty'

print(is_empty(''))

# - 3
# def calculate_mean(lst):

# def calculate_median(lst):

# calculate_mode(lst):

# calculate_range(lst):

# calculate_variance(lst):

# calculate_std(lst):




# --- LEVEL 3 ---
#  - 1
from math import sqrt
def is_prime(num):
    if num == 2: return True
    for i in range(1, int(num / 2)):
        if (num % i == 0):
            return False
    return True
print(is_prime(10))


# - 2
def unique(lst):
    lst_length = len(lst)
    st_length = len(set(lst))

    return 'List is unique' if lst_length == st_length else 'List is not unique'

print(unique([1, 2, 4, 4]))

# - 3
def same_type(lst):
    for i in range(len(lst)):
        if type(lst[0]) != type(lst[i]):
            return False
    return True

print(same_type([1,2,3,4,'5']))


# - 4
def valid_variable(var):
    return var.isidentifier()

print(valid_variable('@vvf'))


# - 5
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
import json
import os
from operator import itemgetter

json_path = os.path.join(os.getcwd(), "data", "countries_data.json")
print("Json path", json_path)
with open(json_path, "r", encoding="utf-8") as json_data:
    countries_data = json.load(json_data)


# 1)
def most_spoken_languages():
    lang_dict = {}
    for countries in countries_data:
        for lang in countries["languages"]:
            if lang_dict.get(lang):
                lang_dict[lang] += 1
            else:
                lang_dict[lang] = 1


    # lang_list = [(language, count) for language, count in lang_dict.items()]
    sorted_lang_list = sorted(list(lang_dict.items()), key=lambda index: index[1], reverse=True)
    ten_most_spoken_lang_list = sorted_lang_list[:10]
    ten_most_spoken_lang = [lang for lang_tpl in sorted_lang_list[:10] for lang in lang_tpl if type(lang) == str]
    return ten_most_spoken_lang_list

def most_populated_countries():
    # population_dict = {}
    # for country in countries_data:
    #     population_dict[country["name"]] = country["population"]

    # population_list = [(name, population) for name, population in population_dict.items()]
    
    # sorted_population_list = sorted(countries_data, key=itemgetter(1), reverse=True)
    sorted_population_list = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    
    # ten_most_populated = [country for country_tpl in sorted_population_list[:10] for country in country_tpl if type(country) == str]
    
    # return ten_most_populated
    return sorted_population_list[:10]


print("Ten Most SPoken Language", most_spoken_languages())
print("Ten Most Populated", most_populated_countries())





# ---------- [7] ----------
