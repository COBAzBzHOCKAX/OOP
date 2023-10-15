from bs4 import BeautifulSoup
import requests


base = 'https://ru.stackoverflow.com/' # Базовая ссылка
html = requests.get(base).content # Забираем HTML-код странички
soup = BeautifulSoup(html, 'lxml') # Создаём объект супа. Первый аргумент - весь HTML-код страницы.
# Второй аргумент - сама библиотека для парсинга. В нашем случае lxml
div = soup.find('div', id="question-mini-list") # Находим с помощью метода find() нужный нам див уточняя id

a = div.find('a', class_='s-link')

parent = a.find_parent()

print(parent)