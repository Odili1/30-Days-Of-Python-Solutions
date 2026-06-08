# ----- FILE HANDLING -----
file = open('./files/reading_file_example.txt')
# with open('./files/reading_file_example.txt') as file:

# read
# read = file.read()
# print(type(read))
# print(read)
# file.close()

# readline
# line = file.readline()
# print(type(line))
# print(line)

# readlines
# lines = file.readlines()
lines = file.read().splitlines()
# print(type(lines))
# print(lines)

# Append to file
# with open('./files/reading_file_example.txt', 'a') as file:
#     file.write('This file has been appended at the end')

# Creates a new file if it does not exist
# with open('./files/writing_file_example.txt', 'w') as file:
#     file.write('This text will be written in  newly created file')


# Delete files
# import os
# if (os.path.exists('./files/writing_file_example.txt')):
#     os.remove('./files/writing_file_example.txt')
# else:
#     print('This file does not exist')
    

# JSON Files
# JSON -> Dict
import json
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

# person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'])

# Dict -> JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

# person_to_json = json.dumps(person, indent=3)
# print(type(person_to_json))
# print((person_to_json))

# Saving to a json file
# with open('./files/json_example.json', 'w') as f_json:
#     json.dump(person, f_json, ensure_ascii=False, indent=3)


# CSV Extension
import csv
with open('./files/csv_example.csv') as f_csv:
    csv_reader = csv.reader(f_csv, delimiter=',')
    # print(csv_reader)
    line_count = 0

    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Columns names are: {','.join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}')
            line_count += 1

    print(f'Number of lines: {line_count}')


# XML Extension
import xml.etree.ElementTree as ET

# tree = ET.parse('./files/xml_example.xml')
# print(type(tree))
# print(tree)
# root = tree.getroot()
# print('Root tag: ', root.tag)
# print('Attribute: ', root.attrib)
# for child in root:
#     print('child: ', child.tag)




# ----- LEVEL 1 -----
# 1
# a) Obama_speech
file = open('./data/obama_speach.txt')
num_words = len(file.read().split(' '))
file.close()

file = open('./data/obama_speach.txt')
num_of_lines = len(file.readlines())
file.close()
# print(f'Obama\nwords: {num_words}\n lines: {num_of_lines}')

# b) Michelle_Obama_speech
file = open('./data/michelle_obama_speech.txt')
num_words = len(file.read().split(' '))
file.close()

file = open('./data/michelle_obama_speech.txt')
num_of_lines = len(file.readlines())
file.close()
# print(f'\n Michelle\nwords: {num_words}\n lines: {num_of_lines}')

# c) Donald_trump_speech
file = open('./data/donald_trump.txt')
num_words = len(file.read().split(' '))
file.close()

file = open('./data/donald_trump.txt')
num_of_lines = len(file.readlines())
file.close()
# print(f'\n Donald\nwords: {num_words}\n lines: {num_of_lines}')

# d) Melina_trump
file = open('./data/melina_trump.txt')
num_words = len(file.read().split(' '))
file.close()

file = open('./data/melina_trump.txt')
num_of_lines = len(file.readlines())
file.close()
# print(f'\nMelina\nwords: {num_words}\n lines: {num_of_lines}')


# - 2
import json
import os
from functools import reduce


def most_spoken_languages(num, filename):
    def reduce_func(x, y):
        for lang in y['languages']:
            if lang in x:
                x[lang] += 1
            else:
                x[lang] = 1
        
        return x
    
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            countries_data = json.load(f)

    lang_dct = reduce(reduce_func, countries_data, {})
    tpl_arr = list(lang_dct.items())

    sorted_arr = sorted(tpl_arr, key=lambda x: x[1], reverse=True)[0:num+1]
    
    # def interchange_position(lang_tpl):
    #     lang, count = lang_tpl
    #     return (count, lang)
    
    return list(map(lambda lang_tpl: (lang_tpl[1], lang_tpl[0]), sorted_arr))

# print(most_spoken_languages(10, filename='./data/countries_data.json'))


# - 3
def most_populated_countries(num, filename):
    def reduce_func(x, y):
        country = y['name']
        population = y['population']

        x.append({"country": country, "population": population})
        
        return x
    

    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            countries_data = json.load(f)

    population_dct = reduce(reduce_func, countries_data, [])
    sorted_arr = sorted(population_dct, key=lambda x: x['population'], reverse=True)[0:num]
    return sorted_arr


# print(most_populated_countries(3, filename='./data/countries_data.json'))



# ---- LEVEL 2 ----
import re
from data.stop_words import stop_words
# --------- GLOBAL FUNCTIONS -----------
def clean_sentence(sentence):
    # pattern = r'[,.\[\]\"\"-_\']'
    pattern = r'[^A-Za-z \n]'
    cleaned_sentence = re.sub(pattern, '', sentence)
    # print(cleaned_sentence)

    return cleaned_sentence


def remove_support_words(sentence):
    lst_of_words = re.split(r' |\n', sentence)
    filtered_words = [word for word in lst_of_words if word.lower() not in stop_words]
    # print("Removed Stop Words: ", filtered_words)
    # print("Removed Stop Words: ", " ".join(filtered_words))

    return " ".join(filtered_words)


def check_text_similarity(first_text, second_text):
    intersection = first_text.intersection(second_text)
    union = first_text.union(second_text)

    similarity = len(intersection)/len(union)

    return similarity * 100


# ---------- END OF GLOBAL FUNCTIONS ---------------


# - 1
def incoming_email_addresses(filename):
    if os.path.exists(filename):
        file = open(filename)
        texts = file.read()
        
        file.close()
    
    email_position_pattern = r'From [a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    extract_sentence = re.findall(email_position_pattern, texts)
    extract_email = list(map(lambda x: x.replace("From ", ""), extract_sentence))
    unique_emails = list(set(extract_email))
    
    return unique_emails


print(incoming_email_addresses("./data/email_exchanges_bid.txt"))


# - 2
def find_most_common_words(filename, num):
    if os.path.exists(filename):
       file = open(filename)
       words = file.read()
       file.close()

    pattern = r'[,.]'
    clean_sentence = re.sub(pattern, '', words)
    print(clean_sentence)
    lst_of_words = re.split(r' |\n', clean_sentence)
    print(lst_of_words)

    def reduce_func(x, y):
        if y in x and not y == '':
            x[y] += 1
        else:
            x[y] = 1
        
        return x
    
    words_dct = reduce(reduce_func, lst_of_words, {})
    tpl_arr = list(map(lambda x: (x[1], x[0]), list(words_dct.items())))

    sorted_arr = sorted(tpl_arr, key=lambda x: x[0], reverse=True)[0:num+1]

    return sorted_arr


# print(find_most_common_words('./files/reading_file_example.txt', 5))


# - 3
def find_most_frequent_words(filename, num, owner):
    if os.path.exists(filename):
       file = open(filename)
       words = file.read()
       file.close()
       

    cleaned_sentence = clean_sentence(words)
    lst_of_words = re.split(r' |\n', cleaned_sentence)
    print(lst_of_words)

    def reduce_func(x, y):
        if y in x and not y == '':
            x[y] += 1
        else:
            x[y] = 1
        
        return x
    
    words_dct = reduce(reduce_func, lst_of_words, {})
    tpl_arr = list(map(lambda x: (x[1], x[0]), list(words_dct.items())))

    sorted_arr = sorted(tpl_arr, key=lambda x: x[0], reverse=True)[0:num+1]

    return f"{owner}'s Speech:\n{sorted_arr}"


# A)
# print(find_most_frequent_words('./data/obama_speach.txt', 10, "Obama"))


# B)
# print(find_most_frequent_words('./data/michelle_obama_speech.txt', 10, "Michelle"))


# C)
# print(find_most_frequent_words('./data/donald_trump.txt', 10, "Trump"))


# D)
# print(find_most_frequent_words('./data/melina_trump.txt', 10, "Melina"))


# - 4
def check_speech_similarity(first_file, second_file):
    if os.path.exists(first_file):
        file = open(first_file)
        first_words = file.read()
        file.close()
    
    if os.path.exists(second_file):
        file = open(second_file)
        second_words = file.read()
        file.close()

    # Clean Sentence
    cleaned_first_words = clean_sentence(first_words).strip()
    cleaned_second_words = clean_sentence(second_words).strip()

    # Remove Stop Words
    first_words_without_stop_words = set(remove_support_words(cleaned_first_words).split())
    second_words_without_stop_words = set(remove_support_words(cleaned_second_words).split())
    # print("First Words", first_words_without_stop_words)
    # print("Second Words", second_words_without_stop_words)
    
    # Check percentage similarity
    get_similarity = check_text_similarity(first_words_without_stop_words, second_words_without_stop_words)

    return "Both speeches are {:.2f}% similar".format(get_similarity)




print(check_speech_similarity('./data/michelle_obama_speech.txt', './data/melina_trump.txt'))



# - 5
def find_most_frequent_words_romeo(filename, num):
    if os.path.exists(filename):
       file = open(filename)
       words = file.read()
       file.close()

    cleaned_sentence = clean_sentence(words).strip()
    lst_of_words = re.split(r' |\n+', cleaned_sentence)
    print(lst_of_words)

    def reduce_func(x, y):
        if y in x and not y == '':
            x[y] += 1
        else:
            x[y] = 1
        
        return x
    
    words_dct = reduce(reduce_func, lst_of_words, {})
    tpl_arr = list(map(lambda x: (x[1], x[0]), list(words_dct.items())))

    sorted_arr = sorted(tpl_arr, key=lambda x: x[0], reverse=True)[0:num+1]

    return sorted_arr


# print(find_most_frequent_words_romeo('./data/romeo_and_juliet.txt', 10))


# - 6
import csv
# A)
def read_csv_python(filename):
    pattern = r'[pP]ython'
    if os.path.exists(filename):
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 1:
                    print(row)
                if re.search(pattern, ', '.join(row)):
                    line_count += 1

    return f'Number of lines containing python or Python {line_count}'


print(read_csv_python('./data/hacker_news.csv'))

# B)
def read_csv_javasrcipt(filename):
    pattern = r'[jJ]ava[sS]cript'
    if os.path.exists(filename):
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if re.search(pattern, ', '.join(row)):
                    line_count += 1
            
    return f'Number of lines containinf JavaScript or javasript or Javascript is {line_count}'


print(read_csv_javasrcipt('./data/hacker_news.csv'))


# C)
def read_csv_java(filename):
    pattern = r'\b[jJ]ava\b'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if re.search(pattern, ', '.join(row)):
                    line_count += 1

    return f'Number of lines containing Java not javascript is {line_count}'

print(read_csv_java('./data/hacker_news.csv'))

import requests
# response = requests.get('https://jsonplaceholder.typicode.com/todos/3')
# todos = json.loads(response)
# print(response.text)






# ---------- DONE  ----------