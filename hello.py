from flask import Flask
from flask import abort
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
#from werkzeug.utils import secure_filename

#from google.cloud import storage

import os
import uuid


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("record.html")

if __name__ == "__main__":
    app.run(debug=True)