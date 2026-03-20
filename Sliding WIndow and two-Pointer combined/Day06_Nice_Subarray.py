'''
Leetcode Link-
https://leetcode.com/problems/count-number-of-nice-subarrays/description/


Description-
We have to find number of nice subarrays ie number of subarray with exacty K odd number
Approach- We can find it using formula atmost(k)-atmost(k-1) as it exactly give 
Number of subarray with Exactly K number
'''



def exactly_k(nums,k):
    def atmost(k):
        l=0
        count=0
        odd=0
        for r in range(len(nums)):
            if nums[r]%2!=0:
                odd+=1
            while odd>k:
                if nums[l]%2!=0:
                    odd-=1
                l+=1
            count+=(r-l+1)
        return count
    return atmost(k)-atmost(k-1)
print(exactly_k([1,1,2,1,1], 3))                        
