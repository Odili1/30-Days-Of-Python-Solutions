# ----- STRINGS -----
# - 1
# 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
# string = 'Thirty ' + 'Days ' + 'of ' + 'Python'
# print(string)

# - 2
# 'Coding', 'For' , 'All' to a single string, 'Coding For All'
string = "Coding " + 'for ' + "All"
# print(string)

# - 3
company = "Coding For All"

# - 4
# print(company)

# - 5
# print(len(company))

# - 6
uppercase = company.upper()
# print(uppercase)

# - 7
lowerCase = company.lower()
# print(lowerCase)

# - 8
# print(company.capitalize())
# print(company.title())
# print(company[company.find('Coding'): company.rfind('Coding') + len('coding')])
# print(company.swapcase())

# - 9
# print(company[company.find('Coding'): company.rfind('Coding') + len('coding')])

# - 10
# print(company.index('Coding'))
# print(company.find('Coding'))
# print(company.count('Coding'))

# - 11
replaced = company.replace('Coding', 'Python')
# print(replaced)

# - 12
replaced = replaced.replace('All', 'Everyone')
# print(replaced)

# - 13
# print(company.split(' '))

# - 14
# print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# - 15
# print(company[0])

# - 16
# print(len(company) - 1)

# - 17
# print(company[10])

# - 18
acron = f'{replaced[replaced.find('Python')]}{replaced[replaced.find('For')]}{replaced[replaced.find('Everyone')]}'
# print(acron)

#  - 19
acronym = f'{company[company.find('Coding')]}{company[company.find('For')]}{company[company.find('All')]}'
# print(acronym)

# - 20
# print(company.index('Coding'))

# - 21
# print(company.index('For'))

# - 22
# print(company.rfind('l'))

# - 23
# 'You cannot end a sentence with because because because is a conjunction'
because = 'You cannot end a sentence with because because because is a conjunction'
# print(because.find('because'))

# - 24
# print(because.rfind('because'))

# - 25
slicedStr = because[because.find('because'): because.rfind('because') + len('because')]
# print(slicedStr)


# - 26
# print(because.find('because'))

# - 27
slicedStr = because[because.find('because'): because.rfind('because') + len('because')]
# print(slicedStr)

# - 28
# print(company.startswith('Coding'))

# - 29
# print(company.endswith('Coding'))

# - 30
newString = ' Coding For All '
# print(newString.strip())

# - 31
'30DaysOfPython'.isidentifier()
'thirty_days_of_python'.isidentifier()

# - 32
pyLib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# - 33
newLine = 'I am enjoying this challenge.\nI just wonder what is next.'
print(newLine)

# - 34
print('Names\tAge\tCountry\tCity'.expandtabs(15))
print('Asabeneh\t250\tFinland\tHelsinki'.expandtabs(15))

# - 35
radius = 10
area = 3.14 * radius ** 2
area = f'The area of a circle with radius {radius} is {area} meters square.'
print(area)

# - 36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))



# ----- DONE -----