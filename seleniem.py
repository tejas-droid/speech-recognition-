from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# install seleium pip install selenium
import time #import time 



name = "dheeme dheeme"
timeout = 5
driver = webdriver.Chrome(executable_path = "E:\\chromedriver_win32\chromedriver.exe")
# https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/  download chrome driver and extract and give its executable_path

driver.get("https://www.youtube.com/results?search_query="+ name)

driver.find_element_by_xpath('//*[@id="dismissable"]').click()

time.sleep(3)
#duration = driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div > span.ytp-time-duration')
duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
#print(duration)
print(duration.text[-2:])
time.sleep(int(duration.text[-2:]))
duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
#print(duration)

c = duration.text
mins  = int(c[:1])
sec = int(c[-2:])
total_time = (mins*60) + sec
print(total_time)

time.sleep(total_time + 5)

driver.close()