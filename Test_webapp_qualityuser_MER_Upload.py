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
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Open_Application() module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

    
def Login_Qualityuser():
    
  try:
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Login_Qualityuser() module")
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

    screen_label=chrome.driver.find_element_by_id("MER Patient Summary")
    assert screen_label == "MER Patient Summary"
    print("\n login test case passed")
    
  except AssertionError:

    print("\n Error occurred Test case failed . Actual value is %s" % screen_label)

  except:
     pass 

##################### start of Manage_MER_Upload()###############################################################
    
def Manage_MER_Upload():
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Manage_MER_Upload() module")
    MER_Upload_buton=chrome_driver.find_element_by_partial_link_text('MER Upload');
    MER_Upload_buton.click()
    sleep(1)
    Pre_upload_checks_MER_Upload()
    Upload_MER_Upload()
    Post_upload_checks_MER_Upload()
    Create_Orders_MER_Upload()
    sleep(10)
    
  ## Take Screen shot
  ##  Take_screen_shot("Manage_MER_Upload_screen")
  ## End Taking Screen shot

###### start of Pre_upload_checks_MER_Upload()
    
def Pre_upload_checks_MER_Upload():
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Pre_upload_checks_MER_Upload() module")
    Pre_upload_checks_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[1]/input")
    Pre_upload_checks_button.click()
    sleep(10)
    
###### end of Pre_upload_checks_MER_Upload()
    
###### start of  Upload MER _upload()
    
def Upload_MER_Upload():
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Upload_MER_Upload() module")
    Upload_MER_upload_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[2]/input")
    Upload_MER_upload_button.click()
    sleep(10)

###### end of  Upload MER _upload()

###### start of  Post_upload_checks_MER_Upload()
def Post_upload_checks_MER_Upload():
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Post_upload_checks_MER_Upload()")
    Post_upload_checks_button= chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[3]/input")
    Post_upload_checks_button.click()
    sleep(10)

###### end of  Post_upload_checks_MER_Upload()

###### start of  Create_Orders_MER_Upload()
    
def Create_Orders_MER_Upload():
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Create_Orders_MER_Upload()")
    Create_Order_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[4]/input")
    Create_Order_button.click()
    sleep(10)

###### end of  Create_Orders_MER_Upload()
    
   

##################### End of Manage_MER_Upload()###############################################################
  
def Manage_Logout():
  try:
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Manage_Logout()")
    Logout_buton=chrome_driver.find_element_by_partial_link_text('Logout');
    Logout_buton.click()
    
  ## Take Screen shot
    Take_screen_shot("Manage_Logout_screen")
  ## End Taking Screen shot
  
  except:
    pass

def Close_Application():
    
  try:
    print("\n we are inside - Test_webapp_qualityuser_MER_Upload.py - Close_Application()")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
Manage_MER_Upload()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


