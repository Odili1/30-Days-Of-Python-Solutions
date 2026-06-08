# ----- LISTS -----
# list() or []


#  - 1
# lst = list()
# print(lst)

# - 2
# lst2 = list([6, 'true', True, 5.5, {"name": "odili"}])
# print(lst2)

# - 3
# print(len(lst2))

# - 4
# first_item = lst2[0]
# middle_item = lst2[len(lst2)//2]
# last_item = lst2[-1]

# print(f'first {first_item}, middle {middle_item} and last {last_item}')

# - 5
# mixed_data_types = list(["dili", 19, 5.11, "single", "Akim Barracks"])


# - 6
it_companies = list(["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"])

# - 7
# print(it_companies)

# - 8
# print(len(it_companies))

# - 9
# first_item = it_companies[0]

# - 10
# it_companies[3] = "Interswitch"
# print(it_companies)

# - 11
it_companies.append("Andela")

# - 12
it_companies.insert(len(it_companies)//2, "Twitter")

# - 13
# upper = it_companies[2].upper()
# print(upper)

# - 14
# joining = '# '.join(it_companies)
# print(joining)

# - 15
# exist = 'Interswitch' in it_companies
# print(exist)

# - 16
# it_companies.sort()
# print(it_companies)

# - 17
# it_companies.reverse()
print(it_companies)

# - 18
firt_three = it_companies[:3]
print(firt_three)

# - 19
last_three = it_companies[-3:]
print(last_three)

# - 20
middle_commpanies = it_companies[len(it_companies)//2: len(it_companies)//2 + 1]
print(middle_commpanies)

# - 21
it_companies.pop(0)
print(it_companies)

# - 22
it_companies.pop(len(it_companies)//2)

# - 23
it_companies.pop(-1)
print(it_companies)

# - 24
it_companies.clear()
print(it_companies)

# - 25
del it_companies
# print(it_companies)

# - 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

# - 27
full_stack = front_end.copy()
newItems = ["Python", "SQL"]
i = 1
for item in newItems:
    full_stack.insert(full_stack.index('Redux') + i, item)
    i += 1

print(full_stack)



# --- LEVEL 2 ---
# - 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

# - i)
minAge = ages[0]
maxAge = ages[-1]
print(minAge, maxAge)

# - ii)
newAges = [minAge, maxAge]
i = 1

for age in newAges:
    ages.append(age)
    i += 1

print(ages)

# - iii)
median = ages[len(ages) // 2]
print(median)

# - iv)
avg = sum(ages)/2
print(avg)

# - v)
rang = maxAge - minAge
print(rang)

# - vi)
compare1 = abs(minAge - avg)
compare2 = abs(maxAge - avg)
print(f'This is a comparison between compare1 {compare1} and compare2 {compare2}')



# --- LEVEL 3 ---
from data import countries

# - 1
middle_country = countries[len(countries)//2]
# print(middle_country)

# - 2
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:len(countries)//2]
del countries[:len(countries)//2]
if len(countries) % 2 != 0:
    first_half.append("Aquaman")

# print(f'First Half {first_half} \n Second Half {countries}')
# - 3
# asian = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# first, second, third, *scandic = asian
# print(first, second, third, scandic)
    

# ---------- DONE ----------