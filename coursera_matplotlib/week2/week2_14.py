import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import pandas as pd

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

observation_dates = np.arange('2017-01-01','2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates))

plt.plot(observation_dates, linear_data, '-o', observation_dates, quadratic_data, '-o')

x = plt.gca().xaxis

for item in x.get_ticklabels():
    item.set_rotation(45) #rotates the tick labels for readablility

plt.subplots_adjust(bottom=0.25) #adjusts the image bc its running off of the screen

canvas.print_figure('images/week2_14.png')
