#define the function search
def search(filename):
#display first message
  print("Searching...")
  #create the two lists
  sections  = []
  books = []
  #open the file
  with open(filename) as file:
    #for each line in the file
    for line in file:
      if line.startswith("Section"):
        split = line.split(":")
        sections.append(split[1][:-1])
      else:
        books.append(line[:-1])
  print("Done!")
  data = (books, sections)
  return data

#define the function save!
def save(filename,data):
  print("Saving...")
  with open(filename, "w") as file:
    file.write(f"Sections:{data[1]}")
    file.write(f"\nBooks:{data [0]}")
  print("Done!")

#define the function Run
def run():
  data = search("data/files/books.txt")
  save("data/files/section-books.txt", data)
 

run()