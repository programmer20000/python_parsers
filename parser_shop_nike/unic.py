with open(file="title_and price_footwear.txt",mode="r+",encoding="utf-8") as file:
    source = file.readlines()
    for element in set(source):
        print(element)
