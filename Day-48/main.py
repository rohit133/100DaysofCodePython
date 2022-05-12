from selenium import webdriver
chrome_driver_path ="C:\Dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_name("q")
# print(price.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

event_times = driver.find_elements_by_xpath("//div[@class='medium-widget event-widget last']/div/ul/li/time")
event_attributes = driver.find_elements_by_xpath("//div[@class='medium-widget event-widget last']/div/ul/li/a")

events = {}
for n in range(len(event_times)):
    events[n]={

        'time': event_times[n].text,
        'name': event_attributes[n].text,

    }

print(events)

# driver.close()
driver.quit()