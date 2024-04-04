import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Locators.Certificate_locators import Certificate_locators


def navigate_certificate(driver):
    adminstrator_ele=driver.find_element("xpath", Certificate_locators.administrator_icon)
    #adminstrator_ele = driver.find_element("xpath", "//span[@data-qa='icon-administrator']")
    WebDriverWait(driver, 30).until(EC.visibility_of(adminstrator_ele))
    actions=ActionChains(driver)
    actions.move_to_element(adminstrator_ele).click().perform()
    actions.perform()
    time.sleep(5)
    certificate_ele=driver.find_element("xpath",Certificate_locators.certificates)
    WebDriverWait(driver, 30).until(EC.visibility_of(certificate_ele))
    certificate_ele.click()
    time.sleep(10)
    head_ele=driver.find_element("xpath",Certificate_locators.certi_docu)
    assert head_ele.text == "Certificates and Documents", "Certificate page not loaded"
    print("Navigation success")
    return driver

def select_the_certificate(driver):
    scl_ele=driver.find_element("xpath",Certificate_locators.scl_lev_cer)
    WebDriverWait(driver, 30).until(EC.visibility_of(scl_ele))
    scl_ele.click()
    time.sleep(20)
    preview_ele=driver.find_element("xpath",Certificate_locators.scl_lev_cer_pre)
    WebDriverWait(driver, 30).until(EC.visibility_of(preview_ele))
    if preview_ele.is_displayed():
        driver.find_element("xpath",Certificate_locators.Generate).click()
        print("Certificate is selected")
    else:
        print("Unable to select the certificate")
    time.sleep(10)
    return driver
