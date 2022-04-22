from webdriver_manager.chrome import ChromeDriverManager
import pytest
import selenium
import sys
import selenium.webdriver.chrome.options
import selenium.webdriver.common.keys
import time
import datetime
import xlrd
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from Screenshot import Screenshot_Clipping
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

## Global Variables
chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

## end of Global Variables

def Open_Application():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_Login_user_Absolute_Path.py program/Open_Application()")
    print("we are inside cardiotrack webapp module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

def Login_Qualityuser():
    print("\n we are inside Test_webapp_qualityuser_Login_user_Absolute_Path.py program/Login_Qualityuser()")
    #username_field = chrome_driver.find_element_by_name("userName")
    # password_field = chrome_driver.find_element_by_id("password")
    # submit_button = chrome_driver.find_element_by_id("edit-submit")

    username_field = chrome_driver.find_element(By.XPATH,"//input[@name='userName']")
    password_field = chrome_driver.find_element(By.XPATH,"//input[@type='password']")
    submit_button = chrome_driver.find_element(By.XPATH,"//input[@value='Sign In']")
    username_data = "qualityuser1"
    password_data = "password1234"
    username_field.send_keys(username_data)
    password_field.send_keys(password_data)
    submit_button.click()
    sleep(5)
    ## create a list from patient table displayed in the screen
    # to identify the table rows
    Patient_list_rows = chrome_driver.find_elements_by_xpath("//table[@id= 'patient-table']/tbody/tr")
    # to identify table columns
    Patient_list_columns = chrome_driver.find_elements_by_xpath("//*[@id= 'patient-table']/tbody/tr[3]/td")
    # to get row count with len method
    Patient_list_rows_count = len(Patient_list_rows)
    print("total number of rows are", Patient_list_rows_count)
    # to get column count with len method
    Patient_list_columns_count = len(Patient_list_columns)
    print("total number of columns are", Patient_list_columns_count)
    # to traverse through the table rows excluding headers
    for i in range(1, Patient_list_rows_count + 1):
        print("the value of i is ", i)
    # to traverse through the table column
        for j in range(1, Patient_list_columns_count + 1):
            print("the value of j is  ", j)
            # to get all the cell data with text method
            All_cell_data = chrome_driver.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text
            print(All_cell_data)
    sleep(5)
    screen_label = chrome_driver.find_element(By.ID,"screen-name").text
    assert screen_label == "MER Patient Summary"
    print("\n login test case passed")
    print("\n Error occurred Test case failed . Actual value is %s" % screen_label)

def read_from_file():
    print("\n we are inside Test_webapp_qualityuser_Login_user_Absolute_Path.py program/read_from_file()")
    print(" we are going to read login credentials from excel file")
    workbook = xlrd.open_workbook("DataSheet.xlsx")
    sheet = workbook.sheet_by_name("login")

    # get total number of rows
    totalrowcount = sheet.nrows
    columncount = sheet.ncols
    print("total number of rows and columns  are ", totalrowcount, columncount)

    for current_row in range(1, totalrowcount):
        username_data = sheet.cell_value(current_row, 0)
        password_data = sheet.cell_value(current_row, 1)
        print(username_data, password_data)

def Manage_Logout():
    print("\n we are inside Test_webapp_qualityuser_Login_user_Absolute_Path.py program/Manage_Logout()")
    chrome_driver.refresh()
    Logout_buton = chrome_driver.refresh()
    Logout_button=chrome_driver.find_element(By.XPATH,"//b[text()='Logout']").click()
    sleep(1)
    print("\n\n logged out successfully from the  app")

####################################### Start commonly called methods section ######################################################################
  

def Close_Application():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_Login_user_Absolute_Path.py program/Close_Application()")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
read_from_file()
Login_Qualityuser()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


