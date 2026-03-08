"""
LeetCode 933 - Number of Recent Calls
Link: https://leetcode.com/problems/number-of-recent-calls/

Problem:
Design a system that counts the number of recent requests within the last
3000 milliseconds. For each ping(t), return the number of requests in the
time range [t-3000, t].

Approach:
Use a queue (deque) to store timestamps.
1. Add the new timestamp.
2. Remove timestamps from the front that are older than (t - 3000).
3. Queue length = number of valid recent calls.

Time Complexity: O(1) amortized per ping
Space Complexity: O(n)
"""

from collections import deque


class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
q=RecentCounter()

print(q.ping(3))    
print(q.ping(2000))
print(q.ping(3000))
print(q.ping(6000))