'''
Leetcode link:
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

Problem:
Given nums and limit, return the length of the longest subarray where
max(nums) - min(nums) ≤ limit.

Python Approach (Sliding Window + Monotonic Deques)

Idea (1-line):
Maintain max queue and min queue for the current window; shrink window when max-min > limit.

Time Complexity: O(n)
Space Complexity: O(n)
'''
from collections import deque
def abs_diff(nums,limit):
    max_dq=deque()
    min_dq=deque()
    left=0
    ans=0
    for right in range(len(nums)):
        while max_dq and nums[max_dq[-1]]<nums[right]:
            max_dq.pop()
        max_dq.append(right)
        while min_dq and nums[min_dq[-1]]>nums[right]:
            min_dq.pop()
        min_dq.append(right)
        while nums[max_dq[0]]-nums[min_dq[0]]>limit:
            if max_dq[0]==left:
                max_dq.popleft()
            if min_dq[0]==left:
                min_dq.popleft()
            left+=1
        ans=max(ans,right-left+1)
    return ans

print(abs_diff([8,2,4,7],4))                


