# ----- HIGHER ORDER FUNCTIONS -----
# def greeting():
#     return 'Welcome to Python'

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()

#         return make_uppercase
#     return wrapper

# g = uppercase_decorator(greeting)
# print(g())


# -----> DECORATORS
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()

        return make_uppercase
    return wrapper

@uppercase_decorator

def greeting():
    return 'Welcome to Python'

# print(greeting())


def decorator_with_parameter(function):
    def wrapper(first, second, country):
        func = function(first, second, country)
        print("I live in {}".format(country))
    return wrapper

@decorator_with_parameter
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))
    
# print_full_name("Eze", "Odili", "Finland")


# ----- > MAP
number = [1,2,3,4,5]

def square(x):
    return x **2

# new_lst = map(square, number)
new_lst = map(lambda x: x ** 2, number)
# print(list(new_lst))

even_num = filter(lambda x: x % 2 == 0, number)
# print(list(even_num))




# --- LEVEL 1 ---
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# - 4
# for i in countries:
#     print(i, end=" ")

# - 5
# for i in names:
#     print(i, end=' ')

# - 6
# for i in numbers:
#     print(i, end=" ")

# print("\n\n")



# --- LEVEL 2 ---
# - 1
def uppercase(function):
    def wrapper(countries):
        arr = function(countries)
        arr_upper = [i.upper() for i in arr]
        return arr_upper
    return wrapper

@uppercase
def func(countries):
    return countries

# print(func(countries))
mapper = map(lambda x: x.upper(), countries)

# print(list(mapper))


# - 2
map_num = list(map(lambda x: x ** 2, numbers))
# print(map_num)

# - 3
map_name = list(map(lambda x: x.upper(), names))
# print(map_name)

# - 4
def land(country):
    if 'land' in country:
        return country
    pass 

filter_countries = list(filter(lambda x: 'land' in x, countries))
# print(filter_countries)

# - 5
filter_six = filter(lambda x: len(x) == 6, countries)
# print(list(filter_six))

# - 6
filter_six_more = filter(lambda x: len(x) >= 6, countries)
# print(list(filter_six_more))

# - 7
filter_e = list(filter(lambda x: x.startswith('E'), countries))
# print(filter_e)

# - 8
chain = list(map(lambda x: x ** 2, list(filter(lambda x: x > 1, numbers))))
# print(chain)

# - 9
def get_string_lists(lst):
    return list(filter(lambda x: type(x) == str, lst))

# print(get_string_lists([1,2,"hey",4, "you"]))

# - 10
from functools import reduce
reduce_num = reduce(lambda x, y: x + y, numbers)
# print(reduce_num)

# - 11
def reduce_func(x, y):
    if (countries.index(y) == len(countries) - 1):
        x += f'and {y} are North European Countries'
    else:
        x += f"{y}, "
    
    return x

sent = reduce(reduce_func, countries, '')
# print(sent)

# - 12
import data

countries = data.countries

def categorize_decorator(fn):
    def wrapper(pattern):
        lst = fn(pattern)
        for i in countries:
            if (i.lower().startswith(pattern) or i.lower().endswith(pattern)):
                lst.append(i)
        return lst
    return wrapper

@categorize_decorator
def categorize_countries(pattern):
    lst = []
    return lst

# print(categorize_countries('land'))
# print(categorize_countries('ia'))
# print(categorize_countries('island'))
# print(categorize_countries('stan'))
# print(countries)


# - 13
def count_dict(x, y):
    start = y[0]

    if (x.get(f'{start}')):
        x[f"{start}"] += 1
    else:
        x[f"{start}"] = 1
    # x[f'{start}'] + 1 if x[f'{start}'] else x[f'{start}'] = 1

    return x

reduced_dict = reduce(count_dict, countries, {})

# print(reduced_dict) 


# - 14
def get_first_ten_countries(countries):
    return countries[:10]

# print(get_first_ten_countries(countries))


# - 15
def get_last_ten_countries(countries):
    return countries[-10:]

# print(get_last_ten_countries(countries))



# LEVEL 3
import json
import os
from operator import itemgetter

json_path = os.path.join(os.getcwd(), "data", "countries_data.json")
print("Json path", json_path)
with open(json_path, "r", encoding="utf-8") as json_data:
    countries_data = json.load(json_data)


# - 1
# Sort By Name
# names = sorted(countries_data, key=lambda x: x['name'])
# print(names)

# Sort By Capital
# capital = sorted(countries_data, key=lambda x: x['capital'])
# print(capital)

# Sort By Population
# population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
# print(population)


# - 2
# Most Spoken Languages
def lang_count(data):
    lang_dict = {}
    for obj in data:
        lang_lst = obj['languages']
        i = 0
        while i < len(lang_lst):
            if (lang_dict.get(f'{lang_lst[i]}')):
                lang_dict[f"{lang_lst[i]}"] += 1
            else:
                lang_dict[f"{lang_lst[i]}"] = 1
            i += 1
    return lang_dict

# lang = sorted(lang_count(countries).items(), key=lambda lang: lang[1], reverse=True)
# ten_most_spoken = dict(lang[:10])
# print(ten_most_spoken)



# - 3
# Most Populated
population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
most_populated = population[:10]
print(most_populated)



# ---------- DONE ----------