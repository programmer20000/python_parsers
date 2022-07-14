from selenium import webdriver

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

url_site = "https://www.pexels.com/ru-ru/"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={headers}")

try:
    driver = webdriver.Chrome(executable_path="ChromeDriver/chromedriver.exe", options=options)
    driver.get(url=url_site)
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        get_link_image = driver.find_elements_by_class_name("BreakpointGrid_column__CTepl")
        for link_image in get_link_image:
            l1 = link_image.find_elements_by_class_name("BreakpointGrid_item__erUQQ")
            for source_image in l1:
                source = source_image.find_elements_by_tag_name("img")
                for image in source:
                    l2 = image.get_attribute("src")
                    with open(file="links_image.txt", mode="a", newline="") as file:
                        file.write(l2 + "\n")
except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
