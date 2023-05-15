from bokeh.plotting import figure, show

p = figure(width = 500, height = 400)

nan = float("nan")
p.line([1,nan,nan,4,5], [3,5,7,1,2],
       line_width = 5,
       alpha = 0.7,
       color = "red"
       )

show(p)