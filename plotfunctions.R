## C A L H A C K S ## I L O V E V A R U N


ggplot(diamonds, aes(carat, price)) +geom_point()

scatter = function(data, VarX, VarY)
{
  attach(data)
  require("ggplot2")
  ggplot(data, aes(x = VarX, y = VarY)) + geom_point()
} # basic scatterplot


regLine = function(data, VarX, VarY)
{
  attach(data)
  require("ggplot2")
  ggplot(data, aes(x = VarX, y = VarY)) +  geom_smooth(method = "lm", se = F)
}

regLine(diamonds, carat, depth)
scatter(diamonds, carat, depth)

smoothLine = function(data, VarX, VarY, wiggly)
{
  attach(data)
  require("ggplot2")
  if(missing(wiggly))
    ggplot(data, aes(x = VarX, y = VarY)) +  geom_smooth()
  else
    ggplot(data, aes(x = VarX, y = VarY)) +  geom_smooth(span = wiggly)
}


hexSmooth = function(data, VarX, VarY)
{
  attach(d)
}

