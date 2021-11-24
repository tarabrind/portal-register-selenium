import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import config


service = Service("/var/local/chromedriver")

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.headless = True

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(config.URL)
    time.sleep(5)

    # select radio button
    if config.STATUS == 1:
        status_radio = driver.find_element(
            By.XPATH,
            "//input[@id='ctl00_ctl31_g_8233b272_8351_4296_80cf_5ceed6e0422b_WorkStatusRbtn_0'][@type='radio']"
        )
        status_radio.click()
        time.sleep(5)
    elif config.STATUS == 2:
        status_radio = driver.find_element(
            By.XPATH,
            "//input[@id='ctl00_ctl31_g_8233b272_8351_4296_80cf_5ceed6e0422b_WorkStatusRbtn_1'][@type='radio']"
        )
        status_radio.click()
        time.sleep(5)

    # press Submit button
    submit_button = driver.find_element(
        By.XPATH,
        "//input[@name='ctl00$ctl31$g_8233b272_8351_4296_80cf_5ceed6e0422b$SubmitStatBtn'][@type='button']"
    )
    submit_button.click()
    time.sleep(5)

except BaseException as er:
    print(er)
finally:
    driver.close()
    driver.quit()
