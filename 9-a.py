# Write a Python program that matches a string that has an a followed by one or more b's.
import re
s = "boring, bory, alvida"
s = re.split('^b.', s)
print(s)