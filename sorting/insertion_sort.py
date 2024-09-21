"""
    Insertion Sort
    Insertion sort is a simple sorting algorithm that works
    the way we sort playing cards in our hands.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
"""


class Solution:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            j = arr[i]
            k = i - 1
            while k >= 0 and j < arr[k]:
                arr[k + 1] = arr[k]
                k -= 1
            arr[k + 1] = j
        return arr

arr = [0, 3, 4, 5, 2, 1]
print(Solution().insertion_sort(arr))