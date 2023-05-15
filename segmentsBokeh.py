from bokeh.plotting import figure, show


p = figure(width = 500, height = 400)

p.segment(
    x0 = [1,2,3,],
    y0 = [1,2,3],
    x1 = [2,3,4],
    y1 = [2,3,4],
    color = "yellow",
    line_width = 10
)
show(p)