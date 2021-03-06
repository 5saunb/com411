import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0,2*np.pi, 0.01)
line, = ax.plot(x,np.sin(x))

def animate(frame):

  line.set_ydata(np.sin(x + frame/50))
  return line,
  

def run():
  global fig
  simple_animation = animation.FuncAnimation(fig,animate,frames=720, interval =16.67)

  plt.show()

run()

