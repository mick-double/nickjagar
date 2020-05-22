from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

tar_url0 = 'https:bestpartner08.jp'
tar_url1 = 'https:google.com'
tar_url2 = 'https://love.blogmura.com/love_furin/ranking/out'
tar_url3 = 'https://blogmura.com/profiles/10919327/ranking'
tar_url4 = 'https://blog.with2.net/rank2091-0.html'

# ブラウザのオプションにヘッドレスモードを指定
options = webdriver.FirefoxOptions()
options.add_argument('--headless')

# /html/body/div[3]/div/div[1]/div[2]/ul/li[5]/div[3]/div/p[1]/a
# <a target="_blank" href="https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F">君の好きなとこ</a>

for i in range(3):

    driver = webdriver.Firefox(options=options)
#    driver = webdriver.Firefox()
    driver.get(tar_url4)
    ##driver.find_element_by_name('profile-list-description').click()
    print(driver.current_url) ## URLを確認する
    ##browser.find_element_by_partial_link_text("https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F").click()
    #browser.find_element_by_link_text("不倫・婚外").click()
    wait = WebDriverWait(driver, 10) # 最大10秒
    #elem = driver.find_element(By.XPATH, '//img[@alt="君の好きなとこ"]')
    #elem = driver.find_element(By.XPATH, '//a[@href="//link.blogmura.com/out/?ch=10919327&amp;url=http://bestpartner08.jp/"]')
    elem = driver.find_element_by_link_text(u'君の好きなとこ')
    print(driver.current_url)
    #if EC.element_to_be_clickable(By.XPATH,'//img[@alt="君の好きなとこ"]'):
    #    print ('true')
    elem.click()
    wait = WebDriverWait(driver, 10) # 最大10秒
    time.sleep(10)
    driver.quit()



## <a target="_blank" href="https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F">君の好きなとこ</a>