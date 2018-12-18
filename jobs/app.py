# import flask class and render_template function
import sqlite3
from flask import Flask, render_template, g

PATH = 'db/jobs.sqlite'

# create a flask instance app object by passing special variable __name__
app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit = False, single = False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cusror.fetchall()

    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()
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
