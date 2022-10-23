from selenium.webdriver import Chrome

driver = Chrome(executable_path="C:/webdrivers/chromedriver_win32/")
driver.get('https://quotes.toscrape.com/js')


element = driver.find_element_by_class_name("author")
print(element.text)

driver.quit()