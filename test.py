fhand = open('mbox.txt', "r")
count = 0

for line in fhand:
  count = count + 1

print('Line Count:', count)