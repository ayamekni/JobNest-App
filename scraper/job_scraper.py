from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pathlib import Path
from pymongo import MongoClient
from bs4 import BeautifulSoup
import time
import random
from dotenv import load_dotenv
from os import getenv
import traceback



load_dotenv()


MONGO_URL=getenv("MONGO_URL")
SCRAPING_URL=getenv("SCRAPING_URL")
WEBDRIVER_URL=getenv("WEBDRIVER_URL")

# Define max number of pages to be scraped
MAX_PAGES_NB = 10

# Function to generate a random user-agent
def generate_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    ]
    return random.choice(user_agents)

# MongoDB setup
client = MongoClient(MONGO_URL)
db = client['job_database']  # Replace with your database name
collection = db['jobs']  # Replace with your collection name

# # Set up Edge options for headless operation
options = EdgeOptions()
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument("profile-directory=Profile 1")
options.add_argument(f"user-agent={generate_random_user_agent()}")

# service=EdgeService(WEBDRIVER_URL)
service=EdgeService(Path(WEBDRIVER_URL).as_posix())

# Initialize the WebDriver
try:
    driver = webdriver.Edge(
    service=service,
    options=options
    )

    # Each page contains 10 jobs
    page_nb=0
    while page_nb < MAX_PAGES_NB:
        url = SCRAPING_URL + f"&page={page_nb}"
    
        driver.get(url)
        print("got url")
        # Wait for the page to load
        # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        time.sleep(5)  # Additional delay for dynamic content

        # Get page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup.prettify())  # Inspect the structure of the HTML if needed

        # Scrape job listings
        # jobs = soup.find_all('div', class_="flex flex-col items-start gap-4 font-inter lg:flex-row")  # Update selector as necessary
        jobs=soup.find_all('section', class_="relative overflow-clip")
        print(f"NB of jobs: {len(jobs)}")
        if not jobs:
            print("No jobs found with this selector.")
        else:
            for job in jobs:
                # Extract job title
                title_element = job.find('a', class_="mr-11 line-clamp-2 text-base font-bold text-gray-800 transition-colors duration-200 hover:underline group-hover:text-secondary-ex dark:text-white md:text-lg")  # Replace with the actual class for company name 
                title = title_element.text.strip() if title_element else "N/A"

                # Extract company name and location
                company_and_location_element = job.find('p', class_="text-xs text-gray-500")  # Replace with the actual class for job title   
                company_and_location = tuple(company_and_location_element.text.strip().split(" - ")) if company_and_location_element else "N/A"
                company=company_and_location[0] if len(company_and_location)>0 else "N/A"
                location=company_and_location[1] if len(company_and_location)>1 else "N/A"

                # Extract description
                description_element=job.find('p', class_="mb-2 text-sm font-medium text-gray-700")
                description=description_element.text.strip() if description_element else "N/A"

                # Insert into MongoDB
                job_data = {'title': title, 'company': company, 'location': location, 'description': description, 'type': 'internship'}
                match_query={'title' : title,'company': company, 'location': location, 'type':'internship'}
                collection.replace_one(match_query, job_data, upsert=True)

                # Print for debugging
                print(f"Inserted job: Title - {title}, Company - {company}, Location - {location}, Description - {description}")
            # else:
            #     print("Error: Missing data for a job.")

        # Go to the next page    
        page_nb += 1
        
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
else:
    driver.quit()
