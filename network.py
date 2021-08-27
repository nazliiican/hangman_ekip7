import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.palabrasaleatorias.com/random-words.php")
soup = BeautifulSoup(page.content, "html.parser")

x = (soup.select("div")[-1].text).lower()
