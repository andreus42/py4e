'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"

name = "mbox-short.txt"
handle = open(name)

counts = dict()

# Read line, Find "From", Strip
for line in handle:
  if not line.startswith("From ") : continue
  current = (line.rstrip()).split()
  time_list = (current[5]).split(":")
  hour = time_list[0]
  
  # Make dictionary for counting
  counts[hour] = counts.get(hour, 0) + 1
  hour_list = list()
  
  #Make in to tuple list for sorting
  for k, v in counts.items() :
    hour_list.append((k, v))
  
hour_list.sort()

for k,v in hour_list:
  print(k, v)
  
