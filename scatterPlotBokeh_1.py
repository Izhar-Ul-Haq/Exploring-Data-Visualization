from bokeh.plotting import figure, show

a = figure(width = 500, height = 400)
b = figure(width = 500, height = 400)
c = figure(width = 500, height = 400)
d = figure(width = 500, height = 400)
e = figure(width = 500, height = 400)

a.circle([1,2,3,4,5], [2,3,4,5,6], color="red", alpha = 1.0, size = 30)
b.circle_x(x = [1,2,3,4,5], y = [2,3,4,5,6], color="red", alpha = 0.5, size = 30)
c.circle_y(x = [1,2,3,4,5], y = [2,3,4,5,6], color="red", alpha = 0.5, size = 30)
d.asterisk(x = [1,2,3,4,5], y = [2,3,4,5,6], color="red", alpha = 0.5, size = 30)
e.diamond_dot(x = [1,2,3,4,5], y = [2,3,4,5,6], color="red", alpha = 0.5, size = 30)


show(a)
show(b)
show(c)
show(d)
show(e)