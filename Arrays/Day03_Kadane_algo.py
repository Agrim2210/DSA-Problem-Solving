"""
Problem: Maximum Subarray (Return Subarray)
Link: https://leetcode.com/problems/maximum-subarray/

Approach:
Use Kadane’s Algorithm.
Track start and end indices when updating maximum sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray(nums):
    current_sum = 0
    max_sum = nums[0]

    start = 0
    temp_start = 0
    end = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, nums[start:end+1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))