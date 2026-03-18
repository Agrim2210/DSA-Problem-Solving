'''
Problem- Find Max  Sum of Subarray  of Size k
Optimal Solution- Using sliding window+two pointer
Time Complexity-O(n)
Space Complexity-O(1)
'''
def max_sum(nums,k):
    curr_sum=0
    max_sum=float("-inf")
    l=0
    for r in range(len(nums)):
        curr_sum+=nums[r]
        if (r-l+1)==k:
            max_sum=max(max_sum,curr_sum)
            curr_sum-=nums[l]
            l+=1
    return max_sum        
print(max_sum([1,3,5,6,7,4,0],3))