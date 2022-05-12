from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




chrome_driver_path ="C:\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

site_url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(site_url)

name = driver.find_element_by_xpath("/html/body/form/input[1]")
name.click()
name.send_keys("Rohit")

lastname = driver.find_element_by_xpath("/html/body/form/input[2]")
lastname.click()
lastname.send_keys("Sharma")

lastname = driver.find_element_by_xpath("/html/body/form/input[3]")
lastname.click()
lastname.send_keys("sharma1997@gmail.com")


button = driver.find_element_by_xpath("/html/body/form/button")
button.click()




sleep(3)
driver.quit()