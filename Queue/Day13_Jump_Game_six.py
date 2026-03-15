'''
LeetCode:1696 Jump Game VI
https://leetcode.com/problems/jump-game-vi/

You are given an integer array nums and an integer k.
You can jump at most k steps forward.
Return the maximum score you can get when reaching the last index.

Approach (Monotonic Deque + DP)

Key idea:

Let dp[i] = max score to reach index i

Transition
dp[i] = nums[i] + max(dp[j]) for i-k ≤ j < i

We maintain a deque storing indices with decreasing dp values

The front always gives the maximum dp within window

Why deque?

Keeps O(n) complexity

Efficient sliding window maximum

Time Complexity: O(n)
Space Complexity: O(n) (can be optimized to O(k))

'''
from collections import deque
class Solution:
    def max_score(self,nums,k):
        n=len(nums)
        dq=deque()
        dp=[0]*n
        dp[0]=nums[0]
        dq.append(0)
        for i in range(1,n):
            while dq and i-dq[0]>k:
                dq.popleft()
            dp[i]=nums[i]+dp[dq[0]]
            while dq and dp[dq[-1]]<dp[i]:
                dq.pop()
            dq.append(i)
        return dp[-1]
s=Solution()
print(s.max_score([1,-1,-2,4,-7,3],2))                        