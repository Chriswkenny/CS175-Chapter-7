#Christopher Kenny
#CS 175
#Pie Chart Assignment


import matplotlib.pyplot as fruity

fruity.title('Fruit Distribution')
values = ([25, 30, 15, 10, 20])
slice_label = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Berries'] 
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'] 
fruity.pie(values, labels=slice_label)
fruity.pie(values, labels = slice_label, colors = colors, autopct='%1.1f%%')
fruity.show()
