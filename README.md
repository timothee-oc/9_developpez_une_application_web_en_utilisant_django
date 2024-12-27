# Installation

* Install Python (version >= 3.12.4) and make sure pip is installed alongside (version >= 24.0)
* Clone this repo in a local directory and `cd` into it
* Create a virtual environment with the command : `py -m venv venv`
* Enter the virtual environment : `.\venv\Script\activate`
* Install required dependencies : `pip install -r requirements.txt`

# How to use

* Run the server with : `py .\litrevu\manage.py runserver`
* Go to [127.0.0.1:8000/login/](http://127.0.0.1:8000/login/) on your browser
* Sign up to create an user account or login if you already have one
* Features :
    - Create a ticket to request a review on a book
    - Create a review for a book directly or as an answer to another user's ticket
    - Modify or delete your own posts
    - Follow other users to see their posts appear on your feed page

# Test data

This repo already contains a db (db.sqlite3) which has been filled with some data (tikets, reviews, follows, etc...) and some pictures (in litrevu/media/) to test the application.
You can log in as either:
    - saraj
    - jean_5679
    - severine123
    - timothee
Their passwords are all the same : **hypersecret**