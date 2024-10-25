#Christopher Kenny
#CS 175
#Two Dimensional list Problem 1
import random
rows = 3
cols = 4
lower_bound = 1
upper_bound = 100

matrix = []
for i in range(rows):
  matrix.append([])
  for y in range(cols):
    matrix[i].append(random.randint(lower_bound, upper_bound))

for row in matrix:
  print(f'Random Matrix: {row}')
