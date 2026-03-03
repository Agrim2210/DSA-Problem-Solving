"""
Problem: Majority Element
Platform: LeetCode
Link: https://leetcode.com/problems/majority-element/

Approach:
Use Boyer-Moore Voting Algorithm.
Maintain a candidate and a count.
If count becomes 0, choose new candidate.
Increase count if element matches candidate, otherwise decrease.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
nums = [2,2,1,1,1,2,2]
print(majority_element(nums))