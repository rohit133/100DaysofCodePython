from selenium import webdriver
from selenium.webdriver.common.keys import Keys




chrome_driver_path ="C:\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

site_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(site_url)

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)


search_bar = driver.find_element_by_xpath('//*[@id="searchInput"]')
search_bar.click()
search_bar.send_keys("Hello World")
# search_bar.send_keys(Keys.ENTER)
# sleep(2000)
search_bar_icon =driver.find_element_by_xpath('//*[@id="searchButton"]')
search_bar_icon.click()


# driver.quit()