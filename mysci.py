# Using this page for instruction: https://ncar.github.io/python-tutorial/tutorials/beginner.html#reading-a-txt-file

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill': 12}

# Data types for each column (oonly if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

# Initialize my data variable
#data = []
#data = {'date':[], 'time':[], 'tempout':[]} #dictionary key
#time = data['time']
data = {}
for column in columns:
   data[column] = []

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
   # data = datafile.read()
   # read the first three lines (header)
   for _ in range(3): # the _ is our iterator: similar to "for i in [0, 1, 2]:"
      # print(_)
      datafile.readline()
      #headerline = datafile.readline()
      #print(headerline)
   # Read and parse the rest of the file
   #for line in datafile:
      #datum = line.split() # () space separated (,) comma seperated ('/t') tab seperated
      #data.append(datum) # Adds datum to end list of lists of strings 
   #for line in datafile:
      #split_line = line.split()
      #data['date'].append(split_line[0])
      #data['time'].append(split_line[1])
      #data['tempout'].append(float(split_line[2])) # Turn temp into a float rather than string
   for line in datafile:
      split_line = line.split()
      for column in columns:
         i = columns[column]
         t = types.get(column, str)
         value = t(split_line[i])
         data[column].append(value)

# DEBUG 
#print(data) - # Print the data read in
#print('data') # Print the word "data"
#print(type(data)) # Print the data type
#for datum in data:
   #print(datum)
#print(data[0]) # python is 0-based language so this is an index list
#print(data[9])
#print(data[-1]) # print last index (-2 would be second to last, etc.)
#print(data[0:10]) # print first 10 data lists
#for datum in data[:10:2]: # if you don't specify the starting index it will assume you are starting at the first index, secod colon is a step
   #print(datum)
#print(data[8][4]) # Pulls data from index 8 and then index 4 of 8
#print(data[8][:5])
#print(data[8][::2])
#print(data[5:8][0])
#print(data[5])
#print(data['time'])
#print(data['tempout'])
#print(data['tempout'])

# Compute the wind chill  temperature
def compute_windchill(t, v):
   a = 35.74
   b = 0.6215
   c = 35.75
   d = 0.4275

   v16 = v ** 0.16
   wci = a + (b * t) - (c * v16) + (d * t * v16)
   return wci

# DEBUG use function zip to match elements from two lists
#for i, j in zip([1,2],[3, 4, 5]):
   #print(i, j)

# Running the function to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
   windchill.append(compute_windchill(temp, windspeed))

# DEBUG
#print(windchill)
for wc_data, wc_comp in zip(data['windchill'], windchill):
   print(f'{wc_data:.5f}   {wc_comp:.5f}   {wc_data - wc_comp:.5f}')

