from bokeh.plotting import figure, show

p = figure(width = 500, height = 400)
x = [1,2,3,4,5]
y = [3,5,7,9,11]

p.line(x, y, line_width = 10)
p.circle(x,y, fill_color = "yellow", size = 30)
show(p)