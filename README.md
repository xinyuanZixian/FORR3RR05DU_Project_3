# FORR3RR05DU_Project_3

2.
If we set the quantity of disks as n, we need T(n) moves.
Move disks from A to C: T(n - 1).
Move the largest disk from A to B: 1.
Move disks from C to B: T(n - 1).
T(n) = T(n - 1) + 1 + T(n - 1)
T(n) = 2T(n - 1) + 1
T(n) = 2 ^ 1 * T(n - 1) + 1
T(n) = 2 ^ 2 * T(n - 2) + 1
.
.
.
T(n) = 2 ^ (n - 1) * T(n - (n - 1)) + 1
T(n) = 2 ^ (n - 1) * T(1) + 1
So the answer is O(2 ^ n).

3.
O(n) is linear time, it could be a simple for loop.
For example:
for x in range(n):
  print(x)
  
O(n ^ 2) is quadratic time, like for loop within a for loop, bubble sort and insertion sort.
For example:
for x in range(n):
  for y in range(n):
    print(x, ", ", y)
    
O(log n) is logarithmic time, like binary search.
For example:
def binary_search(arr, start, end, hkey):
	while start <= end:
		mid = start + (end - start) / 2
		if arr[mid] < hkey:
			start = mid + 1
		elif arr[mid] > hkey:
			end = mid - 1
		else:
			return mid
     return -1
