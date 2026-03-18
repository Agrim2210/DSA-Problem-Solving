'''
Leetcode Link-
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

Problem- Find Max  Sum of Distinct Subarray  of Size k
Optimal Solution- Using sliding window+two pointer + set
Time Complexity-O(n)
Space Complexity-O(k)
'''

def max_sum(nums,k):
    curr_sum=0
    max_sum=float("-inf")
    l=0
    visit=set()
    for r in range(len(nums)):
        while nums[r] in visit:
            visit.remove(nums[l])
            curr_sum-=nums[l]
            l+=1
        curr_sum+=nums[r]
        visit.add(nums[r])
        if (r-l+1)==k:
            max_sum=max(max_sum,curr_sum)
            curr_sum-=nums[l]
            visit.remove(nums[l])
            l+=1
    return max_sum
print(max_sum([1,5,4,2,9,9,9],3))                

