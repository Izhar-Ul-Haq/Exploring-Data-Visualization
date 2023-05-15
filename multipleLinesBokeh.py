from bokeh.plotting import figure, show

p = figure(width = 500, height = 400)

p.multi_line([[1,2,3,4,5], [2,3,4,5,6]], [[2,4,6,8,10],[3,5,7,9,11]],
             color=['red', 'orange'],
             line_width = 5,
             alpha = [.8, .4]             
             )
show(p)