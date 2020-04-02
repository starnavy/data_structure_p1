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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def get_phone_code(phone_number):
  """
  Extract the code from a given phone_number:
  Args:
    string: phone_number
  Returns:
    string: area code
  """
  if phone_number[0] == '(':
    code = phone_number[0:phone_number.find(')')+1]
  elif phone_number[0:3] == '140':
    code = '140'
  elif phone_number[0] in list('789'):
    code = phone_number[0]
  else:
    code = phone_number[0]
  return code


def calls_by_somearea(calls_list, area_code):
  """
  Extract all area code of phone calls maked by Bangalore fixed phones (with area code '(080)')
  Args:
    list: a list of calls with the first item as caller, the second item as receiver
    string: area code like '(080)' for Bangalore
  Returns:
    dictionary: the key is the area code, and the value is the count of calls
  """
  codes = {}
  for c in calls_list:
    caller = c[0]
    receiver = c[1]
    if get_phone_code(caller) == area_code:
      code = get_phone_code(receiver)
      if code in codes:
        codes[code] += 1
      else:
        codes[code] = 1
  return codes


# Part A

Bangalore_code = '(080)'
calls_by_Bangalore = calls_by_somearea(calls, Bangalore_code)

print("The numbers called by people in Bangalore have codes:")
print(sorted(calls_by_Bangalore.keys()))

# Part B
pct = 100 * float(calls_by_Bangalore[Bangalore_code])/sum(calls_by_Bangalore.values())
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(pct))