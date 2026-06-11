# ----- PYTHON WEB -----

# Deploying a Python Flask Project on Render

# source venv/Scripts/activate
# pip freeze > requirements.txt
# pip install gunicorn
# Run gunicorn app:app (gunicorn <filename>:<flask_instance>)

# Create Render account
# name => my-flask-app
# Runtime => Python 3
# Build COummand => pip install -r requirements.txt
# Start Command => gunicorn app:app
# Click Deploy Service => Generates the url for the project


# Check out my "Python-for-Web" Repo for this implementation

# ----- DONE -----