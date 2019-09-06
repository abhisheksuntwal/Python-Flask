"""
Very basic first flask app which creates a path for homepage and
and returns "Hello World" on the home page at localhost post 5000

Output of running the above code in terminal is as below:
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 [127.0.0.1] can also be substituted by "localhost"
"""
from flask import Flask

app = Flask(__name__)

# To access the home page of an application
@app.route('/')
def home():
    return "Hello World"

# port can be any port that can be used to run
# the application in the browser window.
app.run(port=5000)
