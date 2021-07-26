# import Die class from die.py as well as import pygal module
import pygal
from die import Die

# Create a D6
die = Die()

'''
Make some rolls, and store results in a empty list. Increased range to
1000 from printing to analyzing results.
'''

results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
	
'''
Analyze the results. Reminder the +1 is so the program includes
through all 6 sides of the die off by 1 when you use range.
'''

frequencies = []
for value in range (1, die.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
	

'''
Visulalize the results using pygal. Read documentation on pygal basic
bar hist.add; adds the results from the frequencies list randomly
created and render to stores it in the .svg file.
'''

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

	
print(frequencies)
