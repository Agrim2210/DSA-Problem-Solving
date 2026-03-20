'''
Ques-Binary Subarray with sum K

Leetcode Link-
https://leetcode.com/problems/binary-subarrays-with-sum/description/

'''

def exactly_goal(nums,k):
    def atmost(k):
        if k<0:
            return 0
        l=0
        curr_sum=0
        count=0
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while curr_sum >k:
                curr_sum-=nums[l]
                l+=1
            count+=(r-l+1)
        return count
    return atmost(k)-atmost(k-1)
print(exactly_goal([1,0,1,0,1],2))


