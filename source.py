import sys
from selenium import webdriver

path = "~/Projects/Python/"
browser = webdriver.Chrome()
browser.get("https://github.com/login")

def create():
	folderName = str(sys.argv[1])
	python_button = browser.find_element_by_xpath("//input[@id='login_field']")
	python_button.send_keys('username')
	python_button = browser.find_element_by_xpath("//input[@id='password']")
	python_button.send_keys('password')
	python_button = browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]")
	python_button.click()
	browser.get("https://github.com/new")
	python_button = browser.find_element_by_xpath("//input[@id='repository_name']")
	python_button.send_keys(folderName)
	python_button = browser.find_element_by_css_selector('button.first-in-line')
	python_button.submit()


if __name__ == '__main__':
	create()