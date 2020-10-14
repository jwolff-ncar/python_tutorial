# Using this page for instruction: https://ncar.github.io/python-tutorial/tutorials/beginner.html#reading-a-txt-file

# Hello World
#print("Hello, world!")

# Read the data file
filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')

# First attempt - read individual ines of a data file
#print(datafile.readline()) # Line 1
#print(datafile.readline()) # Line 2
#print(datafile.readline()) # Line 3
#print(datafile.readline()) # Line 4

# Second attempt - read all data in file
#data = datafile.read()
#datafile.close()

# Third attempt: Using "with open" automatically closes for you - recommended option
with open(filename, 'r') as datafile:
   data = datafile.read()

# DEBUG 
#print(data) - # Print the data read in
#print('data') # Print the word "data"
#print(type(data)) # Print the data type

