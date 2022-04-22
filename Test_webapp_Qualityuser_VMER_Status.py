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

## Global Variables
chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

## end of Global Variables

def Open_Application():
    
  try:  
    print("we are inside cardiotrack webapp module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

def Login_Qualityuser():
    
  try:  
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

def View_Add_Vmer_Status():
  
    vmer_status_buton=chrome_driver.find_element_by_partial_link_text('VMER Status');
    vmer_status_buton.click()
    sleep(5)
    Add_New_Vmer_status()
    sleep(10)
    
## Search by User
    user_name_list=["P.ASHOK KUMAR","R. BALAKRISHNAN","P.RAJA"]
    ctr=0
    while ctr < len(user_name_list):
      user_name_list_arg = user_name_list[ctr]
      Search_By_Vmer_status_byName(user_name_list_arg)
      ctr +=1
             
## search by Insurer    
    Search_By_Vmer_status_byInsurer("LIC_MDIndia")

## search  by Proposal number    
    proposal_Number=[844,1050,782,1006]
    ctr=0
    while ctr < len(proposal_Number):
      proposal_number_arg = proposal_Number[ctr]
      Search_By_Vmer_status_byProposal_no(proposal_number_arg)
      ctr +=1
      
## Search by AML Calling Date
      AML_Calling_date_list=["2021-07-23","2021-07-22","2021-07-24","2021-07-20"]
      ctr=0
      while ctr< len(AML_Calling_date_list):
         AML_Calling_date_arg = AML_Calling_date_list[ctr]
         Search_By_AML_Calling_Date(AML_Calling_date_arg)
         ctr +=1
         
## Search by Order_Execution_Status
    Order_Execution_Status_list=["Order Execution Status","Pending","Attended","Show Stopper"]
    ctr=0
    while ctr < len(Order_Execution_Status_list):
             Order_Execution_Status(ctr)
             ctr +=1

## Search by Mobile number
    Mobile_Number_list=[9915628661,7305936353,9786784646,8939779053,8226911553,7717228138]
    ctr=0
    while ctr < len(Mobile_Number_list):
         Mobile_Number_arg=Mobile_Number_list[ctr]
         Search_By_Mobile_Number(Mobile_Number_arg)         
         ctr +=1         

## Search by Reponsibility
    Responsibility_list=["Reena","kashish","Nidhi","Kavya/Nidhi","Kavya","Anita/Nidhi","Anita"]
    ctr=0
    while ctr < len(Responsibility_list):
             Responsibility_arg=Responsibility_list[ctr]
             Search_By_Responsibility(Responsibility_arg)
             ctr +=1

## Search by Document_Submitted_status
    Document_Submitted_status_list=["Document Submitted","Y","N"]
    ctr=0
    while ctr < len(Document_Submitted_status_list):
             Document_Submitted_status_arg=Document_Submitted_status_list[ctr]
             Search_By_Document_Submitted_status(ctr)
             ctr +=1
  

def Search_By_Vmer_status_byName(username):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("name_ser").send_keys(username)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)
    
def Search_By_Vmer_status_byInsurer(Insurer_name):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("insurer_ser").send_keys(Insurer_name)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)

def Search_By_Vmer_status_byProposal_no(proposal_no):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("proposal_number_ser").send_keys(proposal_no)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)

def Search_By_AML_Calling_Date(aml_date):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("aml_date_ser").send_keys(aml_date)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)

def Search_By_Mobile_Number(Mobile_Number):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("mobile_number_ser").send_keys(Mobile_Number)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)

def Search_By_Responsibility(Responsibility_args):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("responsibility_ser").send_keys(Responsibility_args)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)


def Order_Execution_Status(Order_Execution_Status_ctr):
    chrome_driver.refresh()
    Order_Execution_Status_dropdown = Select(chrome_driver.find_element_by_id("order_execution_status_ser"))
    Order_Execution_Status_dropdown.select_by_index(Order_Execution_Status_ctr)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)

def Search_By_Document_Submitted_status(Document_Submitted_status_ctr):
    chrome_driver.refresh()
    Document_Submitted_status_dropdown = Select(chrome_driver.find_element_by_id("documents_uploaded_ser"))
    Document_Submitted_status_dropdown.select_by_index(Document_Submitted_status_ctr)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(5)

### switch the focus to current window
def switch_to_current_window():
    current_window_handle_vmer_status=chrome_driver.current_window_handle
    current_window_handle_vmer_status=chrome_driver.current_window_handle
    chrome_driver.switch_to_window(current_window_handle_vmer_status)
    print("\n\n current window handle is ",current_window_handle_vmer_status)   
### switch the focus to current window
    
def Add_New_Vmer_status():
    chrome_driver.refresh()
    Add_New_Vmer_status_button=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/table/tbody/tr/td[2]/input")
    Add_New_Vmer_status_button.click()
    switch_to_current_window()
    sleep(1)
  ## enter insurer name
    Insurer_name=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[1]/td/input")
    Insurer_name.send_keys("Sample Insurer Name")
    sleep(5)
  ## enter city division
    City_division=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[2]/td/input")
    City_division.send_keys("Sample City Division")
    sleep(5)
  ## enter AMl Calling Date
    Aml_calling_date=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[3]/td/input")
    Aml_calling_date.send_keys("21")
    Aml_calling_date.send_keys(Keys.ARROW_RIGHT)
    Aml_calling_date.send_keys(Keys.ARROW_LEFT)
    Aml_calling_date.send_keys("Nov")
    Aml_calling_date.send_keys(Keys.ARROW_RIGHT)
    Aml_calling_date.send_keys("2021")
    sleep(5)
  ## enter branch code
    branch_code=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[4]/td/input")
    branch_code.send_keys("Sample_Branch_code_001")
    sleep(5)
  ## enter MSP Code
    msp_code=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[5]/td/input")
    msp_code.send_keys("Sample_MSP_Code_001")
    sleep(5)
  ## Enter Proposal Number
    proposal_number=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[6]/td/input")
    proposal_number.send_keys("00000090909090")
    sleep(5)
  ## Enter Name
    Proposer_Name=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[7]/td/input")
    Proposer_Name.send_keys("Sample_Proposer_Name")
    sleep(5)
  ## Enter Contact Number
    Propose_Contact_Number=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[8]/td/input")
    Propose_Contact_Number.send_keys("8867867878787")
    sleep(5)
  ## Enter Phone Type
    Phone_Type=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[9]/td/input")
    Phone_Type.send_keys("Mobile")
    sleep(5)
  ## Enter CountryCode
    Country_Code=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[11]/td/input")
    Country_Code.send_keys(91)
    sleep(5)
  ## Enter Alternate Number
    Alternate_Number=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[12]/td/input")
    Alternate_Number.send_keys("6656556565")
    sleep(5)
  ## Enter Language
    Language=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[13]/td/input")
    Language.send_keys("English")
    sleep(5)
  ## Enter Type
    Type=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[14]/td/input")
    Type.send_keys("Sample Type")
    sleep(5)
  ## Enter Propose Date
    Propose_Date=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[15]/td/input")
    Propose_Date.send_keys("21")
    Propose_Date.send_keys(Keys.ARROW_RIGHT)
    Propose_Date.send_keys(Keys.ARROW_LEFT)
    Propose_Date.send_keys("Dec")
    Propose_Date.send_keys(Keys.ARROW_RIGHT)
    Propose_Date.send_keys("2021")
    sleep(5)
  ## Enter Propose Time
    Propose_Time=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[16]/td/input[1]")
    Propose_Time.send_keys("10")
    Propose_Time.send_keys(Keys.ARROW_RIGHT)
    Propose_Time.send_keys(Keys.ARROW_LEFT)
    Propose_Time.send_keys("10")
    Propose_Time.send_keys(Keys.ARROW_RIGHT)
    Propose_Time.send_keys("AM")
    sleep(5)
  ## Enter Reponsibility
    Responsibility=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[17]/td/select").click()
    Responsibility=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[17]/td/select")
    Responsibility.send_keys(Keys.DOWN)
    Responsibility.send_keys(Keys.DOWN)
    Responsibility.send_keys(Keys.DOWN)
    Responsibility.send_keys(Keys.DOWN)
    Responsibility.send_keys(Keys.DOWN)
    Responsibility.send_keys(Keys.DOWN)
    Responsibility.click()
    sleep(5)
    
  ## Enter Scan Id
    Scan_Id=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[18]/td/input")
    Scan_Id.send_keys("CLI01822@6@2710202115585516933")
    sleep(5)
                                       
  ## click Save Button
    Save_button=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[20]/td/input")
    Save_button.click()
    sleep(5)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
def Manage_Logout():  
  try:  
    Logout_buton=chrome_driver.find_element_by_partial_link_text('Logout');
    Logout_buton.click()
     
  except:
    pass
       

def Close_Application():
  sleep(5)   

  try:  
    chrome_driver.close()
    print(" \n\n Testing Completed.....")

  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
View_Add_Vmer_Status()
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


