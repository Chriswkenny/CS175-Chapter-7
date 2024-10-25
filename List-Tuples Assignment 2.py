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
