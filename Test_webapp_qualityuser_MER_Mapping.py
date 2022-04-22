######   please make sure you have provided the correct scan id which is still not assigned to any doctor for new mer assignement #####################

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
import screenshots
#from Screenshot import Screenshot_Clipping
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

    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Open_Application() module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

    
def Login_Qualityuser():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Login_Qualityuser() module")
    username_field=chrome_driver.find_element_by_name("userName")
    password_field = chrome_driver.find_element_by_id("password")
    submit_button = chrome_driver.find_element_by_id("edit-submit")
    username_data="qualityuser1"
    password_data="password1234"
    username_field.send_keys(username_data)
    password_field.send_keys(password_data)
    submit_button.click()
    screen_label=chrome.driver.find_element_by_id("MER Patient Summary")
    assert screen_label == "MER Patient Summary"
    print("\n login test case passed")
    
  except AssertionError:

    print("\n Error occurred Test case failed . Actual value is %s" % screen_label)

  except:
     pass 


def Manage_MER_Mapping():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Manage_MER_Mapping() module")
    MER_Mapping_buton=chrome_driver.find_element_by_partial_link_text('MER Mapping');
    MER_Mapping_buton.click()
    sleep(1)
    Search_scan_Id()
    enter_scan_id("CLI01822@6@102202217124948336") ## existing scan id for reassignment of the doctor
    search_given_scan_id() 
    select_scan_id()
    select_doc_id_merMapping()
    Accept_doc_id_merMapping()
    click_search_doc_id_merMapping()
    select_found_specialist()
    Reassign_specialist()
    click_new_button_merMapping()
    Search_scan_Id()
    enter_scan_id("CLI01822@6@162202211265229065")  ## new mer scan id for assigning new doctor
    search_given_scan_id()
    select_scan_id()
    select_doc_id_merMapping()
    Accept_doc_id_merMapping()
    click_search_doc_id_merMapping()
    select_found_specialist()
    sleep(10)
    click_assign_doc_newmerMapping()
    sleep(10)
    
## Search for given scan id
def Search_scan_Id():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Search_scan_Id() module")
    scand_id_search=chrome_driver.find_element(By.XPATH,"//input[@type='button' and @onclick='m1()']")
    #scand_id_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input")
    scand_id_search.click()
    sleep(5)
    Manage_Logout()
    
## Accept or Enter scan id
def enter_scan_id(scanid):
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/enter_scan_id(scanid) module")
    scan_id_entered=chrome_driver.find_element(By.XPATH,"//input[@type='text' and @name='scan_id']")
    #scan_id_entered=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[1]/div/div/input[1]")
    scan_id_entered.send_keys(scanid)
    sleep(1)
       
## Search for entered scan id
def search_given_scan_id():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/search_given_scan_id() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[1]/div/div/input[2]").click()
    sleep(1)
    
## Select the found Scan id
def select_scan_id():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/select_scan_id() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[1]/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
    sleep(10)

## Search and select the doc id for mer mapping
def select_doc_id_merMapping():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/select_doc_id_merMapping() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/input").click()
    sleep(1)
    
## Accept doc id for mer mapping
def Accept_doc_id_merMapping():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Accept_doc_id_merMapping() module")
    doc_id_merMapping=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[2]/div/div/input[1]")
    doc_id_merMapping.send_keys("DOC027")
    sleep(1)
    
## click Search for doc id
def click_search_doc_id_merMapping():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/click_search_doc_id_merMapping() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[2]/div/div/input[2]").click()
    sleep(1)
    
## Select the found Specialist
def select_found_specialist():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/select_found_specialist() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[2]/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
    sleep(1)
    
## Reassign the specialist
def Reassign_specialist():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Reassign_specialist() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[4]/td/input[1]").click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(1)
    
### MER Mapping for newly created scan id #####
def click_new_button_merMapping():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/click_new_button_merMapping() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[1]/td[1]/input[2]").click()
    sleep(2)
    
## Assign the specialist for newly mer mapped scan id
def click_assign_doc_newmerMapping():
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/click_assign_doc_newmerMapping() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[4]/td/input[1]").click()
    sleep(10)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(10)
    
def Manage_Logout():
  try:
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Manage_Logout() module")
    Logout_buton=chrome_driver.find_element_by_partial_link_text('Logout');
    Logout_buton.click()
    
  except:
    pass

def Close_Application():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_MER_Mapping.py program/Close_Application() module")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
Manage_MER_Mapping()
#Manage_Logout()
Close_Application()

quit()

## end of calling the functions


