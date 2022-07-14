from selenium import webdriver

user_agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={user_agent}")

try:
    driver = webdriver.Firefox(executable_path="FirefoxDriver/geckodriver.exe", options=options)
    url_site = "https://manybooks.net/search-book?field_genre%5B14%5D=14&language=All&search=&sticky=All&created_op=%3C&created%5Bvalue%5D=0&created%5Bmin%5D=&created%5Bmax%5D=&author_uid_op=%3E%3D&author_uid%5Bvalue%5D=0&author_uid%5Bmin%5D=&author_uid%5Bmax%5D=&sort_by=field_downloads&page=0"
    driver.get(url=url_site)

    driver.maximize_window()

    getting_links_books = driver.find_element_by_class_name("view-content").find_elements_by_tag_name("a")
    for link in getting_links_books:
        links = link.get_attribute("href")

        if "titles" in links:
            # print(links)
            with open(file="links.txt", mode="a", newline="") as file:
                file.write(links + "\n")
            print("Writing in file is successful")


except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
