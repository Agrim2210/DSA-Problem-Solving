"""
Problem: Subarray Sum Equals K
Platform: LeetCode
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Approach:
Use prefix sum with a hashmap to store frequencies of prefix sums.
If (current_sum - k) exists in the hashmap, it means a valid subarray exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count
x=subarray_sum([1,2,3],3)    
print(x)
