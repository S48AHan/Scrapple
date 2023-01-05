from bs4 import BeautifulSoup
import requests , openpyxl
'''
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Laptops'
print(excel.sheetnames)
sheet.append(['Laptop Name','Processor','Year of Release','IMDB Rating'])
'''
try:
    source = requests.get('https://www.startech.com.bd/laptop-notebook/laptop?limit=90&fbclid=IwAR2vJ0_8lYnGonLMcVzVCz3K9oH9SLhSnxadTL7CTINASadYauIpsO0UDvo')
    source.raise_for_status()
    soup = BeautifulSoup(source.text,'html.parser')
    laptops = soup.find('div', class_= 'main-content p-items-wrap').findAll('div',class_='p-item')
    print(len(laptops))
    '''
    for laptop in laptops:
        name = laptop.find('td',class_='titleColumn').a.text
        rank = movie.find('td',class_='titleColumn').get_text(strip = True).split('.')[0]
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        rating = movie.find('td',class_='ratingColumn imdbRating').strong.text
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])
'''

except Exception as e:
    print(e)
'''
excel.save('IMDB Movie rating.xlsx')
'''