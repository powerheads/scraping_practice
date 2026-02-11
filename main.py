import sys
sys.stdout.reconfigure(encoding="utf-8")
import requests
from bs4 import BeautifulSoup
url = "https://www.kicktraq.com/projects/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
projects = soup.find_all("div", class_="project-pledgilizer-mid green")
for div in projects:
    print(div.get_text(strip=True))

