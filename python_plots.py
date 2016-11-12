
# do this right when you start 
from ggplot import *
%matplotlib inline


# 2 variables
def scatter(data, x, y):
    ggplot(data, aes(x, y)) + geom_point()

def regLine(data, x, y):
    ggplot(data, aes(x, y) + stat_smooth(method = "lm", se = F)

def smoothLine(data, x, y):
    ggplot(data, aes(x, y) + stat_smooth()

def linePlot(data, x, y):
    ggplot(data, aes(x,y) + geom_line()
    
# 1 variable
def histogram(data, x):
    ggplot(diamonds, aes(x)) + geom_histogram()
    
