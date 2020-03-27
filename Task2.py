"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#print(texts[0])
#print(calls[0])

phone_time = {}

for t in calls:
    if t[0] not in phone_time:
        phone_time[t[0]] = 0
    else:
        phone_time[t[0]] += int(t[3])

for t in calls:
    if t[1] not in phone_time:
        phone_time[t[1]] = 0
    else:
        phone_time[t[1]] += int(t[3])

max_usage = 0
max_key = None
for key in phone_time:
    if phone_time[key] > max_usage:
        max_usage = phone_time[key]
        max_key = key

print("{} spent the longest time, {} seconds, on the phone during 2016".format(max_key, max_usage))