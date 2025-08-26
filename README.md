# JobNest: Your Career Starts in the Nest

JobNest is a web application designed to connect IT professionals and students to job and internship opportunities. It features real-time job scraping, user registration, and personalized application tracking in a modern, user-friendly interface.


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)


<img width="1919" height="834" alt="Screenshot 2025-07-14 172455" src="https://github.com/user-attachments/assets/0228276e-b368-4b5a-9588-6a2f23c9ae6a" />
<img width="1919" height="902" alt="Screenshot 2025-07-14 172523" src="https://github.com/user-attachments/assets/89a8d55c-5aa1-4644-b8e5-c8649e55a253" />
<img width="1918" height="898" alt="Screenshot 2025-07-14 172555" src="https://github.com/user-attachments/assets/64836c33-662e-4340-803a-da8610ca46f4" />

<img width="1919" height="892" alt="Screenshot 2025-07-14 172617" src="https://github.com/user-attachments/assets/821670b1-d5bc-44f7-b17c-538c44669f16" />

## Features
- **Real-Time Job Scraping**: Automatically fetch job and internship opportunities from various platforms.
- **Dynamic Filters**: Filter opportunities by type (Job/Internship) and location.
- **User Management**: Register, log in, and manage your applications.
- **Application Tracking**: Submit applications and track their status directly through the platform.

---

## Project Structure

```plaintext
JobNest/
├── app/
│   ├── templates/        # HTML templates for rendering views
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── apply.html
│   │   └── application_success.html
│   ├── static/           # Static files (CSS, images, etc.)
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── images/
│   │       └── Jobnest.png
│   ├── app.py            # Main Flask application
│   └── __init__.py       # Initializes the Flask app (if using blueprints)
├── scraper/              # Web scraping scripts
│   └── job_scraper.py    # LinkedIn job scraping script
├── venv/                 # Virtual environment (not uploaded to GitHub)
├── .gitignore            # Ignored files and directories
└── README.md             # Project documentation
```

---

## Setup and Installation

### Prerequisites
1. Install [Python](https://www.python.org/) (version 3.8 or later).
2. Install [Git](https://git-scm.com/).
3. Install a web browser's WebDriver (e.g., ChromeDriver or EdgeDriver).

### Steps to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ayamekni/JobNest-App.git
   cd JobNest-App
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:
  - Copy the example.env file and rename it to .env.
  - Add your own variables in the .env file:
    ```bash
   SCRAPING_URL=https://hi-interns.com/internships?facets=%5B%22Company.City%22%2C%22Keywords.Value%22%5D&facetFilters=%5B%5B%22Keywords.Value%3APython%22%5D%5D
   WEBDRIVER_URL=
   # MongoDB Configuration
   MONGO_URL=
   DB_NAME=
   COLLECTION_NAME=
   # LinkedIn login credentials (replace with your own)
   USERNAME=
   PASSWORD=
   # LinkedIn job search base URL
   BASE_URL=https://www.linkedin.com/jobs/search/?keywords={}&location=Tunisia
    ```
6. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will run on `http://127.0.0.1:5000`.

7. **Run the Scraper**:
   To fetch job listings:
   ```bash
   python scraper/job_scraper.py
   python scraper/job_scraperlinkedin.py
   ```

---

## How to Use
1. Visit the home page to explore jobs and internships.
2. Use filters to refine opportunities by type or location.
3. Register or log in to apply for positions.
4. Submit your application and track its status.

---

## Commands Summary
| Command                          | Description                                |
|----------------------------------|--------------------------------------------|
| `git clone <repo_url>`           | Clone the repository                       |
| `python -m venv venv`            | Create a virtual environment               |
| `.venv\Scripts\activate`         | Activate the virtual environment (Windows) |
| `source venv/bin/activate`       | Activate the virtual environment (Linux/Mac)|
| `pip install -r requirements.txt`| Install project dependencies              |
| `python app.py`                  | Run the Flask web application             |
| `python scraper/job_scraper.py`  | Run the job scraper                       |

---

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or suggestions, please contact:
- **Email**: aya.mekni10@gmail.com
- **GitHub**: (https://github.com/ayamekni)
```

