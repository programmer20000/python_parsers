with open(file="links.txt", mode="r+") as file:
    source = file.read()

    for links in set(source.split()):
        with open(file="links_unic.txt", mode="a", newline="") as file:
            file.write(links + "\n")
