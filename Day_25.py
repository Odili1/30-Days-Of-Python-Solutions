# ----- PANDAS -----

import pandas as pd
import os

# 1
def read_hacker_news(filename):
    if os.path.exists(filename):
        hacker_news = pd.read_csv(filename)
    return hacker_news


hacker_news = read_hacker_news("./data/hacker_news.csv")


# 2
first_five_rows = hacker_news.head()
print("First Five Rows:\n", first_five_rows)


# 3
last_five_rows = hacker_news.tail()
print("Last Five Rows:\n", last_five_rows)


# 4
title_column = hacker_news.columns
print("Title Column:\n", list(title_column))


# 5
title_series = hacker_news["title"]
list_of_titles = list(title_series)
# i) 
python_in_title = list(filter(lambda title: "python" in title.lower(), list_of_titles))

print("Titles that contains Python:\n", python_in_title)

# ii)
javascript_in_title = list(filter(lambda title: "javascript" in title, list_of_titles))

print("Titles that contains javascript:\n", javascript_in_title)

# iii) 
data_description =  hacker_news.describe()
data_description['num_points'] = round(data_description['num_points'], 1)
data_description['num_comments'] = round(data_description['num_comments'], 1)

print("\nDescription:\n", data_description)


