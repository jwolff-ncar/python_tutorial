# Using this page for instruction: https://ncar.github.io/python-tutorial/tutorials/beginner.html#reading-a-txt-file

# Read the data file
filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')

# First attempt
#print(datafile.readline())

# Second attempt
#data = datafile.read()
#datafile.close()

# Third attempt: Using "with open" automatically closes for you - recommended option
with open(filename, 'r') as datafile:
   data = datafile.read()

# DEBUG
#print(type(data))

