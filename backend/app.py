import os
import io
import csv
import requests
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import pandas as pd
from random import randint
from ggplot import *
import pyimgur

# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
#csvFile = 'test_data.csv'
#arg = ['latitude', 'longitude']

ONE_VARIABLE_FUNCS = 1
TWO_VARIABLE_FUNCS = 4
MORE_VARIABLE_FUNCS = 4
COUNT = 0

CLIENT_ID = '27eac2b1c4e9f1b'
im = pyimgur.Imgur(CLIENT_ID)


#utils
def csv_to_dframe(csvFile):
    rdr = csv.reader(open(csvFile))
    line1 = rdr.next() # in Python 2, or next(rdr) in Python 3
    df = pd.read_csv(csvFile, index_col=0, header=0, names=line1)
    return df

def save_plot(plot, plot_type):
    name = str(plot_type + '_' +   str(randint(0,100000000)) + '.png')
    a = plot.save(name)
    return name
    #return a

def photo(plotJpg):
    #plotJpg = ('/' + plotJpg)
    url = "http://uploads.im/api"
    payload = ('-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"%s\"\r\nContent-Type: image/png\r\n\r\n\r\n-----011000010111000001101001--' % plotJpg)
    print(payload)
    headers = {
	'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	'cache-control': "no-cache",
	'postman-token': "ff6bf677-28d4-bc24-b247-6007fb4d586a"
	}

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return(response.text)

def imgur(plotJpg):
    uploaded_image = im.upload_image(plotJpg, title=plotJpg)
    #print(uploaded_image.title)
    return(str(uploaded_image.link))



# 1 variable
def histogram(data, x):
    x = str(x)
    #print(data)
    return save_plot(ggplot(data, aes(x)) + geom_histogram(), 'histogram')

def barGraph(data, x):
    weights = data.count(x)
    return save_plot(ggplot(aes(x="x", weight= weights), data) + geom_bar())

def pieChart(data, x):
    counts = Counter(x)
    labels = counts.keys()
    size = counts.values()
    plt.pie(size = size, labels=labels, autopct='%1.1f%%')
    #plt.axis('equal')
    #plt.show()
    fname = str('pie_' +   str(randint(0,100000000)) + '.png')
    plt.savefig(fname, bbox_inches='tight')
    return fname

def facet1(data, x, divider):
    return save_plot(ggplot(data, aes(x,y)) + geom_histogram() + facet_wrap(divider), 'facet_single')

def corrplot(data):
    plt = scatter_matrix(data)
    fname = str('correlation_' +   str(randint(0,100000000)) + '.png')
    plt.savefig(fname, bbox_inches = "tight")
    return fname

def boxplot(data, x):
    plt = data.plot(kind = 'box')
    fname = str('box_' +   str(randint(0,100000000)) + '.png')
    plt.savefig(fname, bbox_inches = "tight")
    return fname

# 2 variables
def scatter(data, x, y):
    return save_plot(ggplot(data, aes(x, y)) + geom_point(), 'scatter')

def regLine(data, x, y):
    return save_plot(ggplot(data, aes(x, y)) + geom_point() + stat_smooth(method = "lm", se = False), 'regression')

def smoothLine(data, x, y):
    return save_plot(ggplot(data, aes(x, y)) + stat_smooth(),'smooth_line')

def linePlot(data, x, y):
    return save_plot(ggplot(data, aes(x,y)) + geom_line(), 'line_plot')


#runner
def runS(csvFile, arg):
    count_args = len(arg)
    df = csv_to_dframe(csvFile)
    outfiles = []
    #outfiles = ''
    if count_args < 1:
        print('hi')

    if count_args == 1:
        fname = (histogram(df, arg[0]))
        outfiles.append(imgur(histogram(df, arg[0])))
        #print(fname)
    if count_args == 2:
        outfiles.append(imgur(scatter(df, arg[0], arg[1])))
        outfiles.append(imgur(regLine(df, arg[0], arg[1])))
        outfiles.append(imgur(smoothLine(df, arg[0], arg[1])))
        outfiles.append(imgur(linePlot(df, arg[0], arg[1])))

    return(str(outfiles))


# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
#app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return 'H E R E C O M E D E M B O Y Z'

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    filen = request.files['file']
    filename = secure_filename(filen.filename)

    args = []

    xval = (request.form['xValue'])
    if (xval):
        args.append(str(xval))

    yval = (request.form['yValue'])
    if yval:
        args.append(str(yval))

    print(args)
    """
    typeOfGraph = (request.form['typeOfGraph'])
    if typeOfGraph:
        args.append(str(typeOfGraph))

    variables = (request.form['variables'])
    if variables:
        args.append(str(variableVs))

    alphaValue = request.form['alphaValue']
    if alphaValue:
        args.append(str(alphaValue))

    titleValue = request.form['titleValue']
    if titleValue:
        args.append(str(titleValue))
    """
    print(args)
    return(runS(filename, args))
    print(str(filen))
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

        """
        out = r_exec(file)
        return out
        """
	#arg = ['latitude']
        return(runS(filename, args))
        #return (str(file))
    else:
        return 'sorry no file'

if __name__ == '__main__':
    app.run(debug = True)

