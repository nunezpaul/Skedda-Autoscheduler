import datetime

from config import Config
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class MyFirefoxOptions(FirefoxOptions):
    def __init__(self):
        super(MyFirefoxOptions, self).__init__()
        self.add_argument('--disable-extensions')
        self.add_argument('--headless')
        self.add_argument('--disable-gpu')
        self.add_argument('--no-sandbox')


class SkeddaBase(object):
    def __init__(self, debug):
        self.img_counter = 0
        self.debug = debug

    def save_screenshot(self):
        print(self)
        if self.debug:
            self.driver.save_screenshot(f'test{self.img_counter}.png')
            print(f'screenshot {self.img_counter} saved!')
            self.img_counter += 1


class SkeddaLogin(SkeddaBase):
    def __init__(self, debug, username, password, display, **kwargs):
        super(SkeddaLogin, self).__init__(debug=debug)
        self.username = username
        self.password = password

        # All constants for the logging in processes
        self.login_url = \
            'https://www.skedda.com/account/login?returnUrl=https%3A%2F%2Fcatsrecroomsskedda.com%2Fbooking'
        self.username_name = 'username'
        self.password_name = 'password'
        self.button_xpath = "//*[@type = 'submit']"

        self.driver = webdriver.Firefox(options=None if display else MyFirefoxOptions())
        self.driver.set_window_size(width=1200, height=1200)
        self.driver.implicitly_wait(10)
        print('Attempting to login...')
        self.login()
        print('Successfully logged into Skedda!')

    def login(self):
        # Go to login page
        self.driver.get(self.login_url)
        self.save_screenshot()

        # Find the elements on login page
        username_element = self.driver.find_element_by_name(self.username_name)
        password_element = self.driver.find_element_by_name(self.password_name)
        submit_button = self.driver.find_element_by_xpath(self.button_xpath)
        self.save_screenshot()

        # Interact with the elements on login page
        username_element.send_keys(self.username)
        password_element.send_keys(self.password)
        submit_button.click()
        self.save_screenshot()


class SkeddaSchedule(SkeddaLogin):
    def __init__(self, num_weeks_away, num_days_away, title, body, debug, username, password, submit, display):
        super(SkeddaSchedule, self).__init__(username=username, password=password, debug=debug, display=display)
        # How many days in the future to make a booking
        self.time_offset = str(datetime.date.today() + datetime.timedelta(weeks=num_weeks_away, days=num_days_away))

        # Construct the appropriate booking url
        self.booking_url = [
            f'https://catsrecrooms.skedda.com/booking?nbend={self.time_offset}' \
            + f'T22%3A00%3A00-07%3A00&nbspaces=170361&nbstart={self.time_offset}' \
            + f'T19%3A00%3A00-07%3A00&viewdate={self.time_offset}',
            f'https://catsrecrooms.skedda.com/booking?nbend={self.time_offset}' \
            + f'T22%3A00%3A00-08%3A00&nbspaces=170361&nbstart={self.time_offset}' \
            + f'T19%3A00%3A00-08%3A00&viewdate={self.time_offset}']
        print(self.booking_url)

        # element identifiers
        self.time_id = 'booking-create-start-time'
        self.title_id = 'booking-modal-title'
        self.notes_id = 'booking-modal-notes'
        # self.button_xpath = '//*[@class="modal-header border-primary bg-primary text-white"]'
        self.button_xpath = '//*[@class="btn btn-success"]'


        print('Attempting to find correct scheduling page...')
        self.find_correct_page()
        print('Successfully found correct scheduling page!')
        notes_element = self.fill_in_fields(title, body)
        if submit:
            self.submit_scheduling(notes_element)
            print('Successfully submitted!')
        else:
            print('Practice run successful.')
            if self.debug:
                print('Debug images are available. File names are:')
                for i in range(self.img_counter):
                    print(f'test{i}.png')
            else:
                print('Debug was not enabled so no outputs available. Provide --debug to turn on debug mode.')


    def find_correct_page(self):
        print('Navigating to calendar...')
        self.driver.get(self.booking_url[-1])
        for i in range(5):
            if i % 4 == 0:
                self.save_screenshot()
            print(f'sleeping for {i + 1} seconds...')
            sleep(1)
        time_element = self._wait_for_element_by_id(self.time_id)

        if str(7) not in str(time_element.text):
            self.driver.get(self.booking_url[1])
            self._wait_for_element_by_id(self.time_id)
        self.save_screenshot()

    def fill_in_fields(self, title, body):
        # Find elements on page
        title_element = self.driver.find_element_by_id(self.title_id)
        notes_element = self.driver.find_element_by_id(self.notes_id)

        # Interact with elements on scheduling page
        for text, element in zip((title, body), (title_element, notes_element)):
            element.clear()
            element.send_keys(text)
        self.save_screenshot()
        return notes_element

    def _wait_for_element_by_id(self, element_id):
        repeat = 0
        while True:
            try:
                print('Searching for element on page...')
                element = WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.find_element_by_id(element_id))
                print('Found element!')
                break
            except TimeoutException:
                self.save_screenshot()
                self.driver.get(self.driver.current_url)
                repeat += 1
                if repeat > 20:
                    print('Cannot find element')
                    exit()

        self.save_screenshot()
        return element

    def submit_scheduling(self, notes_element):
        self.save_screenshot()
        notes_element.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
        self.save_screenshot()

        for i in range(10):
            if i % 9 == 0:
                self.save_screenshot()
            print(f'sleeping for {i + 1} seconds...')
            sleep(1)
        return self.time_offset


if __name__ == '__main__':
    config = Config()
    skedda = SkeddaSchedule(**config.params)
    for i in range(10):
        if i % 9 == 0:
            skedda.save_screenshot()
        print(f'sleeping for {i + 1} seconds...')
        sleep(1)
    skedda.driver.quit()