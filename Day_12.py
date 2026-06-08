# ----- MODULES -----
# --- Method 1
### my_module.py

# def greet(name):
#     print(f"Hello, {name}!")

# import my_module

# my_module.greet("John")


# ----- Method 2
# my_module/
#     __init__.py
#     greet.py

### my_module/__init__.py
# from .greet import greet

### my_module/greet.py
# def greet(name):
    # print(f"Hello, {name}!"


# import my_module
# my_module.greet("John")




# --- LEVEL 1 ---
from random import randint, shuffle
from math import *

alphaNum = [1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# - 1
# print(id)
def random_user_id():
    id = ""
    for i in range(6):
        id += str(alphaNum[randint(0, len(alphaNum) - 1)])

    return id

# print(random_user_id())

# - 2
def user_id_gen_by_user():
    userInput = input('Enter two integer value separated with space ').split(' ')

    len_of_id, num_of_id = userInput

    for j in range(int(num_of_id)):
        id = "#"
        for i in range(int(len_of_id)):
            id += str(alphaNum[randint(0, len(alphaNum) - 1)])

        print(id)
    
    return

# print(user_id_gen_by_user())

# - 3
def rgb_color_gen():
    arg1 = randint(0, 255)
    arg2 = randint(0, 255)
    arg3 = randint(0, 255)

    return f"rgb({arg1}, {arg2}, {arg3})"

print(rgb_color_gen())


# --- LEVEL 2 ---
# - 1
id = hex(floor(randint(0, 16777215)))
print(id)

def list_of_hexa_colors():
    num_of_hex = input('Enter the number of hexadecimal number needed ')

    hex_lst = []
    
    for i in range(int(num_of_hex)):
        hex_num = str(hex(floor(randint(0, 16777215))))
        # print(type(hex_num.split(" ")))

        hex_lst.append('#' + hex_num[2:])

    return hex_lst

# print(list_of_hexa_colors())

# - 2
def list_of_rgb_colors():
    num_of_hex = input('Enter the number of rgb colors number needed ')

    rgb_lst = []

    for i in range(int(num_of_hex)):
        arg1 = randint(0, 255)
        arg2 = randint(0, 255)
        arg3 = randint(0, 255)
        rgb_lst.append(f"rgb({arg1}, {arg2}, {arg3})")

    return rgb_lst

# print(list_of_rgb_colors())


# - 3
def generate_colors():
    userInput = input('Enter the type and number of color code needed. Separate with space ').split(' ')

    typeof, num = userInput

    lst = []
    if typeof == 'hexa':
        for i in range(int(num)):
            hex_num = str(hex(floor(randint(0, 16777215))))

            lst.append('#' + hex_num[2:])
        return lst
    elif typeof == "rgb":
        for i in range(int(num)):
            arg1 = randint(0, 255)
            arg2 = randint(0, 255)
            arg3 = randint(0, 255)
            
            lst.append(f"rgb({arg1}, {arg2}, {arg3})")
        return lst
    else:
        print('To choose type. use \'hexa\' or \'rgb\'')
        generate_colors()

# print(generate_colors())




# --- LEVEL 3 ---
# - 1
def shuffle_list(lst):
    shuffle(lst)
    return lst

# print(shuffle_list([1,2,3,4,5]))


# - 2
def unique_num():
    lst = []

    while len(lst) < 7:
        num = randint(0, 9)
        # print(num)
        if num in lst:
            continue
        lst.append(num)

    return lst

print(unique_num())


# ----- DONE -----