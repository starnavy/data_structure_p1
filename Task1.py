"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_numbers = []

for t in texts:
    if t[0] not in phone_numbers:
        phone_numbers.append(t[0])
    if t[1] not in phone_numbers:
        phone_numbers.append(t[1])
        
for t in calls:
    if t[0] not in phone_numbers:
        phone_numbers.append(t[0])
    if t[1] not in phone_numbers:
        phone_numbers.append(t[1])

count = len(phone_numbers)
print("There are {} different telephone numbers in the records.".format(count))