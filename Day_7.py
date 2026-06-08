# ----- SETS -----
# set()


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# ---LEVEL 1 ---
# - 1
length = len(it_companies)
print(length)

# - 2
it_companies.add('Twitter')
print(it_companies)

# - 3
it_companies.update(["Tizeti", "Accelerex", "Interswitch"])
print(it_companies)

# - 4
it_companies.remove("IBM")
print(it_companies)

# - 5
# What is the difference between remove and discard

# --- LEVEL 2 ---
# - 1
joint = A.union(B)
print(joint)

# - 2
intersect = A.intersection(B)
print(intersect)

# - 3
print(A.issubset(B))

# - 4
print(A.isdisjoint(B))

# - 5
a_b = A.union(B)
b_a = B.union(A)
print(f"A with B {a_b} and B with A {b_a}")

# - 6
print(A.symmetric_difference(B))

# - 7
del A
del B


# ---LEVEL 3 ---
# - 1
age_set = set(age)
print(f"Length of set is {len(age_set)} and length of age is {len(age)}")

# - 2
# Explain the difference between the following data types: string, list, tuple and set


# - 3
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_lst = sentence.split(' ')
sentence_st = set(sentence_lst)
unique_words = len(sentence_st)

print("There are {} unique words and they are: {}".format(unique_words, ', '.join(list(sentence_st))))



# ----- DONE -----