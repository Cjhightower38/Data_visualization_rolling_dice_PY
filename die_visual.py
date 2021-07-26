from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
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
	
print(frequencies)
