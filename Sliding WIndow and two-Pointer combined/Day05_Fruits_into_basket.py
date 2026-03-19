'''
 LeetCode 904 - Fruit Into Baskets
🔗 https://leetcode.com/problems/fruit-into-baskets/

🧩 Problem (Compact):
Given an array fruits[], where fruits[i] is the type of fruit,
return the length of the longest subarray containing at most 2 distinct types.

💡 Approach (Sliding Window):
- Use two pointers (left, right) to maintain a window
- Use a hashmap to count fruit types in the window
- Expand right pointer, add fruits[right]
- If more than 2 distinct fruits → shrink from left
- Track max window size

⏱️ Time: O(n)
📦 Space: O(1)  (since at most 3 keys in map)

🏁 Key Idea:
Longest subarray with at most 2 distinct elements
'''
from collections import defaultdict
def fruits(f):
    l=0
    count=defaultdict(int)
    res=0
    max_res=0
    for r in range(len(f)):
        while len(count)>=2 and f[r] not in count:
            count[f[l]]-=1
            res-=1
            if count[f[l]]==0:
                del count[f[l]]
            l+=1
        if f[r]!=0:
            count[f[r]]+=1
            res+=1
            max_res=max(max_res,res)
    return max_res
print(fruits([1,2,3,2,2]))            
