from urllib import response
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_contet = response.text

soup = BeautifulSoup(website_contet, "lxml")
all_movies = soup.find_all(name="h3" ,class_ ="title")
# print(all_movies)
movie_title = [movie.getText() for movie in all_movies]
# print(movie_title)
movie_list = movie_title[::-1]
print(movie_list)


with open("movie.txt", mode= "w") as file:
    for movies in movie_list:
        file.write(f"{movies}\n")