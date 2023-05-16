from bokeh.plotting import figure, show
from bokeh.models import Range1d

p = figure(width = 500, height = 400, x_range = (0, 20))

p.y_range = Range1d(0,30)

p.circle(x = [1,2,3,4,4,5],
         y = [3,4,5,6,63,3],
         size = 30,
         color = "red"
         )
show(p)

