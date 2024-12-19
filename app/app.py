from flask import Flask, render_template, request
from pymongo import MongoClient
import re  # Import regex
from datetime import datetime
from flask import flash, redirect, url_for, session
from dotenv import load_dotenv
from os import getenv




app = Flask(__name__)
app.secret_key = "secret_key"

load_dotenv()


MONGO_URL=getenv("MONGO_URL")
DB_NAME =getenv("DB_NAME")
COLLECTION_NAME=getenv("COLLECTION_NAME")


client = MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
users_collection = db["users"]  # Collection for users


@app.route("/")
def home():
    # Filtering based on job type
    #job_type = request.args.get("job_type", "All")
    #query = {} if job_type == "All" else {"type": job_type}
    
    
    # Get filter values from query parameters
    job_type = request.args.get("job_type", "All")
    location = request.args.get("location", "All")

    # Build the query dynamically to allow independent filters
    query = {}
    if job_type != "All":
        query["type"] = {"$regex": f"^{job_type}$", "$options": "i"}  # Case-insensitive filter
    if location != "All":
        query["location"] = location  # Exact match for location

    # Fetch unique locations for the filter dropdown
    locations = collection.distinct("location")  # Dynamically fetch unique locations from MongoDB
    

    # Pagination setup
    page = int(request.args.get("page", 1))
    per_page = 8
    skip_jobs = (page - 1) * per_page

    # Fetch jobs with filtering and pagination
    jobs = list(collection.find(query, {"_id": 0}).skip(skip_jobs).limit(per_page))
    total_jobs = collection.count_documents(query)
    total_pages = (total_jobs + per_page - 1) // per_page  # Calculate total pages


    user = session.get("user")  # Get the logged-in user's name from the session
    
    return render_template(
        "home.html",
        jobs=jobs,
        job_type=job_type,
        location=location,
        locations=locations,  # Pass the unique locations
        page=page,
        total_pages=total_pages,
        user=user
    )
   

  
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user already exists
        if users_collection.find_one({"email": email}):
            flash("Email already registered!", "danger")
            return redirect(url_for("register"))

        # Insert new user into the database (plaintext password - insecure)
        users_collection.insert_one({"name": name, "email": email, "password": password})
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user exists and password matches
        user = users_collection.find_one({"email": email})
        if user and user["password"] == password:
            session["user"] = user["name"]
            flash("Logged in successfully!", "success")

            # Redirect to the original destination or home if no next parameter
            next_url = request.args.get("next")
            return redirect(next_url or url_for("home"))
        else:
            flash("Invalid email or password!", "danger")

    # Pass the 'next' parameter to the login form
    next_url = request.args.get("next", "")
    return render_template("login.html", next=next_url)

@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove the user's session
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

@app.route("/apply", methods=["GET", "POST"])
def apply():
    # Check if user is logged in
    if "user" not in session:
        flash("Please log in to apply for this job.", "warning")
        # Redirect to login and pass the next URL as a parameter
        return redirect(url_for("login", next=request.url))

    if request.method == "POST":
        # Process the form data
        name = request.form.get("name")
        email = request.form.get("email")
        cover_letter = request.form.get("cover_letter")
        job_title = request.form.get("job_title")

        # Debugging output
        print(f"Application received for {job_title}: Name={name}, Email={email}, Cover Letter={cover_letter}")

        # Redirect to a confirmation or success page
        return render_template("application_success.html", job_title=job_title)

    # Render the form page
    job_title = request.args.get("title", "Unknown Job")
    return render_template("apply.html", job_title=job_title)



if __name__ == "__main__":
    app.run(debug=True)
