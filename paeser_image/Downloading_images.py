import requests


def Download_image():
    with open(file="links_image_unic.txt", mode="r") as file:
        source = file.read()
        for links in source.split("\n"):
            response =requests.get(url=links).content

Download_image()