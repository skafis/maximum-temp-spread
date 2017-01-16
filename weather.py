#!/usr/bin/python3

def main():
	# open file
	file = open('weather.dat')
	# iterate through the file and split them and add to list 
	lst = []
	for line in file:
		lst += [line.split()]

	# get the columns that we want to work that is column 2 & 3 and remove the first two and last rows and assign it to a varailble
	col = [x[1:3] for x in lst[2:-1]]
	# iterate through the varialble to get the row value
	for val in col:
		if val:
			x,y = val
			# convert and remove non integer characters
			val1 =  int(x.strip('*'))
			val2 = int(y.strip('*'))
			# call the calculate function and pass in the variable
			calculate(val1, val2)


def calculate(val1, val2):
	max_spread = 1
	# get the difference between the values
	spread  = val1 - val2
	print spread
	

if __name__=="__main__":main()