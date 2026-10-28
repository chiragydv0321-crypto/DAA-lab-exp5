"""
Experiment 5: Heap Applications
Program 3: Merge K Sorted Arrays
Aim: Merge sorted arrays using a min heap.
"""

import heapq

def merge_k_arrays(arrays):
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    result = []
    while heap:
        value, arr_id, idx = heapq.heappop(heap)
        result.append(value)
        idx += 1
        if idx < len(arrays[arr_id]):
            heapq.heappush(heap, (arrays[arr_id][idx], arr_id, idx))
    return result

print(merge_k_arrays([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
