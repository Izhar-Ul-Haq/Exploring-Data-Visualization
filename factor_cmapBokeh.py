from bokeh.plotting import figure, show
from bokeh.palettes import Bright6
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

source = ColumnDataSource(dict(fruits = fruits, counts = counts))
p = figure(x_range = fruits, y_range = (0, 9), title = "Fruits Chart",
           toolbar_location = None,
           tools = ""
           )
p.vbar(x = "fruits", top = "counts", width = 0.6, 
       source = source,
       legend_field = "fruits",
       line_color = "blue",
       fill_color = factor_cmap("fruits", palette=Bright6, factors = fruits)        
       )
p.xgrid.grid_line_color = "green"
p.ygrid.grid_line_color = "blue"
p.y_range.start = -1
p.y_range.end = 10
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
show(p)
