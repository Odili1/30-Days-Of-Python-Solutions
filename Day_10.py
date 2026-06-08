# ----- LOOPS -----
# --- LEVEL 1 ---
# - 1
# for i in range(10):
#     print(i, end='')

# i = 0
# while i <= 10:
#     print(i, end='')
#     i += 1


# - 2
# for i in range(10, 0, -1):
#     print(i, end='\n')

# i = 10
# while i >= 0:
#     print(i, end='')
#     i -= 1

# - 3
# h = '#'
# for i in range(7):
#     print(h)
#     h += '#'

# - 4

# for i in range(8):
#     h = '#'
#     for j in range(8):
#         h += ' #'
#     print(h)


# - 5
# for i in range(11):
#     print(f'{i} X {i} = {i*i}')

# - 6
# number = int(input('What table on the times table? '))

# for i in range(13):
#     print(f'{number} x {i} = {number*i}')

# - 7
# lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for i in lst:
#     print(i)


# - 8
# for i in range(0, 100, 2):
#     print(i, end=' ')

# # - 9
# for i in range(1, 100, 2):
#     print(i, end=' ')



# --- LEVEL 2 ---
# - 1
# num = 0
# for i in range(101):
#     num += i
# print(num)


# - 2
odd = 0
even = 0

for i in range(101):
    if i % 2 == 0:
        even += i
    else:
        odd += i

# print(f"The sum of all evens is {even}. Add the sum of all odds is {odd}")


# --- LEVEL 3 ---
# - (1) Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# import sys
# sys.path.append('/data')

import data
import json
import os
from operator import itemgetter
# from data import countries_list
countries = data.countries
json_path = os.path.join(os.getcwd(), "data", "countries_data.json")
print("Json path", json_path)
with open(json_path, "r", encoding="utf-8") as json_data:
    countries_data = json.load(json_data)
    


land = []
for country in countries:
    if not 'land' in country:
        continue
    land.append(country)
else: 
    print(land)


# (2) This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
lst = ['banana', 'orange', 'mango', 'lemon']

newLst = []
for index in range(1, len(lst) + 1):
    newLst.append(lst[-index])
else:
    print(newLst)


# (3) Go to the data folder and use the countries-data.py file.
#   (i) What are the total number of languages in the data
lang_count = 0
for country in countries_data:
    lang_count += len(country["languages"])
else:
    print(lang_count)

#   (ii) Find the ten most spoken languages from the data
lang_dict = {}
for countries in countries_data:
    for lang in countries["languages"]:
        if lang_dict.get(lang):
            lang_dict[lang] += 1
        else:
            lang_dict[lang] = 1


lang_list = [(language, count) for language, count in lang_dict.items()]
sorted_lang_list = sorted(lang_list, key=lambda index: index[1], reverse=True)
ten_most_spoken_lang_list = sorted_lang_list[:10]
ten_most_spoken_lang = [lang for lang_tpl in sorted_lang_list[:10] for lang in lang_tpl if type(lang) == str]
print("Ten Most Spoken Languages List Count", ten_most_spoken_lang_list)
print("Ten Most Spoken Languages", ten_most_spoken_lang)


#   (iii) Find the 10 most populated countries in the world
population_dict = {}
for country in countries_data:
    population_dict[country["name"]] = country["population"]


population_list = [(name, population) for name, population in population_dict.items()]

sorted_population_list = sorted(population_list, key=itemgetter(1), reverse=True)

ten_most_populated_list = sorted_population_list[:10]
ten_most_populated = [country for country_tpl in sorted_population_list[:10] for country in country_tpl if type(country) == str]

print("Ten Most Populated List Count", ten_most_populated_list)
print("Ten Most Populated", ten_most_populated)






# ---------- DONE ----------


