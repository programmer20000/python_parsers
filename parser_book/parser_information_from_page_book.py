from selenium import webdriver

from time import sleep

user_agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={user_agent}")

try:
    driver = webdriver.Firefox(executable_path="FirefoxDriver/geckodriver.exe", options=options)
    driver.maximize_window()

    with open(file="links_unic.txt", mode="r") as file:
        source = file.read()
        for links in source.split("\n"):
            driver.get(url=links)

            get_title_books = driver.find_element_by_class_name("block-content")
            print(get_title_books.text)

except Exception as exception:
    print(exception)
    sleep(6)
finally:
    driver.close()
    driver.quit()
