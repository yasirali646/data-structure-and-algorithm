"""
    Bubble Sort
    Bubble sort is a simple sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
"""

class Solution:
    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    

arr = [0, 3, 4, 5, 2, 1]
print(Solution().bubble_sort(arr))