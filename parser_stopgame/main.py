from selenium import webdriver

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

exclude = "#comments"

url_site = "https://stopgame.ru/video/new/p1"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={headers}")

try:
    driver = webdriver.Chrome(executable_path="ChromeDriver/chromedriver.exe", options=options)
    driver.get(url_site)

    getting_link_description = driver.find_element_by_class_name("items").find_elements_by_tag_name("img")
    for link in getting_link_description:
        l1 = link.get_attribute("src")

        with open(file="links_images.txt", mode="a", newline="") as file:
            file.write(l1 + "\n")

except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
