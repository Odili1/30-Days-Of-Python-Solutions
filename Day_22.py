# ----- WEB SCRAPING -----
import requests
from bs4 import BeautifulSoup

url = 'https://odili1.github.io/Rest_Countries_Api/index.html'

# reponse = requests.get(url)
# status = reponse.status_code
# content = reponse.content

# soup = BeautifulSoup(content, 'html.parser')
# print(reponse.content)
# print(soup.title)
# print(soup.body)
# options = soup.find_all('option')
# for op in options:
#     print(op.text)
#     print(op['value'])

# print(options)



# ---------- EXERCISE ----------

# 1)
url = 'https://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
status = response.status_code
# content = response.content
content = response.text

# with open("./files/boston_university_facts.html", "w", encoding="utf-8") as file:
#     file.write(content)
soup = BeautifulSoup(content, 'html.parser')
# print(soup)
# print(soup.body.prettify())
# print(soup.find_all('a', 'level_1'))

main_data_dict = {}


key = ''
value = ''

        
def scrap_facts_stats_data():
    title = soup.find_all('section', 'facts-stats')[0].contents[1].contents[1].string
    print("TItle: ", title)

    data = {}

    scrap = soup.find_all('div', 'text')
    for level_1 in range(1, len(scrap)):
    # print(scrap[level_1].contents)
        for level_2 in range(len(scrap[level_1].contents)):
            if level_2 == 3:
                value = scrap[level_1].contents[level_2].string
                # print(value)
            if level_2 == 5:
                key = scrap[level_1].contents[level_2].string
                # print(key)
                
                data[f'{key}'] = value

    main_data_dict[f'{title}'] = data

scrap_facts_stats_data()
print(main_data_dict)




# ------------------ [1, 2, 3] --------------------