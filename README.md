# JobNest: Your Career Starts in the Nest

JobNest is a web application designed to connect IT professionals and students to job and internship opportunities. It features real-time job scraping, user registration, and personalized application tracking in a modern, user-friendly interface.

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

5. **Set Up MongoDB**:
   - Install MongoDB and ensure it is running locally or use a cloud MongoDB instance.
   - Update the `MONGO_URI` in `app.py` if needed.

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

