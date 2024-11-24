# Q10. Find the kth largest element in an unsorted array.

import heapq
def find_kth_largest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    
    return heap[0]
arr = [3, 2, 1, 5, 6, 4]
k = 2

print(f"The {k}th largest element is {find_kth_largest(arr, k)}")
