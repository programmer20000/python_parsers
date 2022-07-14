with open(file="links_image.txt", mode="r+") as file:
    source = file.read()
    for links in set(source.split()):
        with open(file="links_image_unic.txt", mode="a") as file:
            file.write(links + "\n")
