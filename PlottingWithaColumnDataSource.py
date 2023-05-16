from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
p = figure(width = 500, height = 400)

data = {
    'x_values':[1,2,3,4,5],
    'y_values':[3,4,5,6,7]
}
source = ColumnDataSource(data = data)
p.circle(x = 'x_values', y = "y_values", source = source)

show(p)

