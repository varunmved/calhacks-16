# do this right when you start
import pandas as pd

from ggplot import *
%matplotlib inline

csvFile = 'data.csv'

#utils
def csv_to_dframe(csv):
    df = pd.DataFrame(csv)
    return df

def save_plot(plot):



# 2 variables
def scatter(data, x, y):
    save_plot(ggplot(data, aes(x, y)) + geom_point())

def regLine(data, x, y):
    ggplot(data, aes(x, y) + stat_smooth(method = "lm", se = F)

def smoothLine(data, x, y):
    ggplot(data, aes(x, y) + stat_smooth()

def linePlot(data, x, y):
    ggplot(data, aes(x,y) + geom_line()

# 1 variable
def histogram(data, x):
    ggplot(diamonds, aes(x)) + geom_histogram()


def run(csvFile, ):

