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

## Global Variables
chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

## end of Global Variables

def Open_Application():
    
  try:
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Open_Application() module")
    print("we are inside cardiotrack webapp module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

def Login_Qualityuser():
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Login_Qualityuser() module")
    username_field=chrome_driver.find_element_by_name("userName")
    password_field = chrome_driver.find_element_by_id("password")
    submit_button = chrome_driver.find_element_by_id("edit-submit")
    username_data="qualityuser1"
    password_data="password1234"
    username_field.send_keys(username_data)
    password_field.send_keys(password_data)
    submit_button.click()
    sleep(1)
    
## Take Screen shot
##    Take_screen_shot("MER Patient Summary")
## End Taking Screen shot
    
def Manage_LabReports():
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Manage_LabReports() module")
    lab_reports_buton=chrome_driver.find_element_by_partial_link_text('Lab Report');
    lab_reports_buton.click()

## Zoylo Report
    Zoylo_report()
    Upload_Replacement_file()
## Zoylo Report
         
def Take_screen_shot(file_name):
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Take_screen_shot(file_name) module")
    Current_Page_Screenshot=Screenshot_Clipping.Screenshot()
    get_current_url = chrome_driver.current_url
    chrome_driver.get(get_current_url)
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    screenshot_img_path=Current_Page_Screenshot.full_Screenshot(chrome_driver, save_path=r'.\\Screenshots - QualityUser', image_name = date_stamp +"_ "+file_name+".png")
    print("\n",screenshot_img_path)

def Zoylo_report():
  
## Select Zoylo Report Type
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Zoylo_report() module")
    Report_type=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[1]/form/table/tbody/tr[1]/td/select")
    Report_type.send_keys(Keys.DOWN)
    Report_type.click()
    sleep(1)
    
    Header_Type=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[1]/form/table/tbody/tr[2]/td/select")
    Header_Type.click()
    Header_Type.send_keys(Keys.DOWN)
    Header_Type.click()
    sleep(1)
    
    Footer_White_Label=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[1]/form/table/tbody/tr[3]/td/select")
    Footer_White_Label.click() 
    Footer_White_Label.send_keys(Keys.DOWN)
    Footer_White_Label.click()
    sleep(1)
    
    Footer_height=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[1]/form/table/tbody/tr[4]/td[1]/input")
    Footer_height.send_keys(Keys.BACK_SPACE)
    Footer_height.send_keys(Keys.BACK_SPACE)
    Footer_height.send_keys(Keys.BACK_SPACE)
    sleep(1)
    
    Footer_height.send_keys(Keys.ARROW_LEFT)
    Footer_height.send_keys(Keys.ARROW_LEFT)
    Footer_height.send_keys(Keys.ARROW_LEFT)
    sleep(1)
    Footer_height.send_keys(99)
    sleep(1)

def Upload_Replacement_file():           
## uploading file   
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Upload_Replacement_file() module")
    file_select_button=chrome_driver.find_element(By.XPATH,"//input[@type='file' and @name='lab_report']")
    file_select_button.send_keys("D://Cardiotrack Workstation Backup 08042022//Bhaskar l//Bhaskar l//CardioTrack Testing//Phyton//CardiotrackWebapp Automation//Sample Test files//CLI01822@1@31120211271622611_consolidated_report.pdf")
    sleep(10)
    Replace_file_button=chrome_driver.find_element(By.XPATH,"//input[@type='button' and @value='Replace']")
    Replace_file_button.click()

def Manage_Logout():
    chrome_driver.refresh()
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Manage_Logout() module")
    Logout_button=chrome_driver.find_element(By.XPATH,"//b[text()='Logout']").click()
    sleep(1)
    print("\n\n logged out successfully from the  app")
    
    
    
def Close_Application():
    print("\n we are inside Test_webapp_Qualityuser_LabReports.py program/Close_Application() module")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")


## calling the functions

Open_Application()
Login_Qualityuser()
Manage_LabReports()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


