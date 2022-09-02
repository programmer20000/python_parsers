with open(file="sql/links_video.txt", mode="r+") as file:
    source = file.read()
    for i in set(source.split()):
        print(i)
        with open(file="sql/link_video_unic.txt", mode="a", newline="") as f:
            f.write(i + '\n')

