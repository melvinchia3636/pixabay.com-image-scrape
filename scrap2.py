from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, threading
driver = webdriver.Chrome()
def download(image):
	filename = image.split('/')[-1]
	r = requests.get(image, stream=True)
	if r.status_code == 200:
	    with open(filename, 'wb') as f:
	        for chunk in r:
	            f.write(chunk)
for page_number in range(1, 175):
	driver.get('https://pixabay.com/images/search/?order=ec&pagi=' + str(page_number))
	[driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) for i in range(20)]
	[threading.Thread(target=download, args=(i.get_attribute('src'),)).start() for i in driver.find_element_by_class_name('search_results').find_elements_by_tag_name('img')]
driver.close()
quit()
