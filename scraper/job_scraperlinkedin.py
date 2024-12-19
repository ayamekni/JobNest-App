# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import time
from dotenv import load_dotenv
from os import getenv
# ---------- CONFIGURATION SECTION ----------*
load_dotenv()

# LinkedIn login credentials (replace with your own)
USERNAME=getenv("USERNAME")
  # Replace with your LinkedIn email
PASSWORD=getenv("PASSWORD")
        # Replace with your LinkedIn password

# MongoDB setup


MONGO_URL=getenv("MONGO_URL")
DB_NAME=getenv("DB_NAME")
COLLECTION_NAME=getenv("COLLECTION_NAME")



# Edge WebDriver setup
WEBDRIVER_URL=getenv("WEBDRIVER_URL")

# Keywords to search for jobs
SEARCH_JOBS = ["engineer", "data scientist", "data analyst", "data engineer"]

# LinkedIn job search base URL
BASE_URL=getenv("BASE_URL")

# ---------- FUNCTION TO SCRAPE LINKEDIN JOBS ----------

# ---------- FUNCTION TO SCRAPE LINKEDIN JOBS ----------
def scrape_linkedin_jobs():
    # Connect to MongoDB
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Configure WebDriver options
    options = Options()
    options.add_argument('--disable-webrtc')
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Initialize WebDriver
    service = Service(WEBDRIVER_URL)
    driver = webdriver.Edge(service=service, options=options)

    try:
        # Log in to LinkedIn
        print("Opening LinkedIn login page...")
        driver.get("https://www.linkedin.com/login")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))

        print("Entering login credentials...")
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.submit()

        # Wait for the homepage to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "global-nav-search"))
        )
        print("Logged in successfully.")

        # Scrape jobs for each keyword
        for search_job in SEARCH_JOBS:
            print(f"Starting job search for: {search_job}")
            search_url = BASE_URL.format(search_job)
            driver.get(search_url)

            current_page = 1
            while current_page < 10:  # Scrape up to 10 pages
                print(f"Scraping page {current_page}...")
                time.sleep(3)

                # Wait for jobs to load on the page
                WebDriverWait(driver, 40).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".job-card-container"))
                )

                # Extract job details
                jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
                print(f"Found {len(jobs)} jobs on page {current_page}.")

                for job in jobs:
                    try:
                        title = job.find_element(By.CSS_SELECTOR, '.job-card-list__title--link').text
                        company = job.find_element(By.XPATH, ".//div[@class='artdeco-entity-lockup__subtitle ember-view']/span").text
                        location_full = job.find_element(By.XPATH, ".//div[@class ='artdeco-entity-lockup__caption ember-view']/ul/li/span").text
                        link = job.find_element(By.CSS_SELECTOR, '.job-card-list__title--link').get_attribute('href')

                        # Extract only the first part of the location before the comma
                        location = location_full.split(",")[0].strip() if "," in location_full else location_full.strip()

                        # Combine description with link
                        description = f"Job posting: {link}"

                        # Only process jobs in Tunisia
                        if "tunisia" in location_full.lower():
                            job_data = {
                                "title": title,
                                "company": company,
                                "location": location if location else "N/A",  # Use the parsed location
                                "description": description,
                                "type": "job"  # Specify 'job' type
                            }

                            # Avoid duplicate entries in MongoDB
                            if not collection.find_one({"title": title, "company": company, "description": description}):
                                collection.insert_one(job_data)
                                print(f"Inserted job: {title} in {location}")
                            else:
                                print(f"Duplicate skipped: {title} in {location}")
                    except Exception as e:
                        print(f"Error scraping job: {e}")

                # Move to the next page
                current_page += 1
                next_page = driver.find_elements(By.XPATH, f"//li[@data-test-pagination-page-btn='{current_page}']/button")
                if next_page:
                    next_page[0].click()
                else:
                    print("No more pages available.")
                    break

    except Exception as e:
        print(f"Error during scraping: {e}")
    finally:
        print("Closing WebDriver...")
        driver.quit()
        print("Scraping finished.")

# ---------- RUN THE SCRAPER ----------
if __name__ == "__main__":
    scrape_linkedin_jobs()
