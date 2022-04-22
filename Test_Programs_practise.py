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
#from screenshot import Screenshot_Clipping
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

class First_class:
    @staticmethod
    def static_method(param1):
        print("\n\nwe are inside static method first class")
        ##print("value of param1 is", param1)
    def normal_method(self,name1):
        print("\n this is normal method of first class",name1)
        return
      #  return (print("\n this is normal method of first class being returned"))
        def normal_method1(self,name2):
            print("\n normal_method1 child method",name1,name2)
    def __init__(self,Number1,Name,Remark):
        self.Number1=Number1
        self.Name=Name
        self.Remark=Remark
        def inside_method():
            print("\nwe are inside the first class constructor")

class second_class(First_class):
    def __init__(self,Pass_Percentage):
      self.Pass_percentage=Pass_Percentage
    def second_class_method(Pass_percentage):
     print("we are inside second class - child class of first_class\n",Pass_percentage)

class Third_class(second_class):
    First_class.static_method(30)
    second_class.second_class_method(45)
    print(" \n we are inside third class")

class fourth_class(Third_class):
    print("\n we are inside fourth_class")


fourth_class_object=second_class(45)
fourth_class_object.second_class_method()
normal_method_returned_value=fourth_class_object.normal_method("guru")
normal_method_returned_value1=fourth_class_object.normal_method("shiva")
#print(normal_method_returned_value)
#print(normal_method_returned_value1)
