hrs = input("Enter Hours: ")
h = float(hrs)
r = float(input("Enter rate: "))

if h <= 40:
	print(40*r)
else:
	print(40*r + (h-40)*r*1.5)