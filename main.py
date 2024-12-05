import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

r = requests.get("https://habr.com/ru/all/")  # https://habr.com/ru/articles/

soup = BeautifulSoup(r.text, 'html.parser')
for s in soup.find_all("article", {"class": "tm-articles-list__item"}):
    link = "https://habr.com" + s.find("a", {"class": "tm-title__link"})["href"]
    localr = requests.get(link)
    localsoup = BeautifulSoup(localr.text, "html.parser")
    article = localsoup.find("article",
                             {"class": "tm-article-presenter__content tm-article-presenter__content_narrow"})
    for keyword in KEYWORDS:
        if article.text.find(keyword) != -1:
            date = localsoup.find("time")["title"]
            name = localsoup.find("h1", {"class": "tm-title tm-title_h1"}).text
            print(f"{date} – {name} – {link}")
            break
