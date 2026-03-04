"""
Problem: Merge Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/merge-sorted-array/

Approach:
Use two pointers starting from the end of both arrays.
Compare elements from nums1 and nums2 and place the larger one at the end of nums1.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

def merge_sorted_array(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    return nums1