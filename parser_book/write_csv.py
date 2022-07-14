import csv

with open(file="links_book.csv", mode="w") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "lINKS BOOK".upper(),
        )
    )

with open(file="links_unic.txt", mode="r") as file:
    source = file.read()
    for links in source.split():

        with open(file="links_book.csv", mode="a") as file:
            writer = csv.writer(file)
            writer.writerows(
                links,
            )

