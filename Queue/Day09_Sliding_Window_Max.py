"""
LeetCode Problem:
Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

Approach: Monotonic Deque (Optimal O(n))

Idea:
We maintain a deque that stores indices of elements in decreasing order of their values.

Key Observations:
1. The front of the deque always holds the index of the maximum element of the current window.
2. When we move the window:
   - Remove indices that are outside the window.
3. Before inserting a new element:
   - Remove elements from the back that are smaller than the current element,
     because they will never be the maximum while the current element exists.

Why this works:
Each element is pushed and popped at most once → O(n) time complexity.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()     
        result = []

        for i in range(len(nums)):

            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
s=Solution()
print(s.maxSlidingWindow([2,-1,2],2))        