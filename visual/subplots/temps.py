import csv
import matplotlib.pyplot as plt

def read_data():
  with open ("visual/subplots/temps.csv") as csvfile:
    
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)

    first_key = header[0].strip
    sec_key = header[1].strip
    
    data = {first_key:[],sec_key:[]}
    
    for row in csv_reader:
      data[first_key].append(row[0].strip())
      data[sec_key].append(row[1].strip())
      
  return data

def run():
  data = read_data()
  print(data)
  fig, (ax1,ax2) = plt.subplots(2,1)
  plt.show()


run()

#This Half-works but you need to look at the seminar/solutions to complete it.