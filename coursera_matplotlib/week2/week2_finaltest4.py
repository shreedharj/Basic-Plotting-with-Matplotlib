# TODO: assigning values to each bar seperately


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

languages = np.array(['Python','SQL','Java','C++','JavaScript'])
pos = np.arange(len(languages))
popularity = [56,39,34,34,29]
bars = plt.bar(pos, popularity, align = 'center', color='grey')
bars[0].set_color('#1F77B4')
plt.xticks(pos, languages)
plt.ylabel('%popularity')
plt.title('Top 5 Languages for Math & Data \n by % popularity on Stack Overflow', alpha=0.8)

#removes ticks
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False)

#removing frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

#assigning values to each bar seperately
for x,y in enumerate(popularity):
    plt.bar(x , y - 5, str(y+'%'), color='white', fontweight='bold')

canvas.print_figure('images/week2_finaltest4.png')

