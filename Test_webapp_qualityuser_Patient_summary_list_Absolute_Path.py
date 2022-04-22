from webdriver_manager.chrome import ChromeDriverManager
import pytest
import selenium
import sys
import selenium.webdriver.chrome.options
import selenium.webdriver.common.keys
import time
import datetime
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
    print("\n we are inside - Test_webapp_qualityuser_Patient_summary_list_Absolute_Path.py - Open_Application() module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

    
def Login_Qualityuser():
    
  try:
    print("\n we are inside - Test_webapp_qualityuser_Patient_summary_list_Absolute_Path.py - Login_Qualityuser() module")
    username_field=chrome_driver.find_element_by_name("userName")
    password_field = chrome_driver.find_element_by_id("password")
    submit_button = chrome_driver.find_element_by_id("edit-submit")
    username_data="qualityuser1"
    password_data="password1234"
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
      print("the value of i is ",i)
    # to traverse through the table column
      for j in range(1, Patient_list_columns_count + 1):
        print("the value of j is  ",j)
    # to get all the cell data with text method
        All_cell_data = chrome_driver.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text
        print(All_cell_data)
    sleep(5)
    # to close the browser
    #chrome_driver.close()

    ## Take Screen shot
    Take_screen_shot("MER Patient Summary")
## End Taking Screen shot

    screen_label=chrome.driver.find_element_by_id("MER Patient Summary")
    assert screen_label == "MER Patient Summary"
    print("\n login test case passed")
    
  except AssertionError:

    print("\n Error occurred Test case failed . Actual value is %s" % screen_label)

  except:
     pass 


def Manage_Logout():
    print("\n we are inside - Test_webapp_qualityuser_Patient_summary_list_Absolute_Path.py - Manage_Logout() module")
    chrome_driver.refresh()
    Logout_buton = chrome_driver.find_element_by_partial_link_text('Logout')
    Logout_buton.click()
    sleep(5)
    print("\n\n logged out successfully from the  app")

####################################### Start commonly called methods section ######################################################################
  

def Close_Application():
    
  try:
    print("\n we are inside - Test_webapp_qualityuser_Patient_summary_list_Absolute_Path.py - Close_Application() module")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


