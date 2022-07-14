import os

from selenium import webdriver
from time import sleep

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

name_folder = input("Enter name folder: ")

exclude = input("Enter exclude link: ")

url_site = "https://www.youtube.com/playlist?list=PLqGS6O1-DZLp_UAGnZ-t49iZXKsDEts_k"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={headers}")

try:
    driver = webdriver.Chrome(executable_path="ChromeDriver/chromedriver.exe", options=options)
    driver.get(url=url_site)

    get_link_video = driver.find_elements_by_class_name("style-scope ytd-playlist-video-renderer")
    for links in get_link_video:
        l1 = links.find_elements_by_tag_name("a")
        for links_video in l1:
            l2 = links_video.get_attribute("href")
            # print(l2)

            if exclude not in l2:
                # print(l2)
                if not os.path.exists(name_folder):
                    os.mkdir(name_folder)
                with open(file=f"{name_folder}/link_video.txt",mode="a",newline="") as file:
                    file.write(l2+"\n")

except Exception as exception:
    print(exception)

finally:
    sleep(6)
    driver.close()
    driver.quit()


