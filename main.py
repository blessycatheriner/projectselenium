from Tests import Certificate, Generation, Login


def main():
    driver = Login.login()
    Certificate.navigate_certificate(driver)
    Certificate.select_the_certificate(driver)
    Generation.search_select_student(driver)
    Generation.update_remarks(driver)
    Generation.generate_and_download(driver)
    driver.quit()


if __name__ == "__main__":
    print("start")
    main()
    print("end")