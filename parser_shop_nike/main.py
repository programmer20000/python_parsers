from selenium import webdriver
from time import sleep

user_agent = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}

products_and_price = {}

start_page = 1
stop_page = 17

options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={user_agent}")
try:
    driver = webdriver.Chrome(executable_path="FirefoxDriver/geckodriver.exe", options=options)
    for i in range(start_page, stop_page):
        print(f"{i} from {stop_page}")
        url_site = f"https://deltasport.ua/store/men/filter/product_types-is-krossovki/?PAGEN_1={i}"
        driver.get(url=url_site)
    get_cards_site = driver.find_elements_by_class_name("s_item")
    for links in get_cards_site:
        l1 = links.find_elements_by_class_name("item_name")
        l2 = links.find_elements_by_class_name("f_price")
        for title in l1:
            for price in l2:
                products_and_price[title.text] = price.text
        print(products_and_price)


except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
