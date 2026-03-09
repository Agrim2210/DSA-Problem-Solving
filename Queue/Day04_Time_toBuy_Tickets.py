'''
🔗 LeetCode Link

https://leetcode.com/problems/time-needed-to-buy-tickets/

Optimal Approach (Observation)-

Instead of simulating the queue, observe:
Every person before or equal to k can buy at most tickets[k] tickets.

Every person after k can buy at most tickets[k] - 1 tickets (because we stop when k finishes).

So we sum the minimum tickets they can buy.
'''
class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        target = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)

        return time
s=Solution()
time=s.timeRequiredToBuy([2,3,2],2)        
print(time)