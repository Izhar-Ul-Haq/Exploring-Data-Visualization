from bokeh.plotting import figure, show


p = figure(width = 500, height = 400)

p.ray(
    x = [1,2,3],
    y = [1,2,3],
    length = 10,
    angle = [10,20,30],
    angle_units = "deg",
    color = "Red",
    line_width = 2
)
show(p)

