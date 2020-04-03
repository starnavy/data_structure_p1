# data_structure_p1

### Task 0:
- Worst case time-complexity: O(1).
- Reason: We are accessing the first and last value from the lists (calls and texts) by an index.

### Task 1:
- Worst case time-complexity: O(n), n is the total number of records in texts and calls.
- Reason: We need to go through all the elements in the texts and calls list in the for loop.

### Task 2:
- Worst case time-complexity: O(n), n is the total number of records in calls.
- Reason: First, we need to go through all the elements in the calls list; and then we search the result for the max usage time at the complexity of O(n) in the worst condition when each phone number is only used once in the data file.

### Task 3:
- Worst case time-complexity: O(nlog(n)), n is the total number of records in calls.
- Reason: First, we need to go through all th elements in the calls to get each phone call's area code and count the number of calls, the time complexity of O(n). Second, we need to sort the result. The worst condition would be that each phone has a different area code, therefore, we have to sort the n area codes at the time complexity of O(nlog(n)).

### Task 4:
- Worst case time-complexity: O(n), n is the total number of records in texts and calls.
- Reason: First, we need to go through all th elements in the calls/texts to get each phone call's area code and count the number of calls, the time complexity of O(n). Second, we need to sort the result. The worst condition would be that all the phone numbers can be classified as telemarketers, therefore, we have to sort the n area codes at the time complexity of O(nlog(n)).
