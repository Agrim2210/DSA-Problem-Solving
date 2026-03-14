'''
LeetCode 1425 - Constrained Subsequence Sum
https://leetcode.com/problems/constrained-subsequence-sum/

Approach:
This problem can be solved using Dynamic Programming + Monotonic Deque.

Let dp[i] represent the maximum subsequence sum that ends at index i.
For each element, we can extend the best subsequence from the previous
k indices or start a new subsequence from nums[i].

Transition:
dp[i] = max(nums[i], nums[i] + max(dp[j]))  where i-k <= j < i

To efficiently find max(dp[j]) in the last k window, we maintain a
monotonic decreasing deque storing indices of dp values.

Deque rules:
1. Remove indices from the front if they are outside the window (i-k).
2. The front always holds the maximum dp value in the current window.
3. Remove smaller dp values from the back to maintain decreasing order.

Time Complexity: O(n)
Space Complexity: O(n)
'''
from collections import deque
class Solution:
    def subsequence_sum(self,nums,k):
        n=len(nums)
        dq=deque()
        dp=[0]*n
        dp[0]=nums[0]
        dq.append(0)
        for i in range(1,n):
            while dq and i-dq[0]>k:
                dq.popleft()
            dp[i]=max(nums[i],nums[i]+dp[dq[0]])
            while dq and dp[dq[-1]]<dp[i]:
                dq.pop()
            dq.append(i)
        return max(dp)            
s=Solution()
print(s.subsequence_sum([10,2,-10,5,20],2))        
