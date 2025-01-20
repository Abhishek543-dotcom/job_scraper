# Job Scraper and Application Automation

## Overview

This project is designed to scrape job postings from various sources, segregate them based on relevance, match them with resumes, and automate the application process. It consists of a backend for data processing and a frontend for user interaction.

## Project Structure

### Backend (`app/backend/`)

-   **`activity_dashboard.py`**: Likely handles the backend logic for the activity dashboard.
-   **`app.py`**: Main application file, possibly for setting up a web server or API.
-   **`application_automation.py`**: Contains logic for automating job applications.
-   **`automation.py`**: General automation utilities.
-   **`automator.py`**: Core module for automation tasks.
-   **`dashboard.py`**: Backend logic for a dashboard interface.
-   **`email_automation.py`**: Handles email-related automation.
-   **`emailer.py`**: Module for sending emails.
-   **`job_scraper.py`**: Core module for scraping job postings.
-   **`job_segregation.py`**: Logic for segregating jobs based on criteria.
-   **`job_segregator.py`**: Module for job segregation tasks.
-   **`main.py`**: Main entry point for the backend application.
-   **`matcher.py`**: Core module for matching jobs with resumes.
-   **`matchers.py`**: Contains various matching algorithms.
-   **`models.py`**: Defines data models used in the application.
-   **`nlp.py`**: Natural Language Processing utilities.
-   **`requirements.txt`**: Lists the Python dependencies for the backend.
-   **`resume_matcher.py`**: Module for matching resumes to job descriptions.
-   **`resume_matching.py`**: Contains logic for resume matching.
-   **`routes.py`**: Defines API routes or web server endpoints.
-   **`scraper.py`**: Core module for web scraping.
-   **`scrapers.py`**: Contains various web scraping utilities.

### Frontend (`app/frontend/`)

-   **`activity_dashboard.py`**: Likely a script for a frontend dashboard.
-   **`index.html`**: Main HTML file for the frontend.
-   **`script.js`**: JavaScript file for frontend logic.
-   **`styles.css`**: CSS file for frontend styling.
-   **`src/`**: Contains source code for the frontend.
    -   **`App.css`**: CSS for the main application component.
    -   **`App.js`**: Main JavaScript component for the frontend.
    -   **`index.js`**: Entry point for the frontend application.
-   **`static/`**: Contains static assets.
    -   **`scripts.js`**: Additional JavaScript files.
    -   **`styles.css`**: Additional CSS files.
-   **`templates/`**: Contains HTML templates.
    -   **`index.html`**: Template for the main page.

### Static (`app/static/`)

-   **`script.js`**: JavaScript file.
-   **`scripts.js`**: Additional JavaScript files.
-   **`style.css`**: CSS file.
-   **`styles.css`**: Additional CSS files.
-   **`css/`**: Contains CSS files.
    -   **`styles.css`**: Main CSS file.
-   **`js/`**: Contains JavaScript files.
    -   **`main.js`**: Main JavaScript file.

### Templates (`app/templates/`)

-   **`base.html`**: Base HTML template.
-   **`index.html`**: Main page template.

### Configuration (`config/`)

-   **`config.json`**: Configuration file for the application.

### Utilities (`utils/`)

-   **`job_segregation.py`**: Utility for job segregation.
-   **`nlp_utils.py`**: Utility for NLP tasks.

### Root

-   **`requirements.txt`**: Lists all Python dependencies for the project.
-   **`scrape_jobs.py`**: Script for scraping jobs.

## Benefits

-   **Automated Job Scraping**: Automatically collects job postings from various sources.
-   **Job Segregation**: Filters and categorizes jobs based on user-defined criteria.
-   **Resume Matching**: Matches resumes with relevant job postings using advanced algorithms.
-   **Application Automation**: Automates the process of applying to jobs.
-   **User Dashboard**: Provides a user interface to monitor and manage the job search process.

## How to Run

1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    pip install -r app/backend/requirements.txt
    ```
2. **Run the Backend**:
    ```bash
    python app/backend/main.py
    ```
3. **Run the Frontend**:
    -   Open `app/frontend/index.html` in a web browser.
    -   Or, if the frontend is integrated with the backend, access it through the backend server.

## How to Use

1. **Configure the Application**:
    -   Modify `config/config.json` to set up parameters such as job search criteria, data sources, and automation settings.
2. **Scrape Jobs**:
    -   Run `scrape_jobs.py` to start scraping jobs based on the configuration.
3. **Segregate Jobs**:
    -   Use the job segregation features to filter and categorize the scraped jobs.
4. **Match Resumes**:
    -   Upload resumes and use the resume matching features to find relevant jobs.
5. **Automate Applications**:
    -   Configure the application automation settings and start the automated application process.
6. **Monitor Activity**:
    -   Use the dashboard to monitor the scraping, matching, and application activities.

## Additional Notes

-   Ensure that the necessary environment variables and API keys are set up if required by the application.
-   Refer to the individual modules and scripts for more specific usage instructions.
