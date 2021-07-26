# import Die class from die.py as well as import pygal module
import pygal
from die import Die

# Create two instances one D6 die and one D10 die.
die_1 = Die()
die_2 = Die(10)

'''
Make some rolls, and store results in a empty list. Increased range to
1000 from printing to analyzing results.
'''

results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
'''
Analyze the results. Reminder the +1 is so the program includes
through all 16 from the addition of the second die sides of the die off
by 1 when you use range. Max_result is the sum of the largest two
sides on the dice. Which makes the starting point 2 the sum of the
smallest numbers. Reminder since the smallest number is 2 the chart will
only generate 15 columns.
'''

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range (2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
	

'''
Visulalize the results using pygal. Read documentation on pygal basic
bar hist.add; adds the results from the frequencies list randomly
created and render to stores it in the .svg file.
'''

hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 50,000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
    '12', '13', '14', '15', '16']
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_sided_dice_visual.svg')

	
print(frequencies)
