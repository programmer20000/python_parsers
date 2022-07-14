with open(file="links_images.txt", mode="r+") as file:
    source = file.read()
    for unic_link in set(source.split()):
        with open(file="link_image_UNIC.txt", mode="a", newline="") as file:
            file.write(unic_link + "\n")