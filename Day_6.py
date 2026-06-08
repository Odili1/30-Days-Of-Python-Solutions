# ----- TUPLES -----
# tuples() or ()


# --- LEVEL 1 ---
# - 1
empty_tuple = ()

# - 2
sisters = ("Chisom", "Chioma", "Miracle")
brothers = ("Sosi", "Dommy", "Cojoe")

# - 3
siblings = sisters + brothers
print(siblings)

# - 4
num_of_siblings = len(siblings)
print(num_of_siblings)

# - 5
parents = ["Mummy", "Daddy"]
siblings_to_list = list(siblings)
siblings_to_list.extend(parents)
family_members = tuple(siblings_to_list)
print(family_members)


# --- LEVEL 2 ---
# - 1
# *siblings, parents = family_members

# print(parents)

# - 2
fruits = ("mango", "banana", "Pineapple")
vegetables = ("utazi", "ugu", "nchuawu")
animal_products = ("fish", "meat", "milk")

food_stuff_tp = fruits + vegetables + animal_products

# - 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp, food_stuff_lt)

# - 4
middle_item = food_stuff_lt[len(food_stuff_lt)//2: len(food_stuff_lt)//2 + 1]
print(middle_item)

# - 5
first_item = food_stuff_lt[:3]
last_item = food_stuff_lt[-3:]
print(first_item, last_item)

# - 6
del food_stuff_tp
# print(food_stuff_tp)

# - 7 
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


# ---------- DONE ----------