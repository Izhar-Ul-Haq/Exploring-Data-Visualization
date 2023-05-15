from bokeh.plotting import figure, show

p = figure(width = 500, height = 400)

x_values = [1,2,3,4,5]
y_values = [2,3,4,5,6]

p.circle(x = x_values,
         y = y_values,
         color = "brown",
         size = 20
         )
show(p)
