def read_data(filepath):
  with open (filepath) as file:
    data = []
    for line in file:
      data.append(int(line.strip()))
     
  print(data)
  return data


def run():
  data = read_data("visual/subplots/temps.txt")
  import matplotlib.pyplot as plt

  fig,(ax1,ax2) = plt.subplots(1,2)
  x = range(1,8,1)
  y = data
  
  ax1.plot(x,y)
  ax1.set_xlabel("Day")
  ax1.set_xlim(0,8)
  ax1.set_ylabel("Temperature (celsius)")
  ax1.set_ylim(1,25)
  
  ax2.bar(x,y)
  ax2.set_xlabel("Day")
  ax2.set_xlim(0,8)
  ax2.set_ylabel("Temperature (celsius)")
  ax2.set_ylim(1,25)
  plt.show()



run()