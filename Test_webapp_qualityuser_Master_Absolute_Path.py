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
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Open_Application() module")
    print("we are inside cardiotrack webapp module")
    chrome_driver.get('https://gcptest.cardiotrack.info/CardioTrack/logOut')
    chrome_driver.maximize_window()
  except:
    pass

    
def Login_Qualityuser():
    
  try:
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Login_Qualityuser() module")
    username_field=chrome_driver.find_element_by_name("userName")
    password_field = chrome_driver.find_element_by_id("password")
    submit_button = chrome_driver.find_element_by_id("edit-submit")
    username_data="qualityuser1"
    password_data="password1234"
    username_field.send_keys(username_data)
    password_field.send_keys(password_data)
    submit_button.click()
    sleep(2)
    
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

def View_Patient_Report_by_Review_status():
  try:  
## start - searching reports based upon query
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/View_Patient_Report_by_Review_status() module")
    display_review_status_reports_byquery("Test CTO06219an0048")
    display_review_status_reports_byquery("Test Telemedicine Webapp Changes Mer Download")
    display_review_status_reports_byquery("Test Specialist 75 Run4")
    display_review_status_reports_byquery("Link Call Test 5")
    display_review_status_reports_byquery("Test Webapp Run5")     
## end- searching reports based upon query
    
    print(" we are displaying the reports by review status = Pending submission from doctor")
    review_status_dropdown = Select(chrome_driver.find_element_by_id("review_status"))
    review_status_dropdown.select_by_index(1)
    sleep(10)
## Navigate and display each page of Report list - tested code out here
    # Patient_report_Next_button_status(chrome_driver)
## Navigate and display each page of Report list - tested code out here
    
    sleep(10)
    
  
  ## Take Screen shot
    Take_screen_shot("Pending_submission_from_doctor_Report")   
  ## End Taking Screen shot
    
    print(" we are displaying the reports by review status = Pending")
    review_status_dropdown = Select(chrome_driver.find_element_by_id("review_status"))
    review_status_dropdown.select_by_index(2)
    sleep(10)
    
  ## Take Screen shot
    Take_screen_shot("Pending_Reports")   
  ## End Taking Screen shot
    print(" we are displaying the reports by review status = Under Review")
    review_status_dropdown = Select(chrome_driver.find_element_by_id("review_status"))
    review_status_dropdown.select_by_index(3)
    sleep(10)

  ## Take Screen shot
    Take_screen_shot("Under_Review_Reports")  
  ## End Taking Screen shot
    print(" we are displaying the reports by review status = Review Completed")
    review_status_dropdown = Select(chrome_driver.find_element_by_id("review_status"))
    review_status_dropdown.select_by_index(4)
    sleep(10)

  ## Take Screen shot
    Take_screen_shot("Review_Completed_Report")   
  ## End Taking Screen shot
    
    screen_label=chrome.driver.find_element_by_id("MER Patient Summary")
    assert screen_label == "MER Patient Summary"
    
  except AssertionError:

    print("Assertion failed. Actual value is %s" % screen_label)

  except:
     pass
#################### Start of Manage_LabReports  ########################################    

def Manage_LabReports():
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Manage_LabReports() module")
    lab_reports_buton=chrome_driver.find_element_by_partial_link_text('Lab Report');
    lab_reports_buton.click()

## Zoylo Report
    Zoylo_report()
    Upload_Replacement_file()
## Zoylo Report
         
def Take_screen_shot(file_name):
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Take_screen_shot(file_name) module")
    Current_Page_Screenshot=Screenshot_Clipping.Screenshot()
    get_current_url = chrome_driver.current_url
    chrome_driver.get(get_current_url)
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    screenshot_img_path=Current_Page_Screenshot.full_Screenshot(chrome_driver, save_path=r'.\\Screenshots - QualityUser', image_name = date_stamp +"_ "+file_name+".png")
    print("\n",screenshot_img_path)

def Zoylo_report():
  
## Select Zoylo Report Type
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Zoylo_report() module")
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
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Upload_Replacement_file() module")
    file_select_button=chrome_driver.find_element(By.XPATH,"//input[@type='file' and @name='lab_report']")
    file_select_button.send_keys("E://Bhaskar l//Bhaskar l//CardioTrack Testing//Phyton//CardiotrackWebapp Automation//Sample Test files//CLI01822@1@31120211271622611_consolidated_report.pdf")
    sleep(10)
    Replace_file_button=chrome_driver.find_element(By.XPATH,"//input[@type='button' and @value='Replace']")
    Replace_file_button.click()

#################### End of Manage_LabReports  ########################################
    
#################### Start of View Add Vmer Status ###################################

def View_Add_Vmer_Status():
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/View_Add_Vmer_Status() module")
    chrome_driver.refresh()
    Vmer_status_button=chrome_driver.find_element(By.XPATH,"//b[text()='VMER Status']")
    Vmer_status_button.click()
    sleep(2)
    print("\n\n clicked vmer status successfully")  
    #vmer_status_buton=chrome_driver.find_element_by_partial_link_text('VMER Status');
    #vmer_status_buton.click()
    Add_New_Vmer_status()
    
    
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
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Search_By_Vmer_status_byName(username) module")
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("name_ser").send_keys(username)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)
    
def Search_By_Vmer_status_byInsurer(Insurer_name):
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Search_By_Vmer_status_byInsurer(Insurer_name) module")
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("insurer_ser").send_keys(Insurer_name)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)

def Search_By_Vmer_status_byProposal_no(proposal_no):
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Search_By_Vmer_status_byProposal_no(proposal_no) module")
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("proposal_number_ser").send_keys(proposal_no)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)

def Search_By_AML_Calling_Date(aml_date):
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Search_By_AML_Calling_Date(aml_date) module")
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("aml_date_ser").send_keys(aml_date)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)

def Search_By_Mobile_Number(Mobile_Number):
    print("\n we are inside Test_webapp_qualityuser_Master_Absolute_Path.py program/Search_By_Mobile_Number(Mobile_Number) module")
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("mobile_number_ser").send_keys(Mobile_Number)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)

def Search_By_Responsibility(Responsibility_args):
    chrome_driver.refresh()
    chrome_driver.find_element_by_id("responsibility_ser").send_keys(Responsibility_args)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)


def Order_Execution_Status(Order_Execution_Status_ctr):
    chrome_driver.refresh()
    Order_Execution_Status_dropdown = Select(chrome_driver.find_element_by_id("order_execution_status_ser"))
    Order_Execution_Status_dropdown.select_by_index(Order_Execution_Status_ctr)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)

def Search_By_Document_Submitted_status(Document_Submitted_status_ctr):
    chrome_driver.refresh()
    Document_Submitted_status_dropdown = Select(chrome_driver.find_element_by_id("documents_uploaded_ser"))
    Document_Submitted_status_dropdown.select_by_index(Document_Submitted_status_ctr)
    search_button=chrome_driver.find_element_by_class_name("btn")
    search_button.click()
    sleep(2)

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
    sleep(2)
  ## enter city division
    City_division=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[2]/td/input")
    City_division.send_keys("Sample City Division")
    sleep(2)
  ## enter AMl Calling Date
    Aml_calling_date=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[3]/td/input")
    Aml_calling_date.send_keys("21")
    Aml_calling_date.send_keys(Keys.ARROW_RIGHT)
    Aml_calling_date.send_keys(Keys.ARROW_LEFT)
    Aml_calling_date.send_keys("Dec")
    Aml_calling_date.send_keys(Keys.ARROW_RIGHT)
    Aml_calling_date.send_keys("2021")
    sleep(2)
  ## enter branch code
    branch_code=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[4]/td/input")
    branch_code.send_keys("Sample_Branch_code_001")
    sleep(2)
  ## enter MSP Code
    msp_code=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[5]/td/input")
    msp_code.send_keys("Sample_MSP_Code_001")
    sleep(2)
  ## Enter Proposal Number
    proposal_number=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[6]/td/input")
    proposal_number.send_keys("00000090909090")
    sleep(2)
  ## Enter Name
    Proposer_Name=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[7]/td/input")
    Proposer_Name.send_keys("Sample_Proposer_Name")
    sleep(2)
  ## Enter Contact Number
    Propose_Contact_Number=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[8]/td/input")
    Propose_Contact_Number.send_keys("8867867878787")
    sleep(2)
  ## Enter Phone Type
    Phone_Type=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[9]/td/input")
    Phone_Type.send_keys("Mobile")
    sleep(2)
  ## Enter CountryCode
    Country_Code=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[11]/td/input")
    Country_Code.send_keys(91)
    sleep(2)
  ## Enter Alternate Number
    Alternate_Number=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[12]/td/input")
    Alternate_Number.send_keys("6656556565")
    sleep(2)
  ## Enter Language
    Language=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[13]/td/input")
    Language.send_keys("English")
    sleep(2)
  ## Enter Type
    Type=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[14]/td/input")
    Type.send_keys("Sample Type")
    sleep(2)
  ## Enter Propose Date
    Propose_Date=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[15]/td/input")
    Propose_Date.send_keys("21")
    Propose_Date.send_keys(Keys.ARROW_RIGHT)
    Propose_Date.send_keys(Keys.ARROW_LEFT)
    Propose_Date.send_keys("Dec")
    Propose_Date.send_keys(Keys.ARROW_RIGHT)
    Propose_Date.send_keys("2021")
    sleep(2)
  ## Enter Propose Time
    Propose_Time=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[16]/td/input[1]")
    Propose_Time.send_keys("10")
    Propose_Time.send_keys(Keys.ARROW_RIGHT)
    Propose_Time.send_keys(Keys.ARROW_LEFT)
    Propose_Time.send_keys("10")
    Propose_Time.send_keys(Keys.ARROW_RIGHT)
    Propose_Time.send_keys("AM")
    sleep(2)
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
    sleep(2)
    
  ## Enter Scan Id
    Scan_Id=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[18]/td/input")
    Scan_Id.send_keys("CLI01822@1@811202114131951005")
    sleep(2)
                                       
  ## click Save Button
    Save_button=chrome_driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/form/table/tbody/tr[20]/td/input")
    Save_button.click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(5)
#################### End of View Add Vmer Status ###################################
    
#################### Start View_Doctor_Schedule ###################################    
def View_Doctor_Schedule():
  try:
    chrome_driver.refresh()
    Doctor_Schedule_button=chrome_driver.find_element(By.XPATH,"//b[text()='Doctor schedule']")
    Doctor_Schedule_button.click()	 
    sleep(2)
    print("\n\n Doctor Schedule clicked")
    #Doctor_schedule_buton=chrome_driver.find_element_by_partial_link_text('Doctor schedule');
    #Doctor_schedule_buton.click()
    #sleep(2)
    
  ## Take Screen shot
    Take_screen_shot("Doctor_schedule_Report")
  ## End Taking Screen shot

  except:
    pass
#################### End View_Doctor_Schedule ###################################
  
#################### Start View_Configuration ###################################      
def View_Configuration():
    Configuration_buton=chrome_driver.find_element_by_partial_link_text('Configuration');
    Configuration_buton.click()
    call_group()
    call_Group_Assign()
    search_Assign_specialist_button()
    search_Specialist()
    Displayed_Specialist()
    call_group_list_select_group()
    Assign_button_Assign_specialist_group()
    call_group_view_option()
    Search_call_group_docid("DOC027")
    click_search_docid()
    Search_clear_call_group_docid()
    Search_call_group_docid("DOC035")
    click_search_docid()
    Search_clear_call_group_docid()
    call_group_view_option()
    Search_records()
    Enter_Group_Id()
    Search_records()
    sleep(2)
    click_Search_Group_Id_Button()
    sleep(2)
    Search_records()
######### callmapping starts here ###################  
    Call_Mapping()
    Search_Doctor_Assign()
    Enter_Docid_Assign()
    Search_Assignment_doctor()
    Select_Assigned_Doctor_found()
    Select_call_group_doc_assign()
    Assign_callgroup_assign_doctor()
    Assign_call_group_to_docid()
    sleep(2)
    Call_Mapping()
    sleep(2)
    
## search Assign specialist button
def  search_Assign_specialist_button():   
    Search_specialist=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[1]/td[2]/input")
    Search_specialist.click()
## search Assign specialist button

## click Enter specialist id button to search for specialist for assignment
def search_Specialist():
    Check_specaialist_id=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[2]/div/div/input[1]")
    Check_specaialist_id.send_keys("DOC027")
    Specialist_details=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[2]/div/div/input[2]")
    Specialist_details.click()
    sleep(2)
## click Enter specialist id button to search for specialist for assignment

## select the displayed specialist
def Displayed_Specialist():    
    Specialist_select=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[2]/div/div/div/div/table/tbody/tr[2]/td[2]/input")
    Specialist_select.click()                                                 
## select the displayed specialist

## display call group list and select the group  
def call_group_list_select_group():    
     call_group_list=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select")
     call_group_list.click()
     Select_Group=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select/option[16]")
     Select_Group.click()
     sleep(2)
## display call group list and select the group
     
## click Assign button and assign specialist to the group
def Assign_button_Assign_specialist_group():
     Assign_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[4]/td/input")
     Assign_button.click()
     sleep(2)
     alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed during duplicate assignment of specialist to the group
     alert_obj.accept()
              
## CREATING AND ASSIGNING SPECIALIST TO THE NEW GROUP WILL BE DONE LATER

## call group View option
def call_group_view_option():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/table/tbody/tr/td[2]/label/a").click()
    
## call group View option

# clicking call group
def call_group():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/table/tbody/tr/td[1]/ul/li/a/b").click()
# clicking call group


## call group Assign option
def call_Group_Assign():    
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/table/tbody/tr/td[1]/label/a").click()
## call group Assign option
    

## search for records in call group
    
def Search_call_group_docid(doc_id):

     doc_id_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/input")
     doc_id_search.send_keys(doc_id)
## search for records in call group

## click search button to search on docid
def click_search_docid():
     docid_click_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[2]/label[1]") 
     docid_click_search.click()
     sleep(2)
## click search button to search on docid
     
def Search_clear_call_group_docid():

     doc_id_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/input")
     doc_id_search.clear()
## search for records in call group

## click Search Group ID button
def   click_Search_Group_Id_Button():
      Group_id_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[2]/input[2]")
      Group_id_button.click()
      sleep(2)
      
## enter Search criteria for group id
def Enter_Group_Id():
  
    Search_Group_Id=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/input")
    Search_Group_Id.send_keys("CONSULT_IND")

def Search_records():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr/td[2]/div/div[1]/div/div[1]/table/tbody/tr/td[3]/input").click()

    
############################################################       call mapping  ############################################################
    
def Call_Mapping():
  
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/table/tbody/tr/td[2]/ul/li/a/b").click()
    sleep(2)
    
# Serching doctor for assignment
def Search_Doctor_Assign():
  
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[1]/td[2]/input").click()
    sleep(2)
# Accept doctor id for searching
def Enter_Docid_Assign():
  
    Doctor_Id_assign=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[1]/div/div/input[1]")
    Doctor_Id_assign.send_keys("CLI01822")
    sleep(2)
# Search Doctor for assignment
def Search_Assignment_doctor():

    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[1]/div/div/input[2]").click()
    sleep(2)

# Select the Assigned found doctor
def Select_Assigned_Doctor_found():
      chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/form[1]/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
      sleep(2)
# Select Call Group
def Select_call_group_doc_assign():
     chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select").click()
     sleep(2)
# Assign selected call group
def Assign_callgroup_assign_doctor():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[3]/td[1]/select/option[16]").click()
    sleep(2)
        
# Assign the selected call group to the doctor
def Assign_call_group_to_docid():
    Assign_Call_group_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/form/table/tbody/tr[4]/td/input")
    Assign_Call_group_button.click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed during specialist already present in the group
    alert_obj.accept()
    sleep(5)
############################################################       call mapping  ############################################################
    
########### end of call mapping of Configuration option ############        
  ## Take Screen shot
    Take_screen_shot("View_Configuration_screen")
  ## End Taking Screen shot
    
#################### end of View_Configuration ###################################          
 
######## Start of Manage_MER-Mapping () ############################################################  
def Manage_MER_Mapping():
    MER_Mapping_buton=chrome_driver.find_element_by_partial_link_text('MER Mapping');
    MER_Mapping_buton.click()
    sleep(1)
    Search_scan_Id()
    enter_scan_id("CLI01822@1@911202114424314930") ## existing scan id for reassignment of the doctor
    search_given_scan_id() 
    select_scan_id()
    select_doc_id_merMapping()
    Accept_doc_id_merMapping()
    click_search_doc_id_merMapping()
    select_found_specialist()
    Reassign_specialist()
    click_new_button_merMapping()
    Search_scan_Id()
    enter_scan_id("CLI01822@1@1111202111173839407")  ## new mer scan id for assigning new doctor
    search_given_scan_id()
    select_scan_id()
    select_doc_id_merMapping()
    Accept_doc_id_merMapping()
    click_search_doc_id_merMapping()
    select_found_specialist()
    sleep(2)
    click_assign_doc_newmerMapping()
    sleep(2)
    
## Search for given scan id
def Search_scan_Id():
    print("\n we are inside ")
    scand_id_search=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input")
    scand_id_search.click()
    sleep(1)
    
## Accept or Enter scan id
def enter_scan_id(scanid):
    #//input[@type='text' and @name='scan_id']
    scan_id_entered=chrome_driver.find_element(By.XPATH,"//input[@type='text' and @name='scan_id']")
    #scan_id_entered=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[1]/div/div/input[1]")
    scan_id_entered.send_keys(scanid)
    sleep(1)

## Search for entered scan id
def search_given_scan_id():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[1]/div/div/input[2]").click()
    sleep(1)
    
## Select the found Scan id
def select_scan_id():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[1]/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
    sleep(1)

## Search and select the doc id for mer mapping
def select_doc_id_merMapping():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/input").click()
    sleep(1)
    
## Accept doc id for mer mapping
def Accept_doc_id_merMapping():
    doc_id_merMapping=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[2]/div/div/input[1]")
    doc_id_merMapping.send_keys("DOC027")
    sleep(1)
    
## click Search for doc id
def click_search_doc_id_merMapping():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[2]/div/div/input[2]").click()
    sleep(1)
    
## Select the found Specialist
def select_found_specialist():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/form[2]/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
    sleep(1)
    
## Reassign the specialist
def Reassign_specialist():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[4]/td/input[1]").click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(2)
    
### MER Mapping for newly created scan id #####
def click_new_button_merMapping():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[1]/td[1]/input[2]").click()
    sleep(2)
    
## Assign the specialist for newly mer mapped scan id
def click_assign_doc_newmerMapping():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/form/table/tbody/tr[4]/td/input[1]").click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(5)
    
#################### End of Manage_MER-Mapping  ########################################
    

#################### start of Manage_call_link    ########################################
def Manage_Call_Link():
  
    Call_Link_buton=chrome_driver.find_element_by_partial_link_text('Call Link');
    Call_Link_buton.click()
    sleep(1)
    search_call_link()
    enter_scanid_call_link()
    search_scan_id_call_link()
    select_scan_id()
    click_validity_date_call_link()
    click_validity_time_call_link()
    click_add_button_call_link()
    
  ## Take Screen shot
  ##Take_screen_shot("Manage_Call_link_screen")
  ## End Taking Screen shot
        

## accept scan id for call linking
def search_call_link():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/input").click()
    sleep(1)
    
## enter to search scan id for call linking
def enter_scanid_call_link():
    scan_id_calllink= chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/form/div/div/input[1]")
    scan_id_calllink.send_keys("CLI01822@1@1111202111173839407")  ## new scan id for creating mer call link
    sleep(1)
    
## search for the scan id - call linking
def search_scan_id_call_link():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/form/div/div/input[2]").click()
    sleep(1)

## select the patient id
def select_scan_id():
    chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/form/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
    sleep(1)

## click validity date
def click_validity_date_call_link():
    validity_date=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/input")
    validity_date.send_keys("29")
    validity_date.send_keys(Keys.ARROW_RIGHT)
    validity_date.send_keys(Keys.ARROW_LEFT)
    validity_date.send_keys("DEC")
    validity_date.send_keys(Keys.ARROW_RIGHT)
    validity_date.send_keys("2021")
    sleep(2)

## click validity time
def click_validity_time_call_link():
    validity_time=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[3]/td[1]/input")
    validity_time.send_keys("12")
    validity_time.send_keys(Keys.ARROW_RIGHT)
    validity_time.send_keys(Keys.ARROW_LEFT)
    validity_time.send_keys("12")
    validity_time.send_keys(Keys.ARROW_RIGHT)
    validity_time.send_keys("PM")
    sleep(2)

## click Add button for adding call link
def click_add_button_call_link():    
    Add_button_call_link=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr[4]/td/input")
    Add_button_call_link.click()
    sleep(2)
    alert_obj = chrome_driver.switch_to.alert # we are handling the alert that is displayed post reassignment of the specialist
    alert_obj.accept()
    sleep(5)

#################### End of Manage_call_link    ########################################

##################### start of Manage_MER_Upload()###############################################################
    
def Manage_MER_Upload():

    MER_Upload_buton=chrome_driver.find_element_by_partial_link_text('MER Upload');
    MER_Upload_buton.click()
    sleep(1)
    Pre_upload_checks_MER_Upload()
    Upload_MER_Upload()
    Post_upload_checks_MER_Upload()
    Create_Orders_MER_Upload()
    sleep(2)
    
  ## Take Screen shot
  ##  Take_screen_shot("Manage_MER_Upload_screen")
  ## End Taking Screen shot

###### start of Pre_upload_checks_MER_Upload()
    
def Pre_upload_checks_MER_Upload():
  
    Pre_upload_checks_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[1]/input")
    Pre_upload_checks_button.click()
    sleep(2)
    
###### end of Pre_upload_checks_MER_Upload()
    
###### start of  Upload MER _upload()
    
def Upload_MER_Upload():
    
    Upload_MER_upload_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[2]/input")
    Upload_MER_upload_button.click()
    sleep(2)

###### end of  Upload MER _upload()

###### start of  Post_upload_checks_MER_Upload()
def Post_upload_checks_MER_Upload():
  
    Post_upload_checks_button= chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[3]/input")
    Post_upload_checks_button.click()
    sleep(2)

###### end of  Post_upload_checks_MER_Upload()

###### start of  Create_Orders_MER_Upload()
    
def Create_Orders_MER_Upload():
  
    Create_Order_button=chrome_driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[1]/div/form/table/tbody/tr[1]/td[4]/input")
    Create_Order_button.click()
    sleep(2)

###### end of  Create_Orders_MER_Upload()
     
##################### End of Manage_MER_Upload()###############################################################

def Manage_Logout():
    chrome_driver.refresh()
    Logout_button=chrome_driver.find_element(By.XPATH,"//b[text()='Logout']").click()
    sleep(1)
    print("\n\n logged out successfully from the  app")

####################################### Start commonly called methods section ######################################################################
  
def display_review_status_reports_byquery(search_query):

#   chrome_driver.refresh()
    chrome_driver.find_element_by_id("ptname").send_keys(search_query)
    search_button=chrome_driver.find_element_by_class_name("input-group-btn")
    search_button.click()
       
   
def Take_screen_shot(file_name):

    Current_Page_Screenshot=Screenshot_Clipping.Screenshot()
    get_current_url = chrome_driver.current_url
    chrome_driver.get(get_current_url)
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    screenshot_img_path=Current_Page_Screenshot.full_Screenshot(chrome_driver, save_path=r'.\\Screenshots - QualityUser', image_name = date_stamp +"_ "+file_name+".png")
    print("\n",screenshot_img_path)


def Patient_report_Next_button_status(chrome_driver):

## Display reports list page by page
  
    chrome_driver.refresh()
    Patient_report_Next_button = chrome_driver.find_element_by_id('next1')
    print("\n",Patient_report_Next_button.is_enabled(), "\t",Patient_report_Next_button.is_displayed())
    
    if (Patient_report_Next_button.is_enabled() == True and Patient_report_Next_button.is_displayed() == True):
         Patient_report_Next_button.click()
         sleep(5)

         while (Patient_report_Next_button.is_enabled() == True and Patient_report_Next_button.is_displayed() == True):
           Patient_report_Next_button.click()
           sleep(5)
        
####################################### End of commonly called methods section ######################################################################
           

def Close_Application():
    
  try:  
    chrome_driver.close()
    print(" \n\n Testing Completed.....")
  except:
      pass


## calling the functions

Open_Application()
Login_Qualityuser()
View_Patient_Report_by_Review_status()
Manage_LabReports()
View_Add_Vmer_Status()
View_Doctor_Schedule()
Manage_Call_Link()
Manage_MER_Upload()
Manage_MER_Mapping()
View_Configuration
Manage_Logout()
Close_Application()

quit()

## end of calling the functions


