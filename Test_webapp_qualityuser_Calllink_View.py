from selenium import webdriver
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
#from Screenshot import Screenshot_Clipping
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

print("\n we are inside Test_webapp_quality_Calllink.py program")
## Global Variables
chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

## end of Global Variables

def Open_Application():
    
  try:

    print("\n we are inside Test_webapp_quality_Calllink.py program/Open_application() module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
    Review_Status=chrome_driver.find_element(By.XPATH,"//tbody/tr[@class='patient_list']/td[9]").text
    print(Review_Status)
    sleep(10)
    Manage_Logout()
    quit()
  except:
    pass

    
def Login_Qualityuser():
    
  try:
    print("\n we are inside Test_webapp_quality_Calllink.py program/Login_qualityuser() module")
    username_field=chrome_driver.find_element_by_name("userName")
    password_field = chrome_driver.find_element_by_id("password")
    submit_button = chrome_driver.find_element_by_id("edit-submit")
    username_data="qualityuser1"
    password_data="password1234"
    username_field.send_keys(username_data)
    password_field.send_keys(password_data)
    submit_button.click()
    sleep(5)
    
## Take Screen shot
    Take_screen_shot("MER Patient Summary")
## End Taking Screen shot

    screen_label=chrome_driver.find_element_by_id("MER Patient Summary")
    assert screen_label == "MER Patient Summary"
    print("\n login test case passed")
    
  except AssertionError:

    print("\n Error occurred Test case failed . Actual value is %s" % screen_label)

  except:
     pass 

#################### start of View_call_link_details    ########################################

def Manage_Call_Link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/Manage_Call_Link() module")
    Call_Link_buton=chrome_driver.find_element(By.CSS_SELECTOR,"ul.select>li>a[href='call_link']")
    Call_Link_buton.click()
    sleep(5)
    view_call_link_details()
    view_Enter_search_scanid_call_link()
    click_view_search_scan_id_call_link()
    sleep(25)

## click view for list of call link ids with validity details
def view_call_link_details():
    print("\n we are inside Test_webapp_quality_Calllink.py program/view_Call_Link() module")
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR,"ul.select>li>a[href='view_call_link_list']").click()

## Enter scanid to check for validity details
def view_Enter_search_scanid_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/view_Search_scanid_call_link() module")
    view_Search_scanid=chrome_driver.find_element(By.XPATH,"//input[@type='text'  and @id='search_text']")
    view_Search_scanid.send_keys("CLI01822@6@162202210215161323")

## search scanid's validity details
def click_view_search_scan_id_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/search_scand_id_Call_Link() module")
    chrome_driver.find_element(By.XPATH,"//input[@type='button' and @value='Search']").click()

#################### End of View_call_link_details    ########################################
    
def Manage_Logout():
  try:
    print("\n we are inside Test_webapp_quality_Calllink.py program/Manage_Logout() module")
    Logout_buton=chrome_driver.find_element_by_partial_link_text('Logout');
    Logout_buton.click()
    

  except:
    pass


def Close_Application():
    
  try:
    print("\n we are inside Test_webapp_quality_Calllink.py program/Close_Application() module")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
Manage_Call_Link()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


