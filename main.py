import requests
from bs4 import BeautifulSoup

# 1. Делаем запрос на страницу (пример)
url = "https://www.kicktraq.com/projects/"
response = requests.get(url)  # response.text содержит HTML

# 2. Создаём объект BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3. Вытаскиваем весь текст со страницы
text = soup.get_text()
print(text)