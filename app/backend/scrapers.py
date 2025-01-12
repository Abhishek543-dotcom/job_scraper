from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_linkedin_jobs():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.linkedin.com/jobs")
    time.sleep(5)  # Wait for the page to load

    job_elements = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
    jobs = []

    for job_element in job_elements:
        title = job_element.find_element(By.CSS_SELECTOR, ".job-card-list__title").text
        company = job_element.find_element(By.CSS_SELECTOR, ".job-card-container__company-name").text
        location = job_element.find_element(By.CSS_SELECTOR, ".job-card-container__metadata-item").text
        description = job_element.find_element(By.CSS_SELECTOR, ".job-card-container__description").text
        application_link = job_element.find_element(By.CSS_SELECTOR, ".job-card-container__apply-button").get_attribute("href")
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "description": description,
            "application_link": application_link
        })

    driver.quit()
    return jobs

def scrape_naukri_jobs():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.naukri.com")
    time.sleep(5)  # Wait for the page to load

    job_elements = driver.find_elements(By.CSS_SELECTOR, ".jobTuple")
    jobs = []

    for job_element in job_elements:
        title = job_element.find_element(By.CSS_SELECTOR, ".title").text
        company = job_element.find_element(By.CSS_SELECTOR, ".subTitle").text
        location = job_element.find_element(By.CSS_SELECTOR, ".loc").text
        description = job_element.find_element(By.CSS_SELECTOR, ".job-description").text
        application_link = job_element.find_element(By.CSS_SELECTOR, ".title").get_attribute("href")
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "description": description,
            "application_link": application_link
        })

    driver.quit()
    return jobs

def scrape_google_jobs():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.google.com/search?q=jobs")
    time.sleep(5)  # Wait for the page to load

    job_elements = driver.find_elements(By.CSS_SELECTOR, ".job-card-list")
    jobs = []

    for job_element in job_elements:
        title = job_element.find_element(By.CSS_SELECTOR, ".job-card-list__title").text
        company = job_element.find_element(By.CSS_SELECTOR, ".job-card-list__company-name").text
        location = job_element.find_element(By.CSS_SELECTOR, ".job-card-list__metadata-item").text
        description = job_element.find_element(By.CSS_SELECTOR, ".job-card-list__description").text
        application_link = job_element.find_element(By.CSS_SELECTOR, ".job-card-list__apply-button").get_attribute("href")
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "description": description,
            "application_link": application_link
        })

    driver.quit()
    return jobs
