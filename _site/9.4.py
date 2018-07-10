'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
#name = "mbox-short.txt"

handle = open(name)
counts = dict()

for line in handle:
  if not line.startswith("From ") : continue
  current = (line.rstrip()).split()
  email = (current[1])
  counts[email] = counts.get(email, 0) + 1

top_emailer = None
email_count = None

for emailer, emails in counts.items():
  if top_emailer is None or emails > email_count:
    top_emailer = emailer
    email_count = emails

print(top_emailer, email_count)