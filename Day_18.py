# ----- REGULAR EXPRESSION -----
import re
word = 'apple'
regex_pattern = rf'{word}' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'banana', 'apple', 'banana']


# ----- EXERCISE -----
#  - 1
import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


def most_frequent_word(paragraph):
    arr = []

    paragraph_set = set(re.split(r'\.? ', paragraph))
    print("paragraph set", paragraph_set)

    for word in paragraph_set:
        number_app = len(re.findall(f'{word}', paragraph))
        arr.append((number_app, word))

    return sorted(arr, key=lambda x: x[0], reverse=True)

# print(most_frequent_word(paragraph))


# - 2
sentence = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

def distance_apart(sent):
    regex_pattern = r'-?\d+'
    arr = re.findall(regex_pattern, sent)
    distance = int(arr[-1]) - int(arr[0])
    return distance

# print(distance_apart(sentence))


# --- LEVEL 2 ---
# - 1
def is_valid_variable(var):
    regexp = r'^[_a-zA-z]+[_a-zA-Z0-9]*$'
    match = re.match(regexp, var)

    return False if not match else True

# print(is_valid_variable('first_name')) # True
# print(is_valid_variable('first-name')) # False
# print(is_valid_variable('1first_name')) # False
# print(is_valid_variable('firstname')) # True


# ----- LEVEL 3 -----
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sent):
    replaced = re.sub(r'[$%@&;#]', '', sent)
    return replaced

print(clean_text(sentence))
print(most_frequent_word(clean_text(sentence)))



# ---------- DONE ----------

