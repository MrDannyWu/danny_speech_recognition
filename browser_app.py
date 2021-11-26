import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def open_url(url='https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=月亮代表我的心'):


    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # chrome_options.add_argument('ser-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36')
    # chrome_options.add_argument('sec-ch-ua-platform="Android"')
    # chrome_options.add_argument('sec-ch-ua-mobile=?1')
    # chrome_options.add_argument('referer=https://music.163.com/')
    # chrome_options.add_argument('sec-ch-ua=" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"')
    # chrome_options.add_argument('cookie=cookie=_ntes_nnid=ae73ee13626b46db9344aae679155f59,1637672730237; _ntes_nuid=ae73ee13626b46db9344aae679155f59; NMTID=00OudXQR_W_FhcVrEdpqn4Q4dbKNJUAAAF9TObAVQ; WNMCID=ocqllu.1637672730435.01.0; WEVNSM=1.0.0; JSESSIONID-WYYY=NYnlnmncuPbD4psncdXu%5CN093JvH23lyh1wkklsSaeHEYoQVURwJ3Df8cReGEwDXOilQ8hs%5CrD%5C3XMQ3g%2BAk%2BTiGG2u2K%2FblhOckd3T%5CCTcOrjZt5KGHByYsRm%5CTHnWsjikyssUJpXjeMKMSNayt%5C0XO%2Fha7I10anwIumQbQ3Iekd2zB%3A1637676195913; _iuqxldmzr_=33')

    dcap = (DesiredCapabilities.ANDROID)
    dcap["chrome.page.settings.userAgent"] = ("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36")
    bs_app = webdriver.Chrome(executable_path='./tools/chromedriver.exe', options=chrome_options, desired_capabilities=dcap)
    # bs_app = webdriver.Chrome(executable_path='./tools/chromedriver.exe', options=chrome_options)

    bs_app.get(url)
    time.sleep(2)

    play = bs_app.find_element_by_xpath('//a[@class="song_name"]')
    play.click()
    # play_1 = bs_app.find_element_by_xpath('//a[@title="播放/暂停(p)"]')
    # play_1.click()
    # time.sleep(1000)

if __name__ == '__main__':
    open_url()