import bs4
import requests

response = requests.get("https://news.ycombinator.com/news",)
web_page = response.text

soup = bs4.BeautifulSoup(web_page, "html.parser")

a = soup.find_all("h1", class_="storyline")
print(a)








# with open("website.html") as file:
#     data = file.read()
#
# soup = bs4.BeautifulSoup(data, "html.parser")
#
# print(soup.find("h1"))