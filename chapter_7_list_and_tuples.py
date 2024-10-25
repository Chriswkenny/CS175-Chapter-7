# -*- coding: utf-8 -*-
"""Chapter 7: List and Tuples

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1el-sb41PQ4dMZogUCVeexURyDww_9EiZ
"""

#Christopher Kenny
#CS 175
#List-tuples word doc assignment

scores = [2.5, 7.3, 6.5, 4.0, 5.2]

for x in scores:
    total = sum(scores)
    average = total/len(scores)

print(f"The average of the elements is {average}.")

#Christopher Kenny
#CS 175
#List-tuples word doc assignment

def cities():
  city_list = []
  with open('cities.txt', 'r') as cities:
    for city in cities:
      city_list.append(city.strip())
  print(city_list)

cities()

#Christopher Kenny
#CS 175
#matplotlib assignment

import matplotlib.pyplot as xyz

def main():
    x_axis = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    width = 10
    xyz.title('Sales by Year')
    xyz.xlabel('Year')
    xyz.ylabel('Sales')
    xyz.xticks(x_axis, [2016, 2017, 2018, 2019, 2020])
    xyz.yticks([0, 100, 200, 300, 400, 500],['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    xyz.bar(x_axis, heights, width, color=('r','g','b','w','k'))
    xyz.show()

main()

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