import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from orangehrm.utilities.excel_functions import Selva_Excel_Functions


def login(self,browser):
    excel_file_name = "C://Users//ssekar588//PycharmProjects//GUVI Selenium 2//orangehrm//credentials_data//test_data.xlsx"
    sheet_name = "Sheet1"
    s = Selva_Excel_Functions(excel_file_name, sheet_name)
    rows = Selva_Excel_Functions(excel_file_name, sheet_name).Row_Count()
    for row in range(2, rows + 1):
        username = Selva_Excel_Functions(excel_file_name, sheet_name).Read_Data(row, 6)
        password = Selva_Excel_Functions(excel_file_name, sheet_name).Read_Data(row, 7)
        username_input = browser.find_element(By.XPATH, "//input[@placeholder='Username']")
        username_input.send_keys(username)
        password_input = browser.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_input.send_keys(password)
        login = browser.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login.click()

    # Wait for the page to load and check if login was successful
        browser.implicitly_wait(10)
        if 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index' in browser.current_url:
            print("SUCCESS : Login Success with Username {a}".format(a=username))
            Selva_Excel_Functions(excel_file_name, sheet_name).Write_Data(row, 8, "TEST PASS")
            browser.back()
        elif 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login' == browser.current_url:
            print("FAIL : Login Failure with Username {a}".format(a=username))
            Selva_Excel_Functions(excel_file_name, sheet_name).Write_Data(row, 8, "TEST FAIL")
            browser.back()

# Close the browser
