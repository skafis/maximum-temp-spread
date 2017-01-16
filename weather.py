#!/usr/bin/python
"""
The accompanying file weather.dat contains weather data for a single month as space-separated values. The first column (Dy) contains the day of the month; the second (MxT) contains the maximum temperature for that day, while the third (MnT) contains the minimum temperature.

The final row contains aggregate values for the entire month.

Write a program to find the row with the maximum spread in the weather.dat file, where spread is defined as the difference between MxT and MnT. For example, the spread for day 2 was (79 - 63) = 16.

Your program should print the day of the month and spread to standard output.

Assuming that your program is called weather.py, then a sample run will look like:

$ python weather.py
2 16

(The actual day and spread will depend on the contents of the file.)
"""

# initiate a function main
def main():
	# open file
	file = open('weather.dat')
	# initiate empty list lst
	lst = []
	# iterate through the file 
	for line in file:
		# split the lines and add to empty list lst
		lst += [line.split()]

	# get the columns that we want to work that is column 2 & 3 and remove the first two and last rows and assign it to a varailble
	columns = [x[1:3] for x in lst[2:-1]]

	# iterate through the varialble to get the row value
	for value in columns:
		# check for every row and assign the values to variable x and y
		if value:
			x,y = value

			# convert to integers and remove non integer characters
			value1 =  int(x.strip('*'))
			value2 = int(y.strip('*'))

			# call the calculate function and pass in the variable
			print calculate(value1, value2)


def calculate(value1, value2):
	# in
	max_spread = 1
	# get the difference between the values
	spread  = value1 - value2
	max_spread = 0 

	# check if the result is grater than 0
	if spread > max_spread:
		# if true assign the result to maximum spread
		max_spread = spread
		# return the maximum spread
		return max_spread



if __name__=="__main__":main()