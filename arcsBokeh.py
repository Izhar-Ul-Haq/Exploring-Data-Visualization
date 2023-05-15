from bokeh.plotting import figure, show
p = figure(width = 500, height = 400)

p.arc(
    x = [1,2,3],
    y = [1,2,3],
    color = "red",
    radius = 0.5,
    start_angle = 1.5,
    end_angle = 4.7
)
show(p)