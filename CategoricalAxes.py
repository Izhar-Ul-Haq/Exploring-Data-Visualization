from bokeh.plotting import figure, show

factors = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
x = [10, 20, 30,40,50,60,70]
p = figure(width = 500, height = 400, y_range = factors)

p.circle(x = x, y = factors, 
         size =20, line_width = 5, 
         fill_color ="red",
         color = "yellow"
         )

show(p)

