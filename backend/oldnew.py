
# do this right when you start 
from ggplot import *
import matplotlib.pyplot as plt
from collections import Counter


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
    
def barGraph(data, x):
    weights = data.count(x)
    ggplot(aes(x="x", weight= weights), data) + geom_bar()
    
def pieChart(data, x):
    counts = Counter(x)
    labels = counts.keys()
    size = counts.values()
    plt.pie(size = size, labels=labels, autopct='%1.1f%%')
    #plt.axis('equal')
    #plt.show()
    fname = str('pie_' +   str(randint(0,100000000)) + '.png')
    plt.savefig(fname, bbox_inches='tight')

def facet1(data, x, divider):
    save_plot(ggplot(data, aes(x,y)) + geom_histogram() + facet_wrap(divider), 'facet_single')

def corrplot(data):
    plt = (scatter_matrix(data)
    fname = str('correlation_' +   str(randint(0,100000000)) + '.png')
    plt.savefig(fname, bbox_inches = "tight")

def boxplot(data, x):
    plt = data.plot(kind = 'box')
    fname = str('box_' +   str(randint(0,100000000)) + '.png')
    plt.savefig(fname, bbox_inches = "tight")