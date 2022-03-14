from bs4 import BeautifulSoup
import requests
import lxml
response = requests.get("https://news.ycombinator.com/news")
yc_text = response.text

soup = BeautifulSoup(yc_text,"lxml")
articals = soup.find_all(name="a", class_="titlelink")
artical_texts = []
artical_links = []
for article_tag in articals:
    text = article_tag.getText()
    artical_texts.append(text)
    link = article_tag.get("href")
    artical_links.append(link)


artical_upvotes = [int(score.getText().split()[0]) for score in  soup.find_all(name="span", class_="score")]
largest_number = max(artical_upvotes)
largest_index = artical_upvotes.index(largest_number)
print(artical_texts[largest_index])
print(artical_links[largest_index])


