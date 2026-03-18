''' 
Leetcode Link-
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Problem-Find Max count of substring without repeating character 
Optimal Solution-
using sliding window+Two pointer+ set
Time Complexity-O(n)
Space complexity-O(k)

'''
def longest_substring(s):
    max_count=0
    l=0
    visit=set()
    for r in range(len(s)):
        while s[r] in visit:
            visit.remove(s[l])
            l+=1
        visit.add(s[r])
        max_count=max(max_count,r-l+1)
    return max_count
print(longest_substring("abcdeabc"))            

