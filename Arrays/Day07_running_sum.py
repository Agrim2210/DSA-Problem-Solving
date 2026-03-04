"""
Problem: Running Sum of 1D Array
Platform: LeetCode
Link: https://leetcode.com/problems/running-sum-of-1d-array/

Approach:
Use prefix sum technique.
Each element becomes the sum of itself and the previous element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums