# ----- PYTHON PACKAGE MANAGER -----

import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    # 'http://www.python.org',
    # 'https://www.linkedin.com/in/asabeneh/',
    # 'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)


import requests
import json

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

# response = requests.get(url)
# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json())

url = 'https://restcountries.eu/rest/v2/all'

# response = requests.get(url)
# print(response.status_code)
# print(response.json())



# ----- EXERCISE -----
# - 1
def url_romeo_and_juliet(url):
    # response = requests.get(url)
    # texts = response.text
    # print(texts)
    return 0
# Invalid URL
# print(url_romeo_and_juliet('http://www.gutenberg.org/files/1112/1112.txt'))


# - 2
# A)
def info_to_list(url, query):
    lst = []
    response = requests.get(url)
    # print("RESPONSE\n", response)
    data = response.json()
    # print("JSON DATA\n", data)
    # with open("./files/cat_breeds.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)
    if query == 'weight':
        for cat in data:
            weight = cat['weight']['metric'].split(' - ')[1]
            lst.append(int(weight))
    elif query == 'lifespan':
         for cat in data:
            life_span = cat['life_span'].split(' - ')[1]
            lst.append(int(life_span))

    
    # print(int(wt))
    return lst

lst_of_weights = info_to_list('https://api.thecatapi.com/v1/breeds', 'weight')

# MIN
min_weight = min(lst_of_weights)
# print(f'minimum weight => {min_weight}')

# MAX
max_weight = max(lst_of_weights)
# print(f'maximum weight => {max_weight}')

# MEAN
mean_weight = sum(lst_of_weights) / len(lst_of_weights)
# print(f'mean weight => {mean_weight}')

# MEDIAN
len_of_lst = len(lst_of_weights)
sorted_lst = sorted(lst_of_weights)

if len_of_lst % 2 == 0:
    median_weight = sorted_lst[len_of_lst / 2]
elif len_of_lst % 2 != 0:
    first_num = sorted_lst[len_of_lst // 2]
    second_num = sorted_lst[(len_of_lst // 2) + 1]
    median_weight = (first_num + second_num) / 2

# print(f'medain weight => {median_weight}')

# STANDARD DEVIATION
import math
len_of_lst = len(lst_of_weights)
sum_of_squares = 0

for weight in lst_of_weights:
    deviation = abs(weight - mean_weight)
    sum_of_squares += deviation ** 2

standard_deviation = math.sqrt(sum_of_squares / len_of_lst)

# print(f'weight standard deviation => {standard_deviation}')



# B)
lst_of_life_span = info_to_list('https://api.thecatapi.com/v1/breeds', 'lifespan')

# MIN
min_life_span = min(lst_of_life_span)
# print(f'minimum life span => {min_life_span}')

# MAX
max_life_span = max(lst_of_life_span)
# print(f'maximum life span => {max_life_span}')

# MEAN
mean_life_span = sum(lst_of_life_span) / len(lst_of_life_span)
# print(f'mean life span => {mean_life_span}')

# MEDIAN
len_of_lst = len(lst_of_life_span)
sorted_lst = sorted(lst_of_life_span)

if len_of_lst % 2 == 0:
    median_life_span = sorted_lst[len_of_lst / 2]
elif len_of_lst % 2 != 0:
    first_num = sorted_lst[len_of_lst // 2]
    second_num = sorted_lst[(len_of_lst // 2) + 1]
    median_life_span = (first_num + second_num) / 2

# print(f'median life span => {median_life_span}')

# STANDARD DEVIATION
import math
len_of_lst = len(lst_of_life_span)
sum_of_squares = 0

for life_span in lst_of_life_span:
    deviation = abs(life_span - mean_life_span)
    sum_of_squares += deviation ** 2

standard_deviation = math.sqrt(sum_of_squares / len_of_lst)

# print(f'life span standard deviation => {standard_deviation}')



# C)
from functools import reduce
def frequency_table(url):
    response = requests.get(url)
    data = response.json()
    
    def freq_table_dct(x, y):
        country = y['origin']
        if country in x:
            x[country] += 1
        else:
            x[country] = 1

        return x
    

    freq_dct = reduce(freq_table_dct, data, {})
    print(f'Country\t\tNo. of Breed')

    for key in freq_dct:
        print(f'{key}\t\t{freq_dct[key]}')
    return freq_dct

# print(frequency_table('https://api.thecatapi.com/v1/breeds',))



# - 3)
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(url)
content = response.text
# content = response.content

# with open("./files/bs_parsed_data.html", "w", encoding="utf-8") as file:
#     file.write(content)
# print(content)
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
# print(soup.body)




# ---------- DONE ----------