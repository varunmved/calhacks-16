def adjustAlpha(plot, param, al): # works for scatter, regLine
    #new["alpha"] = "alpha = I(al/100)"
    #newPlot = plot + geom_point(param, alpha = I(al/100))
    #save_plot 
    param = " + geom_point(alpha = I(al/100))"
    return param

def switch(newX, newY): # used for scatter, regLine, smoothLine, linePlot
    newBase = "ggplot(data, aes(newX, newY))"
    return newBase
    # template is geom_point() for example
    # save_plot 
    
def addTitle(title):
    newTitle = " + ggtitle(newTitle)"
    return newTitle
    #new["title"] = "+ ggtitle(newTitle)"
    # save 
    
    
def adjust(typeOfGraph, arg, switch, alpha, title):
    #templateList = ['histogram', 'boxplot', 'bargraph', 'scatter', 'regLine', 'smoothLine', 'linePlot', 'pieChart', 'corrplot']
    #matPlots = ['boxplot', 'pieChart', 'corrplot']
    typeOfGraph # which one they ended up picking
    
    param = ''
    
    # switch special
    if typeOfGraph == 'histogram':
        special = "+ geom_histogram()"
        
    if typeOfGraph == 'scatter':
        special = "+ geom_point()"

    if typeOfGraph == 'regLine':
        special = "+ geom_point() + stat_smooth(method = 'lm', se = F)"
    
    count_args = len(arg)
    if count_args == 1:
        base = "ggplot(df, aes(arg[0]))"
    else if count_args == 2:
        base = "ggplot(df, aes(arg[0], arg[1]))"
        if typeOfGraph == 'regLine' or typeOfGraph == 'scatter':
            special = adjustAlpha(base, param, alpha)
            if switch == True:
                base = switch(arg[1], arg[0])
                
    plot = base + special 
                
    if title == True:
        plot = plot + addTitle(title)
    save_plot(plot, 'newplot')
