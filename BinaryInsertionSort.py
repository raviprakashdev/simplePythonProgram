class Sort:
    def __init__(self, array):
        self.array = array

    def binary_insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            pos = self.binary_search(key, 0, i) + 1
            for k in range(i, pos, -1):
                self.array[k] = self.array[k - 1]
            self.array[pos] = key
        return self.array
 
    def binary_search(self, element, first, last):
        if last - first <= 1:
            if element < self.array[first]:
                return first - 1
            else:
                return first
        mid = (first + last)//2
        if self.array[mid] < element:
            return self.binary_search(element, mid, last)
        elif self.array[mid] > element:
            return self.binary_search(element, first, mid)
        else:
            return mid
            
def main():
    array = list(map(int, input("Enter unsorted array: ").split(' ')))
    obj = Sort(array)
    sorted_array = obj.binary_insertion_sort()
    print("Sorted Array: ", end = '')
    print(*sorted_array)

if __name__ == "__main__":
    main()     
