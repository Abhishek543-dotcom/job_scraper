import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class JobAutomator:
    def __init__(self, driver_path, resume_path):
        self.driver_path = driver_path
        self.resume_path = resume_path
        self.driver = None

    def setup_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def find_application_link(self, job_url):
        self.driver.get(job_url)
        try:
            apply_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
            )
            apply_button.click()
            time.sleep(2)
            application_link = self.driver.current_url
            return application_link
        except (NoSuchElementException, TimeoutException):
            return None

    def fill_application_form(self, application_url, user_details):
        self.driver.get(application_url)
        for field, value in user_details.items():
            try:
                input_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, field))
                )
                input_field.send_keys(value)
            except (NoSuchElementException, TimeoutException):
                continue

    def upload_resume(self):
        try:
            file_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            file_input.send_keys(os.path.abspath(self.resume_path))
        except (NoSuchElementException, TimeoutException):
            pass

    def submit_application(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
            )
            submit_button.click()
        except (NoSuchElementException, TimeoutException):
            pass

    def close_driver(self):
        if self.driver:
            self.driver.quit()
