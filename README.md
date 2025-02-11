**Photography Contest Management System**

A simple, console-based system that manages photography contests, allowing participants to submit their photographs, view contest rules, and get results. The system includes basic functionality for photo submission, rules display, and judging. The judging system uses a simple rating approach.
Project Structure

**The project contains the following files and directories**:

Photography-Contest-Management-System/
├── app.py                # Main Python script to run the application logic
├── index.html            # Homepage of the contest (viewing contest details)
├── judge.html            # Judge's page for rating photos
├── results.html          # Display contest results after judging
├── submit.html           # Submission page for participants to upload their photos
├── rules.html            # Contest rules page
├── styles.css            # Styling for the HTML pages
├── data.db               # SQLite database for storing photo submissions and results
└── README.md             # Project description and usage instructions/

**Features**

    Participant Submission: Users can submit their photos along with a title and description.
    Judging System: Judges can rate submitted photos.
    Result Display: After judging, the results of the contest will be displayed on a results page.
    Rules Display: Contest participants and judges can view the official contest rules.
    Database: All data (photos, descriptions, and results) are stored in a SQLite database for easy management and retrieval.

**Setup Instructions**
1. Prerequisites

Ensure you have Python 3.x installed on your machine. You will also need the following Python libraries:

    Flask (for handling web routing and rendering HTML pages)
    SQLite3 (for database management)

You can install Flask by running:

pip install flask

SQLite comes pre-installed with Python, so no separate installation is required.
2. Running the Application

    Clone the repository or download the project files.

    In the terminal, navigate to the project folder and run:

python app.py

    Open your browser and go to http://127.0.0.1:5000/ to start using the Photography Contest Management System.

3. Pages

    Homepage (index.html): Displays contest information and navigation links.
    Submit Page (submit.html): Allows participants to submit their photos, titles, and descriptions.
    Rules Page (rules.html): Displays the official contest rules.
    Judge Page (judge.html): Judges can rate submitted photos.
    Results Page (results.html): Shows the results after the contest has been judged.

**Database (data.db)**

The database file data.db stores:

    Photo submissions: Each participant’s photo title, description, and file name.
    Ratings: Each judge’s ratings for each photo.

**Example Usage**

    Participant Submission: Navigate to the submit page (submit.html) and upload your photo with a title and description.
    Judging: Judges can go to the judge.html page, view photos, and rate them.
    Viewing Results: After the contest ends, visit the results.html page to view the scores.

**File Descriptions**

    app.py: The main Python script that handles routing, database connections, and application logic.
    index.html: A simple landing page with contest details and links to other pages.
    judge.html: The judge’s interface to rate photos.
    results.html: Displays the final contest results based on the ratings provided by judges.
    submit.html: The page where participants submit their photos, titles, and descriptions.
    rules.html: Displays the contest rules.
    styles.css: The CSS file for styling the HTML pages.
    data.db: SQLite database that stores photos, descriptions, and contest results.

