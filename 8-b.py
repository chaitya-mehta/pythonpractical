# Write a program to copy content of one JSON file into another JSON file.
import json
f = open("example1.json")
data = json.load(f)
data = json.dumps(data)
fp = open("ex2.json", 'w')
fp.write(data)