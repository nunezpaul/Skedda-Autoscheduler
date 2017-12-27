# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:32:50 2017

@author: p
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

def login(email = os.environ['SKEDDA_UN'], password = os.environ['SKEDDA_PW']):
    driver = webdriver.Firefox()
    
    loginURL = ['https://www.skedda.com/account/login?',
                'returnUrl=https%3A%2F%2Fcatsrecrooms',
                '.skedda.com%2Fbooking']  
                
    driver.get(''.join(loginURL))
    
    XpathUN = "//input[@name='UserName']"
    XpathPW = "//input[@name='Password']"
    XpathBTN ="//*[@type = 'submit']"
    XpathRMBR="//input[@id='RememberMe']"
    XpathCHK ="//*[@class = 'scheduler-time-column']"
    
    i = 0
    while True:
        try:
            UN = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathUN))
            PW = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathPW))
            BTN =WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathBTN))
            RMBR=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathRMBR))
            break
        except:
            i +=1
            print('Attempting to find login page...')
            if i > 10:
                break

    RMBR.click()
    UN.clear()
    UN.send_keys(email)
    PW.clear()
    PW.send_keys(password)
    BTN.click()

    i = 0
    while True:
        try:
            CHK =WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathCHK))
            print 'Successfully logged in to Skedda!'
            break
        except:
            i+=1
            print('Waiting for login to complete...')
            if i > 10:
                print('WARNING: After 10 attempts, no clear sign that login finished.')
                print('Attempting to move forward to see if this is not an issue.)')
                break
    return driver
                      
if __name__ == '__main__':
    login()
                      
