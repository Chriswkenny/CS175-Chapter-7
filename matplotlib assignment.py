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
