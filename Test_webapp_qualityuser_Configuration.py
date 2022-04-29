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
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Open_Application() module")
    print("we are inside cardiotrack webapp module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

    
def Login_Qualityuser():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Login_Qualityuser module")
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


def View_Configuration():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/View_Configuration module")
    Configuration_buton=chrome_driver.find_element_by_partial_link_text('Configuration');
    Configuration_buton.click()
    call_group()
    call_Group_Assign()
    search_Assign_specialist_button()
    search_Specialist()
    Displayed_Specialist()
    call_group_list_select_group()
   # Assign_button_Assign_specialist_group()
   # call_group_view_option()
   # Search_call_group_docid("DOC027")
   # click_search_docid()
   # Search_clear_call_group_docid()
   # Search_call_group_docid("DOC035")
    #click_search_docid()
    #Search_clear_call_group_docid()
    #call_group_view_option()
    #Search_records()
    #Enter_Group_Id()
    #Search_records()
    #sleep(2)
    #click_Search_Group_Id_Button()
    #sleep(2)
    #Search_records()
######### callmappin#g starts here ###################
    #Call_Mapping()
    #Search_Doctor_Assign()
    #Enter_Docid_Assign()
    #Search_Assignment_doctor()
    #Select_Assigned_Doctor_found()
    #Select_call_group_doc_assign()
    #Assign_callgroup_assign_doctor()
    #Assign_call_group_to_docid()
    sleep(2)
    #Call_Mapping()
    sleep(2)
    
## search Assign specialist button
def  search_Assign_specialist_button():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/search_Assign_specialist_button() module")
    #Search_specialist=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[1]/td[2]/input")
    Search_specialist=chrome_driver.find_element(By.XPATH,"//input[@type='button' and @name='search']")
    Search_specialist.click()
## search Assign specialist button

## click Enter specialist id button to search for specialist for assignment
def search_Specialist():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/search_Specialist() module")
    Check_specaialist_id=chrome_driver.find_element(By.XPATH,"//input[@type='text' and @name='specialist_id']")
    Check_specaialist_id.send_keys("DOC027")
    Specialist_details=chrome_driver.find_element(By.XPATH,"//input[@type='button' and @onclick='getspecialist();']")
    Specialist_details.click()
    sleep(2)
## click Enter specialist id button to search for specialist for assignment

## select the displayed specialist
def Displayed_Specialist():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Displayed_Specialist() module")
    Specialist_select=chrome_driver.find_element(By.XPATH,"//input[@type='button'  and @name='view' and  @value='Select']")
    Specialist_select.click()
## select the displayed specialist

## display call group list and select the group  
def call_group_list_select_group():
     print("\n we are inside Test_webapp_qualityuser_Configuration.py program/call_group_list_select_group() module")
     #call_group_list=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select")
     call_group_list=Select(chrome_driver.find_element(By.ID,"call_group_id"))
     call_group_list.click()
     call_group_list.select_by_value(14)
   #  Select_Group=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select/option[16]")
   #  Select_Group.click()
     sleep(2)
## display call group list and select the group
     
## click Assign button and assign specialist to the group
def Assign_button_Assign_specialist_group():
     print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Assign_button_Assign_specialist_group() module")
     Assign_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[4]/td/input")
     Assign_button.click()
     sleep(2)
     alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed during duplicate assignment of specialist to the group
     alert_obj.accept()
              
## CREATING AND ASSIGNING SPECIALIST TO THE NEW GROUP WILL BE DONE LATER

## call group View option
def call_group_view_option():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/call_group_view_option() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/table/tbody/tr/td[2]/label/a").click()
    
## call group View option

# clicking call group
def call_group():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/call_group() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/table/tbody/tr/td[1]/ul/li/a/b").click()
# clicking call group


## call group Assign option
def call_Group_Assign():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/call_Group_Assign() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/table/tbody/tr/td[1]/label/a").click()
## call group Assign option
    

## search for records in call group
    
def Search_call_group_docid(doc_id):
     print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Search_call_group_docid(doc_id) module")
     doc_id_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/input")
     doc_id_search.send_keys(doc_id)
## search for records in call group

## click search button to search on docid
def click_search_docid():
     print("\n we are inside Test_webapp_qualityuser_Configuration.py program/click_search_docid() module")
     docid_click_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[2]/label[1]") 
     docid_click_search.click()
     sleep(2)
## click search button to search on docid
     
def Search_clear_call_group_docid():
     print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Search_clear_call_group_docid() module")
     doc_id_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/input")
     doc_id_search.clear()
## search for records in call group

## click Search Group ID button
def  click_Search_Group_Id_Button():
      print("\n we are inside Test_webapp_qualityuser_Configuration.py program/click_Search_Group_Id_Button() module")
      Group_id_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[2]/input[2]")
      Group_id_button.click()
      sleep(2)
      
## enter Search criteria for group id
def Enter_Group_Id():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Enter_Group_Id() module")
    Search_Group_Id=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/input")
    Search_Group_Id.send_keys("CONSULT_IND")

def Search_records():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Search_records() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[3]/input").click()

    
############################################################       call mapping  ############################################################
    
def Call_Mapping():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Call_Mapping() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/table/tbody/tr/td[2]/ul/li/a/b").click()
    sleep(2)
    
# Serching doctor for assignment
def Search_Doctor_Assign():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Search_Doctor_Assign() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[1]/td[2]/input").click()
    sleep(2)
# Accept doctor id for searching
def Enter_Docid_Assign():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Enter_Docid_Assign() module")
    Doctor_Id_assign=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[1]/div/div/input[1]")
    Doctor_Id_assign.send_keys("CLI01822")
    sleep(2)
# Search Doctor for assignment
def Search_Assignment_doctor():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Search_Assignment_doctor() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[1]/div/div/input[2]").click()
    sleep(2)

# Select the Assigned found doctor
def Select_Assigned_Doctor_found():
      print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Search_Assignment_doctor() module")
      chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[1]/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
      sleep(2)
# Select Call Group
def Select_call_group_doc_assign():
     print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Select_call_group_doc_assign() module")
     chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select").click()
     sleep(2)
# Assign selected call group
def Assign_callgroup_assign_doctor():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Assign_callgroup_assign_doctor() module")
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select/option[16]").click()
    sleep(2)
    
    
# Assign the selected call group to the doctor
def Assign_call_group_to_docid():
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Assign_call_group_to_docid() module")
    Assign_Call_group_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[4]/td/input")
    Assign_Call_group_button.click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed during specialist already present in the group
    alert_obj.accept()
    sleep(5)
############################################################       call mapping  ############################################################

    
def Manage_Logout():
  try:
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Manage_Logout() module")
    Logout_buton=chrome_driver.find_element_by_partial_link_text('Logout');
    Logout_buton.click()
    
  ## Take Screen shot
    Take_screen_shot("Manage_Logout_screen")
  ## End Taking Screen shot
 
  except:
    pass

def Close_Application():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_Configuration.py program/Close_Application() module")
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
View_Configuration()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


