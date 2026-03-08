"""
Problem: Product of Array Except Self
Platform: LeetCode
Link: https://leetcode.com/problems/product-of-array-except-self/

Approach:
Compute prefix products and suffix products.
For each index, multiply product of elements before it and after it.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result