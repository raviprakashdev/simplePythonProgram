# function to partition the list
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]  # pivot element

    for j in range(low, high):
        # If current element is smaller than the pivot, swap the element with pivot
        if arr[j] <= pivot:
            i = i + 1
            # swapping the elements
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# sorting the partitioned lists
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at correct place in sorted array
        pi = partition(arr, low, high)
        # sort the partitions

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# driver function
if __name__ == "__main__":
    arr = [12, 5, 30, 8, 16, 3, 14, 7]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print(arr[i], end=" ")
