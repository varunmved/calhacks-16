# do this right when you start
import csv
import pandas as pd
from random import randint

from ggplot import *
#%matplotlib inline

csvFile = 'test_data.csv'
arg = ['latitude', 'longitude']

ONE_VARIABLE_FUNCS = 1
TWO_VARIABLE_FUNCS = 4
MORE_VARIABLE_FUNCS = 4
COUNT = 0

#utils
def csv_to_dframe(csvFile):
    rdr = csv.reader(open(csvFile))
    line1 = rdr.next() # in Python 2, or next(rdr) in Python 3
    #print(line1)
    df = pd.read_csv(csvFile, index_col=0, header=0, names=line1)
    #print(df.shape)
    #print(df.head(1))
    #print(df[:,0])
    return df

def save_plot(plot, plot_type):
    name = str(plot_type + '_' +   str(randint(0,100000000)) + '.png')
    plot.save(name)#, plot=plot)
    #print 'hi'

def upload_to_web(plotJpg):
    print('hi')
    #r = request.post(

# 1 variable
def histogram(data, x):
    x = str(x)
    #print(data)
    save_plot(ggplot(data, aes(x)) + geom_histogram(), 'histogram')

# 2 variables
def scatter(data, x, y):
    save_plot(ggplot(data, aes(x, y)) + geom_point(), 'scatter')

def regLine(data, x, y):
    save_plot(ggplot(data, aes(x, y) + stat_smooth(method = "lm", se = False)), 'regression')

def smoothLine(data, x, y):
    save_plot(ggplot(data, aes(x, y) + stat_smooth()),'smooth_line')

def linePlot(data, x, y):
    save_plot(ggplot(data, aes(x,y) + geom_line()), 'line_plot')


#runner
def run(csvFile, arg):
    count_args = len(arg)
    df = csv_to_dframe(csvFile)
    df.head()
    if count_args < 1:
        print('hi')

    if count_args == 1:
        histogram(df, arg[1])

    if count_args == 2:
        scatter(df, arg[0], arg[1])
        regLine(df, arg[0], arg[1])
        smoothLine(df, arg[0], arg[1])
        linePlot(df, arg[0], arg[1])


run(csvFile, arg)
