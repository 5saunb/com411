def display(x_values, y_values):
  import matplotlib.pyplot as plt

  x = x_values
  y = y_values

  plt.plot(x, y)
  plt.show()


def run():
  x_values = [1,2,3,4,5]
  y_values = [1,4,9,16,25]

  display(x_values,y_values)


run()