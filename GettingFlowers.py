import requests
import xlsxwriter
from bs4 import BeautifulSoup

URL = "https://www.flowerglossary.com/types-of-flowers/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

starting_div = soup.findAll(attrs={"class": None})
h2_tags = soup.findAll("h2")
h3_tags = soup.findAll("h3")
flower_names = []
total_data = []
x = 0

for names in h3_tags:
    name_text = " ".join(names.text.split())
    if name_text != "Related posts:" and name_text != "Resources:":
        flower_names.append(name_text)



for j in starting_div:
    divs = j.findAll("div")
    for match in divs:
        specific = match.findAll(attrs={"class": None})
        for data in specific:
            flower_data = []
            if data.name == "p": 
                if data.find('span') is None and data.find("em") is None:
                    data_text = " ".join(data.text.split())
                    if data_text != "":
                        flower_data.append(data_text)
                    # if data.name == "ul":
            if data.name == "ul":
                for li_tag in data.findAll('li'):
                        if li_tag is not None:
                            li_text = " ".join(li_tag.text.split())
                            flower_data.append(li_text)
            if flower_data:
                total_data.append(flower_data)
# print(total_data)


workbook = xlsxwriter.Workbook('data_data.xlsx')
worksheet = workbook.add_worksheet()

for row_num, row_data in enumerate(total_data):
    worksheet.write(row_num, 0, row_data)
workbook.close()
        
            
            
                

# for i in soup.find("h2").next_siblings:
#     if i.name == "p" or i.name == "ul":
#         print(i)