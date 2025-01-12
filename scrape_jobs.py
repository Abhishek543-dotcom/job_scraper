import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_utils import setup_driver
from utils.nlp_utils import match_resume_to_job
from config import Config

def scrape_jobs(platform):
    driver = setup_driver()
    driver.get(platform)
    
    # Example: Scrape job titles, companies, and locations
    job_titles = driver.find_elements(By.CSS_SELECTOR, '.job-title')
    companies = driver.find_elements(By.CSS_SELECTOR, '.company-name')
    locations = driver.find_elements(By.CSS_SELECTOR, '.location')
    
    jobs = []
    for title, company, location in zip(job_titles, companies, locations):
        jobs.append({
            'title': title.text,
            'company': company.text,
            'location': location.text
        })
    
    driver.quit()
    return jobs

def main():
    config = Config()
    platforms = [config.LINKEDIN_URL, config.NAUKRI_URL, config.GOOGLE_JOBS_URL]
    all_jobs = []
    for platform in platforms:
        jobs = scrape_jobs(platform)
        all_jobs.extend(jobs)
    
    # Save jobs to CSV
    df = pd.DataFrame(all_jobs)
    df.to_csv('data/jobs.csv', index=False)

if __name__ == "__main__":
    main()
