#define function to sum weights
def sum_weight(beep_weight, bop_weight):
  total_weight = beep_weight + bop_weight
  return print("The sum of Beep and Bop's weight is {}!".format(total_weight))
#define function to calculate average weights
def calc_avg(beep_weight, bop_weight):
  avg_weight = (beep_weight+bop_weight)/2
  return print("The Average weight of Beep and Bop is {}!".format(avg_weight))
#define the run command
def run():
  print("What is the weight of Beep?")
  beep_weight = int(input())
  print("What is the weight of Bop?")
  bop_weight = int(input())
  print("Please enter sum or average")
  calc = input()
  if (calc == "sum"):
    sum_weight(beep_weight,bop_weight)
  elif(calc =="average"):
    calc_avg(beep_weight,bop_weight)
  else:
    print("Can you read? Start the dang program again and follow the instructions...")

#RUN THE PROGRAM
run()