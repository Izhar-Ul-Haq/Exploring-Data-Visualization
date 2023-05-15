from bokeh.plotting import figure, show

p = figure(width = 500, height = 400)

p.step([1,2,3,4,5], [2,3,4,5,6], mode = "center", line_width =3)

show(p)