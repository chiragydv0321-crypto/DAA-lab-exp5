"""
Experiment 5: Heap Applications
Program 1: Heap Sort
Aim: Sort an array using a max heap.
"""

def heap_sort(a):
    a = a[:]
    n = len(a)
    def sift_down(size, root):
        while True:
            largest = root
            left, right = 2 * root + 1, 2 * root + 2
            if left < size and a[left] > a[largest]:
                largest = left
            if right < size and a[right] > a[largest]:
                largest = right
            if largest == root:
                break
            a[root], a[largest] = a[largest], a[root]
            root = largest
    for i in range(n // 2 - 1, -1, -1):
        sift_down(n, i)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(end, 0)
    return a

print(heap_sort([12, 11, 13, 5, 6]))
