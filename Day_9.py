# ----- CONDITIONALS -----
# --- LEVEL 1 ---
# - 1
# user_age = input('Enter your age ')

# if int(user_age) >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     print(f'You need {abs(int(user_age) - 18)} more years to learn to drive.')

# - 2
# your_age = 25
# my_age = int(input('Enter your age '))

# if my_age > your_age:
#     if abs(my_age - your_age) > 1:
#         print(f'I am {abs(int(my_age) - your_age)} years older than you')
#     else:
#         print(f'I am {abs(int(my_age) - your_age)} year older than you')
# elif your_age > my_age:
#     if abs(your_age - my_age) > 1:
#         print(f'You are {abs(int(your_age) - my_age)} years older than me')
#     else:
#         print(f'You are {abs(int(my_age) - your_age)} year older than me')
# else:
#     print('We are age mates')


# - 3
# a = int(input('Enter number one '))
# b = int(input('Enter number two '))

# if a > b:
#     print('a is greater b')
# elif a < b:
#     print('a is smaller than b')
# else:
#     print('a is equal to b')


# --- LEVEL 2 ---
# - 1
# score = int(input('Enter Score '))

# if score >= 80 and score <= 100:
#     print('A')
# elif score >= 70 and score <= 89:
#     print('B')
# elif score >= 60 and score <= 69:
#     print('C')
# elif score >= 50 and score <= 59:
#     print('D')
# elif score >= 0 and score <= 49:
#     print('F')
# else:
#     print('Input a proper score between 0 - 100')

# - 2
# month = input('Enter current month ').lower()

# if month == 'september' or month == 'september' or month == 'september':
#     print('Autumn')
# if month == 'december' or month == 'january' or month == 'february':
#     print('Winter')
# if month == 'march' or month == 'april' or month == 'may':
#     print('Spring')
# if month == 'june' or month == 'july' or month == 'august':
#     print('Summer')

# - 3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(f'Fruits in the fridge {fruits}')
# affirm = input('Want to add a fruit? (Y/N) ').lower()
# n = 1

# if affirm == 'y':
#     while n:
#         new_fruit = input('Add a fruit ')

#         if new_fruit in fruits:
#             print(f'{new_fruit} already exists in the fridge. \n Add something else')
#         else:
#             fruits.append(new_fruit)
#             print(f'Fruits in the fridge {fruits} \n Fridge closed')
#             n = 0
# elif affirm == 'n':
#     print('Alright, fridge closed')
#     n = 0
# else:
#     print('Cannot understand command')
#     n = 0


# --- LEVEL 3 ---
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# - 1
if person['skills']:
    middle_skill = person['skills'][len(person['skills'])//2]
    print(middle_skill)

# - 2
if person['skills']:
    if 'Python' in person['skills']:
        print(person['skills'][person['skills'].index('Python')])


# - 3
if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif len(person['skills']) == 3 and 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend end developer')
elif 'React' in person['skills'] and 'Node' in person['skills']and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')
    

# - 4
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")


# ----- DONE -----
