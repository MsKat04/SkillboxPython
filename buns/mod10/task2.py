import requests
from bs import BeautifulSoup

def get_h3_headers(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлекаем все теги <h3> и получаем их текстовое содержимое
        h3_headers = [h3.text for h3 in soup.find_all('h3')]
        return h3_headers

url = "http://www.columbia.edu/~fdc/sample.html"
headers_list = get_h3_headers(url)

if headers_list:
    print("Подзаголовки сайта:")
    for header in headers_list:
        print(header)