import mymodule
import os
import sys
from statistics import *


print(mymodule.generate_full_name('Odili', "Gerald"))

# OS Module
print(os.getcwd())
# print(os.mkdir('country_data'))
# print(os.chdir('country_data'))
# print(os.rmdir('country_data'))


# SYS Module
# print(sys.version)
# print(sys.path)
# print(sys.maxsize)
# sys.exit()

#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


# STATISTICS Module
age = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(age))
print(median(age))
print(stdev(age))
print(mode(age))




