#manipulating and cleaning date using zip/unpacking


import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
x,y = zip(*zip_generator) #takes first number of both arrays and turns into a coordinate (zip combines two arrays into coordinates)
print(x)
print(y)

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.scatter(x, y, s=100, color='magenta')

canvas.print_figure('images/week2_8.png')
