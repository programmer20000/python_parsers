import os

from imgdl import download

if not os.path.exists("image"):
    os.mkdir("image")
with open(file="link_image_UNIC.txt") as file:
    source = file.readlines()
    for links in source:
        paths = download(links, store_path='image', n_workers=50)