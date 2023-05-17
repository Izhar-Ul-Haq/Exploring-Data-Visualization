from bokeh.plotting import figure, show

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]
sorted_fruits = sorted(fruits, key = lambda x: counts[fruits.index(x)])
p = figure(x_range = sorted_fruits, height = 400, title = "Fruits",
           toolbar_location = None,
           tools = ""
           )
p.vbar(x = fruits, top = counts, width = 0.4)
p.xgrid.grid_line_color = "red"
p.ygrid.grid_line_color = "blue"
p.y_range.start = 0
show(p)