with open(file="links_video.txt", mode="r+") as file:
    source = file.read()
    for unic_links in set(source.split()):
        with open(file="links_video_unic.txt", mode="a", newline="") as file:
            file.write(unic_links + "\n")