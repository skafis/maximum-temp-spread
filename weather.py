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


# import pandas module as varible p
import pandas as pd

# open the the weather.dat file
open_file = pd.read_csv('weather.dat', sep='\s+')

# get the columns we need and strip off any non integer character bypassing an an anonymous
# function as an argument to openfile
open_file[['MxT', 'MnT']] = open_file[['MxT', 'MnT']].apply(lambda x: x.str[:2].astype(int))

# find the difference between the two columns
spread = open_file.MxT - open_file.MnT

# find the maximum spread and the index 
max_spread = spread.index[spread==max(spread)].tolist()

# find the row with the highest spread unstack them to a list 
max_spread_column = open_file.loc[max_spread][['Dy', 'MxT', 'MnT']].unstack().tolist()

# customize the results to get the desired output
print max_spread_column[0], max_spread_column[1]-max_spread_column[2]
