from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

what = input("what: ")

url_site = "https://images.google.com/"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={headers}")

try:
    driver = webdriver.Chrome(executable_path="ChromeDriver/chromedriver.exe", options=options)
    driver.get(url=url_site)

    input_filed = driver.find_element_by_tag_name("input")
    input_filed.send_keys(what)
    input_filed.send_keys(Keys.ENTER)

    driver.find_element_by_xpath(
        "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img").get_attribute(
        "src")
    image_download = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img""").get_attribute("src")
    print(image_download)

except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
# /html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img
# /html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[4]/a[1]/div[1]/img
