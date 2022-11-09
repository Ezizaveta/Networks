import requests
from bs4 import BeautifulSoup

url = 'https://emojipedia.org/google/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('img')
for n, i in enumerate(items, start=1):
    item = i.get('src')
    print(item)
    str_item = str(item)
    if str_item[len(item) - 4:len(str_item)] == ".png":
        file_data = requests.get(str_item, stream=True)
        name = str_item.split('/')[-1]
        file = open(name, 'wb')
        for chunk in file_data.iter_content(4096):
            file.write(chunk)
