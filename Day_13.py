# ----- LIST COMPREHENSION -----
numTpl = [(i, i * i) for i in range(11)]
numArr = [[i, i * i] for i in range(11)]
# print(numTpl)
# print(numArr)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_lst = [num for k in list_of_lists for num in k]

# print(flattened_lst)

# def add_two_nums(a, b):
#     return a + b

# print(add_two_nums(2, 3)) 

# print((lambda x: x)(3))


# add_two_nums = lambda a, b: a + b

# print(add_two_nums(2, 4))

def power(n):
    return lambda m: n ** m

# print(power(2)(3))


# --- LEVEL 1 ---
# - 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_lst = [i for i in numbers if i <=0]
# print(filtered_lst)

# - 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_lst = [num for irow in list_of_lists for row in irow for num in row]

# print(flatten_lst)


# - 3
power_up = [(i, i**0, i**1, i**2, i**3, i**4, i**5,) for i in range(11)]
# print(power_up)


# - 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_lst = [country for lst in countries for tpl in lst for country in tpl]
print(flat_lst)

newLst = []
i = 0
while i < len(flat_lst):
    first = flat_lst[i].upper()
    second = flat_lst[i][:3].upper()
    third = flat_lst[i + 1].upper()

    item = [first, second, third]

    newLst.append(item)

    i += 2

# print(newLst)
# output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


# - 5
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_lst = [country for lst in countries for tpl in lst for country in tpl]

newLst = []
i = 0
while i < len(flat_lst):
    Country = flat_lst[i].upper()
    city = flat_lst[i + 1].upper()

    item = {
        'country': f'{Country}',
        'city': f'{city}'
    }

    newLst.append(item)

    i += 2

# print(newLst)
# output:[{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]



# - 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

flat_lst = [name for lst in names for tpl in lst for name in tpl]

newLst = []
i = 0
while i < len(flat_lst):
    name1 = flat_lst[i]
    name2 = flat_lst[i + 1]

    item = name1 + ' ' + name2

    newLst.append(item)

    i += 2

print(newLst)
# output:['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']




# - 7
calculate_slope = lambda x, y: (x[0] - x[1])/(y[0] - y[1])
print(calculate_slope([1, 2], [1, 2]))




# ---------- DONE ----------