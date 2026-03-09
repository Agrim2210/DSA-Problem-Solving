'''
🔗 LeetCode Link

https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

Approach (Counting / Greedy):
> Instead of simulating the queue rotation, we observe:
> Students only have two preferences → 0 or 1.
> If the current sandwich is 1 but no student wants 1, the process stops.
> Same for 0.
So we just:
> Count number of students who prefer 0 and 1.
> Iterate through sandwiches.
> Reduce the count when a sandwich is eaten.

If no student wants the sandwich → stop.
Time and Space Complexity:
TC->O(n)
SC->O(1)

'''
class Solution(object):
    def countStudents(self, students, sandwiches):
        count0 = students.count(0)
        count1 = students.count(1)

        for s in sandwiches:
            if s == 0:
                if count0 == 0:
                    break
                count0 -= 1
            else:
                if count1 == 0:
                    break
                count1 -= 1

        return count0 + count1
s=Solution()
count=s.countStudents([1,1,0,0],[0,1,0,1])      
print(count)  