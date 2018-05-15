import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from Tkinter import *


def zoom_factory(ax,base_scale = 2.):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        cur_xrange = (cur_xlim[1] - cur_xlim[0])*.5
        cur_yrange = (cur_ylim[1] - cur_ylim[0])*.5
        xdata = event.xdata # get event x location
        ydata = event.ydata # get event y location
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1/base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print event.button
        # set new limits
        ax.set_xlim([xdata - cur_xrange*scale_factor,
                     xdata + cur_xrange*scale_factor])
        ax.set_ylim([ydata - cur_yrange*scale_factor,
                     ydata + cur_yrange*scale_factor])
        plt.draw() # force re-draw

    fig = ax.get_figure() # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event',zoom_fun)

    #return the function
    return zoom_fun


#style.use('fivethirtyeight')
plt.style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

plt.hold(True)
xs = [0]
ys = [0]
zs = [0]
#ax1.scatter(0,0,0,s= 9,c='r')
def animate(i):

    graph_data = open('data.txt','r').read()
    lines = graph_data.split('\n')
    for line in lines:
        if len(line) > 1:
            data = line.split(' ')
            x = data[0].strip()
            y = data[1].strip()
            z = data[2].strip()
            x =float(x)
            y = float(y)
            z = float(z)
            xs.append(x)
            ys.append(y)
            zs.append(z)
            ax1.clear()
	    ax1.scatter(0,0,0,s= 100,c='r')
            ax1.scatter(xs,ys,zs,s = 1, c='b')
            plt.axis('off')


ani = animation.FuncAnimation(fig, animate, interval=10)
plt.axis('off')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
scale = 1.5
f = zoom_factory(ax1,base_scale = scale)

plt.show()
