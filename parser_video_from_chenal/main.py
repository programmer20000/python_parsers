import os

from selenium import webdriver

folder_name = input(" Enter folder name: ")

user_agent = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")

try:
    driver = webdriver.Chrome(executable_path="ChromeDriver\chromedriver.exe", options=options)
    url_site = "https://www.youtube.com/c/HowdyhoNet/videos"
    driver.get(url=url_site)

    getting_links = driver.find_elements_by_class_name("style-scope ytd-grid-renderer")
    for links1 in getting_links:
        links_1 = links1.find_elements_by_tag_name("a")
        for links2 in links_1:
            links_2 = links2.get_attribute("href")

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            with open(file=f"{folder_name}/links_video.txt", mode="a", newline="") as file:
                file.write(links_2 + "\n")


except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
