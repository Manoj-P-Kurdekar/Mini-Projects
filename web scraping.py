from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/Data_science")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())