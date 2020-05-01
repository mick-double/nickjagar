from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
tar_url0 = 'https:bestpartner08.jp'
tar_url1 = 'https:google.com'



## for i in range(3):

driver = webdriver.Firefox()
driver.get(tar_url0)
##driver.find_element_by_name('profile-list-description').click()
print(driver.current_url) ## URLを確認する
##browser.find_element_by_partial_link_text("https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F").click()
#browser.find_element_by_link_text("不倫・婚外").click()
wait = WebDriverWait(driver, 10) # 最大10秒
# elem = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/a[@class="button-vote"]')
#<img src="//love.blogmura.com/love_furin/img/love_furin88_31.gif" alt="にほんブログ村 恋愛ブログ 不倫・婚外恋愛（ノンアダルト）へ" width="88" height="31" border="0">
sleep(5)
elem = driver.find_element(By.XPATH, "//a[@href='https://bestpartner08.jp/archives.html']")
print(driver.current_url)
elem.click()
wait = WebDriverWait(driver, 10) # 最大10秒
elem = driver.find_element(By.XPATH, "//a[@href='https://bestpartner08.jp/blog-entry-968.html']")
elem.click()
wait = WebDriverWait(driver, 10) # 最大10秒

driver.quit()




## <a target="_blank" href="https://link.blogmura.com/out/?ch=10919327&amp;url=http%3A%2F%2Fbestpartner08.jp%2F">君の好きなとこ</a>