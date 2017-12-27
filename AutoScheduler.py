# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:58:38 2017

@author: p
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime, time, os
from loginSkedda import login
from pyvirtualdisplay import Display
from selenium import webdriver

def scheduleSkedda(days_from_tuesday,
                   title = "West Coast Swing Dance Social",
                   body = "Come dance the California state dance with us!"):
   
    email = os.environ['SKEDDA_UN']
    pw = os.environ['SKEDDA_PW']

    print('Initializing Headless Mode.')
    with Display(visible=0, size=(1024, 768)) as display:

        print('Initializing Webdriver.')
        driver = login(email = email, password = pw)
        print('Attempting to schedule next desired date.')
        
        today = datetime.date.today() + datetime.timedelta(days = days_from_tuesday) #move to Wedensday
        fourWeeksOut = today + datetime.timedelta(weeks = 4)
        
        bookingURL = ['https://catsrecrooms.skedda.com/booking?nbend=',
        str(fourWeeksOut),'T22%3A00%3A00-07%3A00&nbspaces=170361&nbstart=',
        str(fourWeeksOut),'T19%3A00%3A00-07%3A00&viewdate=',
        str(fourWeeksOut)]
        driver.get(''.join(bookingURL))
        
        XpathTime = "//*[@class ='col-md-12 well well-sm text-center ember-view']/h4"
        XpathTitle = "//*[@id='title']"
        XpathNotes = "//*[@id ='notes']"
        XpathButton = "//*[@class = 'btn btn-success btn-lg']"
        XpathCHK ="//*[@class = 'scheduler-time-column']"
        
        i = 0
        while True:
            try:
                Time = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathTime))
                break
            except:
                i +=1
                print('attempting to find Time element on page...try ' + str(i))
                if i > 10:
                    print('ERROR')
                    break
    
        Time = str(Time.text[23])

        if Time != str(7):
            bookingURL = ['https://catsrecrooms.skedda.com/booking?nbend=',
            str(fourWeeksOut),'T22%3A00%3A00-08%3A00&nbspaces=170361&nbstart=',
            str(fourWeeksOut),'T19%3A00%3A00-08%3A00&viewdate=',
            str(fourWeeksOut)]
            driver.get(''.join(bookingURL))

        i = 0
        while True:
            try:
                Title = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathTitle))
                Notes = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathNotes))
                Button = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathButton))
                break
            except:
                i +=1
                print('attempting to find elements on page...')
                if i > 5:
                    print('ERROR')
                    break
        
        Title.clear()
        Title.send_keys(title)
        Notes.clear()
        Notes.send_keys(body)
        Button.click()

        i = 0
        while True:
            try:
                Title = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(XpathCHK))
                print('Successfully scheduled time on Skedda!')
                break
            except:
                i+=1
                print('Waiting for confirmation...')
                if i > 5:
                    print('WARNING: No confirmation that the event has been scheduled.')
                    print('Please check to ensure that the date was properly scheduled.')
                    break
        time.sleep(5)
        driver.quit()
    print('Exiting Selenium, Firefox and Virtual Display.')
    return fourWeeksOut

if __name__ == '__main__':
    scheduleSkedda()

#URL = ['https://catsrecrooms.skedda.com/booking?nbend=', 
#    '2017-10-11T22%3A00%3A00-07%3A00&nbspaces=170361&nbstart',
#    '=2017-10-11T19%3A00%3A00-07%3A00&viewdate=2017-10-25&viewend=2017-12-14']
