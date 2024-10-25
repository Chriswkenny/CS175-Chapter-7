#Christopher Kenny
#CS 175
#CSV File Assigment

import csv

def main():
  data = open('data.csv', 'r')
  categories_list = []
  values_list = []

  with open('data.csv', 'r') as data:
    csv_reader = csv.reader(data)
    next(csv_reader)
    for row in csv_reader:
      categories_list.append(row[0])
      values_list.append(int(row[1]))

  print(f"Categories List: {categories_list}")
  print(f"Values List: {values_list}")

  import matplotlib.pyplot as fruit

  def bar_graph():
      x_axis = range(len(categories_list))
      heights = values_list
      width = 0.7
      fruit.title('Fruit Distribution')
      fruit.xlabel('Category')
      fruit.ylabel('Value')
      fruit.xticks(x_axis, categories_list)
      fruit.yticks(heights)
      fruit.bar(x_axis, heights, width, color=('#A50202','#5BF72F','#0AECCF','#E61AB3','#02144D'))
      fruit.show()

  bar_graph()

main()
