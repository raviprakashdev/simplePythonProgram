# Merge Sort implementation
# Average Time Complexity is O(nlog(n))

# Merges two subarrays of arr[]
# First subarray is arr[l..n]
# Second subarray is arr[n+1..r]

def merge(arr, l, n, r): 
	n1 = n - l + 1
	n2 = r - n

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays
	for i in range(0 , n1):
		L[i] = arr[l + i]

	for j in range(0 , n2):
		R[j] = arr[n + 1 + j]

	# Merge the temp back into arr[l..r]
	i = 0
	j = 0
	k = l

	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else: 
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1: 
		arr[k] = L[i] 
		i += 1
		k += 1

	# Copy the remaining elements of R[]
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr,l,r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and n
		n = (l+(r-1))//2

		# Sort first and second halves
		mergeSort(arr, l, n)
		mergeSort(arr, n+1, r)
		merge(arr, l, n, r)

# Receiving an input from the user
arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	arr.append(ele)

# Calling mergeSort function
mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
	print ("%d" %arr[i])
