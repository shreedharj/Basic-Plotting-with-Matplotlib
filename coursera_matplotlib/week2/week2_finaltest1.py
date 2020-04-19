#TODO: remove all the ticks (both axes), and tick labels on the Y axis

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

languages = np.array(['Python','SQL','Java','C++','JavaScript'])
pos = np.arange(len(languages))
popularity = [56,39,34,34,29]
plt.bar(pos, popularity, align = 'center')
plt.xticks(pos, languages)
plt.ylabel('% popularity')
plt.title('Top 5 Languages for Math & Data \n by % popularity on Stack Overflow', alpha=0.8)

plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=True)

canvas.print_figure('images/week2_finaltest1.png')

