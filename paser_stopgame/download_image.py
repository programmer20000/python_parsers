import os

import requests

with open(file='image_link.txt', mode='r') as file:
    source = file.read()

    for image in source.split('\n'):
        symbol = image[80:-2]

        if '-' not in symbol:

            def download_images(url=''):
                if  not os.path.exists('image_folder'):
                    os.mkdir('image_folder')
                try:
                    response = requests.get(url=url)
                    with open(file=f'image_folder/image_{symbol}.jpg', mode='wb') as file:
                        file.write(response.content)
                        print('downloading image is successful')
                except:
                    print('downloading image not successful ')

            download_images(url=image)
