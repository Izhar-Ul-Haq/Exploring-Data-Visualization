from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show

p = figure(width = 500, height = 400)
source = ColumnDataSource(data=dict(
    x = [1,2,4,5,6],
    y1 = [1,2,5,6,3],
    y2 = [2,4,1,4,6]
))

p.vline_stack(['y1', 'y2'], x = 'x', source = source)
show(p)