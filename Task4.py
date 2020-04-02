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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# test check-in function
def get_phone_usage_summary(calls_list, texts_list):
    """
    Generate the phone usage summary including: outgoing/incoming phone calls/texts
    Args:
        list: a list of calls with the first item as caller, the second item as receiver
        list: a list of texts with the first item as sender, the second item as receiver
    Returns:
        dictionary: key is the phone number, and value is a list with 4 elements representing phone_out, phone_in, text_out, text_in respectively
    """
    phone_summary = {}
    # phone_summary[phone_number] = [phone_out, phone_in, text_out, text_in]
    for c in calls_list:
        if c[0] not in phone_summary:
            phone_summary[c[0]] = [1,0,0,0]
        else:
            phone_summary[c[0]][0] += 1
            if c[1] not in phone_summary:
                phone_summary[c[1]] = [0,1,0,0]
            else:
                phone_summary[c[1]][1] += 1
    for t in texts_list:
        if t[0] not in phone_summary:
            phone_summary[t[0]] = [0,0,1,0]
        else:
            phone_summary[t[0]][2] += 1
            if t[1] not in phone_summary:
                phone_summary[t[0]] = [0,0,0,1]
            else:
                phone_summary[t[0]][3] += 1
    return phone_summary


def get_suspicious_telemarketers(calls_list, texts_list):
    # possible telemarketers: these are numbers that make outgoing calls but NEVER send texts, receive texts or receive incoming calls.
    phone_summary = get_phone_usage_summary(calls_list, texts_list)
    suspicious_telemarketers = []
    for i in phone_summary:
        if phone_summary[i][0] > 0 and sum(phone_summary[i][1:4]) == 0:
            suspicious_telemarketers.append(i)
    return sorted(suspicious_telemarketers)


def main():
    suspicious_telemarketers = get_suspicious_telemarketers(calls, texts)
    print("These numbers could be telemarketers: ")
    for i in suspicious_telemarketers:
        print(i)

main()

