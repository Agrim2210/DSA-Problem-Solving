"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/

Approach:
Use hashmap to store visited elements.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i


print(twoSum([2,7,11,15], 9))