# INTRODUCTION

# LEVEL 3
# - 1
int_num = 5
float_num = 5.5
comp_num = 1 + 2j
string_name = "Odili1"
bool_val = True
int_lst = [1,2,3,4,5]
int_tpl = (2,3,4,5,6)
int_set = {2,4,5,6,7,8,8}
info_dct= {
    "name": "Odili",
    "age": 27,
    "country": "Nigeria",
    "languages": ["Typescript", "Python", "C-sharp", "Go"]
}

print(int_lst)
print(int_tpl)
print(int_set)
print(info_dct)

# - 2 
# Find an Euclidian distance between (2, 3) and (10, 8)
import math
def euclidianDistance(a, b):
    x1, x2, y1, y2 = a[0], b[0], a[1], b[1]
    
    # Formula -> Math.Root((x2-x1)**2 + (y2-y1)**2)
    x = (x2 - x1) ** 2
    y = (y2- y1) ** 2

    dist = math.sqrt((x + y))
    return dist




print(euclidianDistance((2,3), (10,8)))


# ----- DONE -----