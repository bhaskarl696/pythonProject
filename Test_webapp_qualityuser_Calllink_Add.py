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

#################### start of Manage_call_link    ########################################
def Manage_Call_Link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/Manage_Call_Link() module")
    #Call_Link_buton=chrome_driver.find_element_by_partial_link_text('Call Link');
    Call_Link_buton=chrome_driver.find_element(By.CSS_SELECTOR,"ul.select>li>a[href='call_link']")
    Call_Link_buton.click()
    search_call_link()
    enter_scanid_call_link()
    search_scan_id_call_link()
    select_scan_id()
    click_validity_date_call_link()
    click_validity_time_call_link()
    click_add_button_call_link()
    sleep(25)
    
  ## Take Screen shot
  ##Take_screen_shot("Manage_Call_link_screen")
  ## End Taking Screen shot
        

## accept scan id for call linking
def search_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/search_Call_Link() module")
    sleep(5)
   # chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/input").click()
    chrome_driver.find_element(By.XPATH,"//input[@type='button' and @name='search']").click()
    sleep(1)
    
## enter to search scan id for call linking
def enter_scanid_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/enter_scanid_Call_Link() module")
    #scan_id_calllink= chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/form/div/div/input[1]")
    scan_id_calllink=chrome_driver.find_element(By.XPATH,"//input[@type='text' and @name='scan_id']")
    scan_id_calllink.send_keys("CLI01822@6@142202210145280691")
    sleep(1)
    
## search for the scan id - call linking
def search_scan_id_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/search_scand_id_Call_Link() module")
    #chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/form/div/div/input[2]").click()
    chrome_driver.find_element(By.XPATH,"//input[@type='button' and @value='Search' and @alt='Submit']").click()
    sleep(1)

## select the patient id
def select_scan_id():
    print("\n we are inside Test_webapp_quality_Calllink.py program/select_scand_id() module")
    #chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/form/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
    chrome_driver.find_element(By.XPATH,"//input[@type='button' and @name='view' and @value='Select']").click()
    sleep(1)

## click validity date
def click_validity_date_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/click_validity_date_call_Link() module")
    validity_date=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/input")
    validity_date.send_keys("21")
    validity_date.send_keys(Keys.ARROW_RIGHT)
    validity_date.send_keys(Keys.ARROW_LEFT)
    validity_date.send_keys("Nov")
    validity_date.send_keys(Keys.ARROW_RIGHT)
    validity_date.send_keys("2022")
    sleep(5)

## click validity time
def click_validity_time_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/click_validity_time_Call_Link() module")
    validity_time=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[3]/td[1]/input")
    validity_time.send_keys("12")
    validity_time.send_keys(Keys.ARROW_RIGHT)
    validity_time.send_keys(Keys.ARROW_LEFT)
    validity_time.send_keys("12")
    validity_time.send_keys(Keys.ARROW_RIGHT)
    validity_time.send_keys("PM")
    sleep(5)

## click Add button for adding call link
def click_add_button_call_link():
    print("\n we are inside Test_webapp_quality_Calllink.py program/click_add_button_Call_Link() module")
    #Add_button_call_link=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[4]/td/input")
    Add_button_call_link=chrome_driver.find_element(By.XPATH,"//input[@type='button' and @name='view' and @value='Add']")
    Add_button_call_link.click()
    sleep(1)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(2)

#################### End of Manage_call_link    ########################################
    
def Manage_Logout():
  try:
    print("\n we are inside Test_webapp_quality_Calllink.py program/Manage_Logout() module")
    Logout_buton=chrome_driver.find_element_by_partial_link_text('Logout');
    Logout_buton.click()
    
  ## Take Screen shot
    Take_screen_shot("Manage_Logout_screen")
  ## End Taking Screen shot

  
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


