from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
tar_url0 = 'https:bestpartner08.jp'
tar_url1 = 'https:google.com'
tar_url2 = 'https:tomomi0824.blog.fc2.com'

# ブラウザのオプションにヘッドレスモードを指定
options = webdriver.FirefoxOptions()
options.add_argument('--headless')

for i in range(3):

    driver = webdriver.Firefox(options=options)
    driver.get(tar_url2)
    ##driver.find_element_by_name('profile-list-description').click()
    print(driver.current_url) ## URLを確認する
    ##browser.find_element_by_partial_link_text("https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F").click()
    #browser.find_element_by_link_text("不倫・婚外").click()
    wait = WebDriverWait(driver, 10) # 最大10秒
    elem = driver.find_element(By.XPATH, '//a[@href="//blog.with2.net/link/?1977271:1372"]')
    print(driver.current_url)
    elem.click()
    wait = WebDriverWait(driver, 10) # 最大10秒
    driver.quit()



## <a target="_blank" href="https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F">君の好きなとこ</a>