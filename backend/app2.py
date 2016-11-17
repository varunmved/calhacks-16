import os
import io
import csv
import requests
from flask import Flask, request, redirect, url_for, send_from_directory
from flask.ext.cors import CORS, cross_origin
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
#import pandas as pd
#from random import randint
#from ggplot import *
import pyimgur

ONE_VARIABLE_FUNCS = 1
TWO_VARIABLE_FUNCS = 4
MORE_VARIABLE_FUNCS = 4
COUNT = 0

#imgur client, this really should be within a config
CLIENT_ID = '27eac2b1c4e9f1b'
im = pyimgur.Imgur(CLIENT_ID)

#utils

##imgur upload
def imgur(plotJpg):
    uploaded_imag
 im.upload_image(plotJpg,utitle=plotJpg)
    #print(uploaded_image.title)
    #return(str(uploaded_image.link))
    return (uploaded_image.link)


#main

##runner
def runS(csvFile, arg):
    count_args = len(arg)
    df = csv_to_dframe(csvFile)
    outfiles = []
    if count_args < 1:
        print('hi')

    if count_args == 1:
        outfiles.append(imgur(histogram(df, arg[0])))
    if count_args == 2:
        outfiles.append(imgur(scatter(df, arg[0], arg[1])))
        outfiles.append(imgur(regLine(df, arg[0], arg[1])))
        outfiles.append(imgur(smoothLine(df, arg[0], arg[1])))
        outfiles.append(imgur(linePlot(df, arg[0], arg[1])))

    return(json.dumps(outfiles))


# Initialize the Flask application
app = Flask(__name__)
cors = CORS(app)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])
app.config['CORS_HEADERS'] = 'Content-Type'

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


#routes

## root (does nothing)
@app.route('/')
def index():
    return 'H E R E C O M E D E M B O Y Z'

## Route that will process the file upload
@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    # Get the name of the uploaded file
    imd = ImmutableMultiDict(request.form)
    print(imd)
    filen = request.files['file']
    filename = secure_filename(filen.filename)
    args = []

    xval = imd.getlist('variables')[0].split(',')[0]
    if (xval):
        args.append(str(xval))

    yval = imd.getlist('variables')[0].split(',')[1]
    if yval:
        args.append(str(yval))

    return(runS(filename, args))
    print(str(filen))

    #this needs to be better written, move file storage to S3

    # Check if the file is one of the allowed types/extensions
    if filen and allowed_file(filen.filename):
        print(str(filen))
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(filen.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        #return redirect(url_for('uploaded_file, filename=filename))

        return(runS(filename, args))
    else:
        return 'sorry no file'

if __name__ == '__main__':
    app.run(debug = True)

