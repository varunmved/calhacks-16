## part 6

# adjust alpha

def adjustAlpha(plot, al, new): # works for scatter, regLine
    new["alpha"] = "alpha = I(al/100)"
    plot + ggplot(data, aes(x, y)) + geom_point(alpha = I(al/100))
    #save_plot 
    return new

def switch(template, newX, newY): # used for scatter, regLine, smoothLine, linePlot
    ggplot(data, aes(newX, newY)) + template
    # template is geom_point() for example
    # save_plot 
    
def addTitle(plot, newTitle, new):
    plot + ggtitle(newTitle)
    new["title"] = "+ ggtitle(newTitle)"
    # save 
    
def axisLabels(plot, xlabel, ylabel, new):
    plot + xlab(xlabel) + ylab(ylabel)
    new["xlab"] = "+ xlab(xlabel) + ylab(ylabel)"
    # save new plot

def adjustLine(plot, sz, args):
    newArg = "size = sz"
    if args:
        plot + geom_line(newArg, args)
    else:
        plot + geom_line(newArg)