import numpy as np
from bokeh.plotting import figure, show

p = figure()
# width = 500, height = 400
x = [1, 2, 3, 4, 5]
random = np.random.standard_normal(5)
cosine = np.cos(x)

p.circle(x=x, y=random)
p.line(x=x, y=cosine)
show(p)