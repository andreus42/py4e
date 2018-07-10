'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_100094.json (Sum ends with 96)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url = 'http://py4e-data.dr-chuck.net/comments_100094.json'
url = input('Enter location:')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Make connecttion, read data, parse .json
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
info = json.loads(data.decode())

print('Retrieving', url)
print('Retrieved', len(data), 'characters')

count = 0
sum = 0

# Loop through a dictionary of list (info[comments]) of dictionaries (name, count)
for each in info['comments'] :
  sum += int(each['count'])
  count += 1

print('Count:', count)
print('Sum:', sum)