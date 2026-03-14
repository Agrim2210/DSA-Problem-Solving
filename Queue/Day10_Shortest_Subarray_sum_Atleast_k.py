'''
LeetCode: Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Approach (Prefix Sum + Monotonic Deque) — O(n)

1. Compute prefix sum array where:
   prefix[i] = sum of nums[0..i-1]

2. We want the smallest length (i - j) such that:
   prefix[i] - prefix[j] >= k

3. Use a deque to store indices of prefix sums in increasing order.

4. For each index i:
   - While deque is not empty and
     prefix[i] - prefix[dq.front()] >= k
     → update answer with (i - dq.front())
     → pop front (since we found a valid shorter subarray)

   - While deque is not empty and
     prefix[i] <= prefix[dq.back()]
     → pop back (maintain increasing prefix sums)

   - Push current index i into deque.

5. Return the minimum length found, otherwise -1.

Key Idea:
The deque keeps candidate starting points with increasing prefix sums,
allowing us to quickly find valid subarrays and maintain optimal indices.
'''
from collections import deque
class Solution:
    def shortest_Subarray(self,nums,k):
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        dq=deque()
        ans=float('inf')
        for j in range(n+1):
            while dq and prefix[j]-prefix[dq[0]]>=k:
                ans=min(ans,j-dq.popleft())
            while dq and prefix[j]<=prefix[dq[-1]]:
                dq.pop()
            dq.append(j)
        return ans if ans!=float("inf") else -1
s=Solution()
print(s.shortest_Subarray([2,-1,2],3))                    
