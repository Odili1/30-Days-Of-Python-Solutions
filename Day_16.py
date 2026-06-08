# ----- PYTHON DATETIME -----
from datetime import datetime
now = datetime.now()
day = now.day
year = now.year
month = now.month
hour = now.hour
minute = now.minute
seconds = now.second
timestamp = now.timestamp()
# print('timestamp:', timestamp)
print(f'{day}/{month}/{year} {hour}:{minute}')

time_one = now.strftime('%d/%m/%Y, %H:%M:%S')
# print(time_one)

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, '%d %B, %Y')
# print("date_object =", date_object)


from datetime import time
a = time()
# print('a=', a)

b = time(10, 30, 50)
# print('time= ', b)


# ----- EXERCISE -----
# - 1
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

# - 2
formated_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print('formated_date', formated_date)

# - 3
string = '5 December, 2019'
time_string = datetime.strptime(string, '%d %B, %Y')
print('time_String', time_string)

# - 4
time_now = datetime(2024, 4, 16, 13, 29)
new_year = datetime(2025, 1, 1, 0, 0)
diff_time = new_year - time_now
print('time_diff', diff_time)

# - 5
old_time = '1 January 1970'
curr_time = datetime.now()

time_diff = curr_time - datetime.strptime(old_time, '%d %B %Y')
print('time-diff', time_diff)



# ---------- DONE ----------



