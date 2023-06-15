import random
import time
# Naive Search: scan the entire list and asks if its equal to the target
# if yes, return the index
# if no, return -1

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

list = []

naive_search

# binary search
# we will use leverage the fact that our list is sorted
# Method 1
def binary_search(arr, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if arr[midpoint] == target:
        return midpoint
    elif target < arr[midpoint]:
        return binary_search(arr, target, low, midpoint - 1)
    else: # target > arr[midpoint]
        return binary_search(arr, target, midpoint + 1, high)

if __name__ == '__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(sorted_list)

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start) / length, " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start) / length, " seconds")
