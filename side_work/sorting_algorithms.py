# Merge sort algorithm

"""
STEPS
- use recursion to half the array until you have 
each elt in its own array smaller array
- now go back and merge the smaller arrays by sorting
until you have one sorted array 
"""

def merge_sort(arr):
    # split the arr into two parts
    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) //2:]

        # use recursion to break down the arr into single elt 
        merge_sort(left_arr)
        merge_sort(right_arr)

        # now put the single sorted elt back into a larger sorted array 

        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # merged_arr idx

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # now there might be some left overs in either array in case their sizes weren't equal
        # merge those into the merged array 

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
    return arr

arr = [9, -3, 4, 10, 1, 5, -8]
merge_sort(arr)

# PROBLEMS

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            print(nums2[j], nums1[i], k)
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
    

# Problem 2:

    """
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) 
    time complexity and with the smallest space complexity possible.
    """


    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) > 1:
            left_arr = nums[: len(nums)//2]
            right_arr = nums[len(nums)//2 :]

            self.sortArray(left_arr)
            self.sortArray(right_arr)

            i, j, k = 0, 0, 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    nums[k] = left_arr[i] 
                    i += 1
                else:
                    nums[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                nums[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                nums[k] = right_arr[j]
                j += 1
                k += 1
        return nums

        