#define the first function - display_ladder
def display_ladder(steps):
    print("""
    | |
    ***""" * steps)
#define the second function - create_ladder
def create_ladder():
  print("How many steps are remaining?")
  steps = int(input())
  display_ladder(steps)
  print("""
    | |""")

create_ladder()