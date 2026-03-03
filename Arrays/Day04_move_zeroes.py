"""
Problem: Move Zeroes
Platform: LeetCode
Link: https://leetcode.com/problems/move-zeroes/

Approach:
Use two pointers.
One pointer tracks position to place next non-zero element.
Traverse array and swap non-zero elements forward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeroes(nums):
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1

    return nums
nums = [0,1,0,3,12]
print(move_zeroes(nums))