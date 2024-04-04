import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Generation_locators import Generation_locators
from Test_Data.test_data_gen import Test_Dat

def search_select_student(driver):
    search_box=driver.find_element("xpath",Generation_locators.search)
    WebDriverWait(driver, 30).until(EC.visibility_of(search_box))
    search_box.send_keys(Test_Dat.search_name)
    time.sleep(5)
    checkbox=driver.find_element("xpath",Generation_locators.checkbox)
    checkbox.click()
    gen_but=driver.find_element("xpath",Generation_locators.generate)
    gen_but.click()
    time.sleep(10)
    details_ele=driver.find_element("xpath",Generation_locators.details)
    if details_ele.is_displayed():
        print("selection of student is successful")
    else:
        print("selection of student is unsuccessful")
    time.sleep(10)

def update_remarks(driver):
    rem_ele = driver.find_element("xpath",Generation_locators.remarks)
    driver.execute_script("arguments[0].scrollIntoView(true);",rem_ele)
    WebDriverWait(driver, 30).until(EC.visibility_of(rem_ele))
    rem_ele.send_keys(Test_Dat.remarks)
    print("Remark update successful")
    time.sleep(10)

def generate_and_download(driver):
    gen_but=driver.find_element("xpath",Generation_locators.generate)
    WebDriverWait(driver, 30).until(EC.visibility_of(gen_but))
    if gen_but.is_displayed():
        gen_but.click()
        time.sleep(10)
        gen_success=driver.find_element("xpath",Generation_locators.doc_gen)
        WebDriverWait(driver, 30).until(EC.visibility_of(gen_success))
        if gen_success.is_displayed():
            print("Report Generation successful")
            down_but=driver.find_element("xpath",Generation_locators.download)
            WebDriverWait(driver, 30).until(EC.visibility_of(down_but))
            down_but.click()
            time.sleep(10)
            print("Report download success")
        else:
            print("Report download failed")
    else:
        print("Click generate button failed")
