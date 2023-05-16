from bokeh.plotting import figure, show
from bokeh.sampledata.stocks import AAPL
import bokeh.sampledata
import pandas as pd

# bokeh.sampledata.download()
df = pd.DataFrame(AAPL)
print(df.head)
df['date'] = pd.to_datetime(df['date'])

p = figure(width = 800, height = 500, x_axis_type = 'datetime')
p.line(x = df.date, y = df.close, color = "red",
       alpha = 0.7
       )

show(p)