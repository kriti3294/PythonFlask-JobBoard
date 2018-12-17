# import flask class and render_template function
from flask import Flask, render_template

# create a flask instance app object by passing special variable __name__
app = Flask(__name__)

# folder to store templates: jobs/template
#to create single route: define jobs
#define function jobs:

#add route decorator:
# Attach a route() decorator with the URL of / to the jobs function.
# Attach an additional route decorator of /jobs.
# Note: The jobs function can now be reached at / and /jobs
@app.route('/')
@app.route('/jobs')

def jobs():
    #passing template
        return render_template('index.html')
