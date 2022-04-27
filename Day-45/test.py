import lxml
from bs4 import BeautifulSoup
with open("Day-45\website.html",encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
all_anchor_tags = soup.find_all(name="a")
all_paragraph_tags = soup.find_all(name="p")

# for tag in all_anchor_tags:
#     print(tag.getText("a"))

# for tag in all_anchor_tags:
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

# section_heading = soup.find(name="h3", class_= "heading")
# print(section_heading)

# compnay_url = soup.select_one(selector="p a")
# print(compnay_url)

