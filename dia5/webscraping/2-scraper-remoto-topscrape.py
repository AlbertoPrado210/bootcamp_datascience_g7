import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = "http://books.toscrape.com"

response = requests.get(URL)

if response.status_code == 200:
    data = response.content
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_='product_pod')
    print(f'total de libros : {len(books)}')
    lista_libros = []
    print(books[0])
    for book in books:
        titulo = book.find('h3').find('a')['title']
        price = book.find('p',class_='price_color').get_text()
        lista_libros.append([titulo,price])
        
    print(tabulate(lista_libros, headers=['Título','Precio'], tablefmt='grid'))