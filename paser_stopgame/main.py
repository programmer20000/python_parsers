import requests
from bs4 import BeautifulSoup

source = ''

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

page_start = 1
page_stop = 61


def get_link_image():
    for i in range(page_start, page_stop):
        response = requests.get(url=f'https://stopgame.ru/news/all/p{i}', headers=headers)
        print(f'{i} from {page_stop}')
        source = response.text

        beautifulSoup = BeautifulSoup(source, 'lxml')
        get_links = beautifulSoup.find(class_='items').find_all('img')

        for link in get_links:
            image_link = link.get('src')

            with open(file='image_link.txt', mode='a', newline='') as file:
                file.write(image_link + '\n')

def main():
    get_link_image()

if __name__ == '__main__':
    main()
