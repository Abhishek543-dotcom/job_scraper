from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class JobScraper:
    def __init__(self, driver_path):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_linkedin(self, query, location):
        self.driver.get('https://www.linkedin.com/jobs')
        search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search"]')))
        search_box.send_keys(f'{query} {location}')
        search_box.send_keys(Keys.RETURN)

        job_listings = []
        while True:
            try:
                job_elements = self.driver.find_elements(By.XPATH, '//li[contains(@class, "jobs-search-results__list-item")]')
                for job_element in job_elements:
                    title = job_element.find_element(By.XPATH, './/h3[contains(@class, "job-card-list__title")]').text
                    company = job_element.find_element(By.XPATH, './/h4[contains(@class, "job-card-container__company-name")]').text
                    location = job_element.find_element(By.XPATH, './/span[contains(@class, "job-card-container__metadata-item")]').text
                    link = job_element.find_element(By.XPATH, './/a[contains(@class, "job-card-list__title")]').get_attribute('href')
                    job_listings.append({
                        'title': title,
                        'company': company,
                        'location': location,
                        'link': link
                    })
                next_button = self.driver.find_element(By.XPATH, '//button[contains(@aria-label, "Next")]')
                next_button.click()
                time.sleep(2)
            except (NoSuchElementException, TimeoutException):
                break

        self.driver.quit()
        return job_listings

    def scrape_naukri(self, query, location):
        self.driver.get('https://www.naukri.com/')
        search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="qsb-keyword-sugg"]')))
        search_box.send_keys(query)
        location_box = self.driver.find_element(By.XPATH, '//input[@id="qsb-location-sugg"]')
        location_box.send_keys(location)
        search_box.send_keys(Keys.RETURN)

        job_listings = []
        while True:
            try:
                job_elements = self.driver.find_elements(By.XPATH, '//article[contains(@class, "jobTuple")]')
                for job_element in job_elements:
                    title = job_element.find_element(By.XPATH, './/a[contains(@class, "title")]').text
                    company = job_element.find_element(By.XPATH, './/a[contains(@class, "subTitle")]').text
                    location = job_element.find_element(By.XPATH, './/li[contains(@class, "location")]').text
                    link = job_element.find_element(By.XPATH, './/a[contains(@class, "title")]').get_attribute('href')
                    job_listings.append({
                        'title': title,
                        'company': company,
                        'location': location,
                        'link': link
                    })
                next_button = self.driver.find_element(By.XPATH, '//a[contains(@class, "fright fs14 btn-secondary br2")]')
                next_button.click()
                time.sleep(2)
            except (NoSuchElementException, TimeoutException):
                break

        self.driver.quit()
        return job_listings

    def scrape_google_jobs(self, query, location):
        self.driver.get('https://www.google.com/search?q=jobs+in+{}+{}'.format(query, location))
        job_listings = []
        while True:
            try:
                job_elements = self.driver.find_elements(By.XPATH, '//div[contains(@class, "PwjeAc")]')
                for job_element in job_elements:
                    title = job_element.find_element(By.XPATH, './/div[contains(@class, "BjJfJf PUpOsf")]').text
                    company = job_element.find_element(By.XPATH, './/div[contains(@class, "vNEEBe")]').text
                    location = job_element.find_element(By.XPATH, './/div[contains(@class, "Qk80Jf")]').text
                    link = job_element.find_element(By.XPATH, './/a[contains(@class, "vNLQIc")]').get_attribute('href')
                    job_listings.append({
                        'title': title,
                        'company': company,
                        'location': location,
                        'link': link
                    })
                next_button = self.driver.find_element(By.XPATH, '//a[contains(@id, "pnnext")]')
                next_button.click()
                time.sleep(2)
            except (NoSuchElementException, TimeoutException):
                break

        self.driver.quit()
        return job_listings
