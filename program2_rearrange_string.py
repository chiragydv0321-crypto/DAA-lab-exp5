"""
Experiment 5: Heap Applications
Program 2: Rearrange String
Aim: Rearrange characters so that no adjacent characters are the same.
"""

from collections import Counter
import heapq

def rearrange_string(s):
    counts = Counter(s)
    heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(heap)
    result, previous = [], (0, "")
    while heap:
        count, char = heapq.heappop(heap)
        result.append(char)
        if previous[0] < 0:
            heapq.heappush(heap, previous)
        count += 1
        previous = (count, char)
    answer = ''.join(result)
    return answer if len(answer) == len(s) else ""

print(rearrange_string("aaabbc"))
