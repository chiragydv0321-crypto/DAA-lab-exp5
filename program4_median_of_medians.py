"""
Experiment 5: Heap Applications
Program 4: Median-of-Medians
Aim: Find the kth smallest element using deterministic selection.
"""

def median_of_medians(a, k):
    if len(a) <= 5:
        return sorted(a)[k - 1]
    groups = [a[i:i + 5] for i in range(0, len(a), 5)]
    medians = [sorted(g)[len(g) // 2] for g in groups]
    pivot = median_of_medians(medians, (len(medians) + 1) // 2)
    low = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    high = [x for x in a if x > pivot]
    if k <= len(low):
        return median_of_medians(low, k)
    if k <= len(low) + len(equal):
        return pivot
    return median_of_medians(high, k - len(low) - len(equal))

print(median_of_medians([7, 10, 4, 3, 20, 15], 3))
