'''
Welcome Andrew S Metell from Using Python to Access Web Data

Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_100091.html (Sum ends with 44)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_100091.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
  # Look at the parts of a tag
  # print('TAG:', tag)
  # print('URL:', tag.get('href', None))
  # print('Contents:', tag.contents[0])
  # print('Attrs:', tag.attrs)
  #use regex to grab number string, turn to in, add to sum
  nums = re.findall('[0-9]+', tag.contents[0])
  for each in nums :
    sum = sum + int(each)
  print('Sum', sum)
    
    