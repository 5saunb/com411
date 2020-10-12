#ask user for number of cables
print("How many cables should I remove?")
cables_to_remove = int(input())

#control variable
cables_removed = 0

#removing the cables
print()

while (cables_removed < cables_to_remove):
    print("Removed cable.")
    cables_removed = cables_removed + 1
