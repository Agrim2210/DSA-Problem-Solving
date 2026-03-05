"""
Problem: Contains Duplicate
Platform: LeetCode
Link: https://leetcode.com/problems/contains-duplicate/

Approach:
Use a set to track seen elements.
If an element already exists in the set, a duplicate is found.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False