import pandas
import sys
from bokeh.io import output_notebook, show
from bokeh.plotting import figure


print("Hello, world!")
p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)

show(p)