import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from app.backend.resume_parsing import ResumeParser

class ApplicationAutomator:
    def __init__(self, resume_path, driver_path):
        self.resume_path = resume_path
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.resume_parser = ResumeParser(resume_path)

    def find_application_link(self, job_url):
        self.driver.get(job_url)
        try:
            apply_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
            )
            apply_button.click()
            application_link = self.driver.current_url
            return application_link
        except (NoSuchElementException, TimeoutException):
            return None

    def fill_application_form(self, application_link):
        self.driver.get(application_link)
        try:
            # Example form fields
            first_name_field = self.driver.find_element(By.NAME, "first_name")
            last_name_field = self.driver.find_element(By.NAME, "last_name")
            email_field = self.driver.find_element(By.NAME, "email")
            resume_upload_field = self.driver.find_element(By.NAME, "resume")

            resume_data = self.resume_parser.parse_resume()
            first_name_field.send_keys(resume_data['first_name'])
            last_name_field.send_keys(resume_data['last_name'])
            email_field.send_keys(resume_data['email'])
            resume_upload_field.send_keys(self.resume_path)

            submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
            submit_button.click()
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def close_driver(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    resume_path = "path/to/your/resume.pdf"
    driver_path = "path/to/chromedriver"
    job_url = "https://example.com/job-posting"

    automator = ApplicationAutomator(resume_path, driver_path)
    application_link = automator.find_application_link(job_url)
    if application_link:
        success = automator.fill_application_form(application_link)
        if success:
            print("Application submitted successfully.")
        else:
            print("Failed to submit application.")
    else:
        print("Could not find application link.")
    automator.close_driver()
