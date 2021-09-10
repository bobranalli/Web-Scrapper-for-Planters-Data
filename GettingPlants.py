import requests
import xlsxwriter
from bs4 import BeautifulSoup

URL = "http://www.gardening.cornell.edu/homegardening/scenee139.html"
base_url = "http://www.gardening.cornell.edu/homegardening/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

normal_div = soup.findAll("div", {"class": "normal"})

my_plants = []
array_of_plants = []
# links = ["scenea5d2.html", "scene8ada.html", "scene2f17.html"]

time = 0

for i in normal_div:
    a_link = i.findAll('a')
    b_link = i.findAll('b')
for common in b_link:
    if common is not None:
        b_title = common.text
        if b_title == "By common name:":
            for x in a_link:
                plant_headers = []
                current_link = x['href']
                soup = BeautifulSoup(requests.get(base_url + current_link).content, "html.parser")
                header_name = soup.find("div", {"class": "head2"})
                plant_text = " ".join(header_name.text.split())
                plant_headers.append(plant_text)

                plant_info = soup.findAll("div", {"class": "intro"})

                for info in plant_info:
                    ps = info.findAll('p')
                    for p_tags in ps:
                        for child in p_tags.children:
                            if child.name == "b":
                                p_tags_clean = " ".join(p_tags.text.split())
                                plant_headers.append(p_tags_clean)
                            if child.next_element.name == "ul":
                                for li_tag in child.next_element.findAll('li'):
                                    if li_tag is not None:
                                        square_info = " ".join(li_tag.text.split())
                                        print(square_info)
                                        # plant_headers.append(square_info)
                                
                    # p_info = " ".join(info.text.split())
                    # if p_info != "Varieties":
                                
                    

                # for ul_tag in soup.findAll("ul", {"type": "square"}):
                #     for li_tag in ul_tag.findAll('li'):
                #         if li_tag is not None:
                #             square_info = " ".join(li_tag.text.split())
                #             plant_headers.append(square_info)
                
                array_of_plants.append(plant_headers)


workbook = xlsxwriter.Workbook('flowers_data.xlsx')
worksheet = workbook.add_worksheet()

for row_num, row_data in enumerate(array_of_plants):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)

workbook.close()