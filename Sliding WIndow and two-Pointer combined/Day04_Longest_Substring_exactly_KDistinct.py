from collections import defaultdict
def exactly_k(s,k):
    max_count=-1
    count=defaultdict(int)
    l=0
    for r in range(len(s)):
        while len(count)>k and s[k] not in count:
            count[s[l]]-=1
            if count[s[l]]==0:
                del count[s[l]]
            l+=1
        count[s[r]]+=1
        if len(count)==k:
            max_count=max(max_count,r-l+1)        
    return max_count
print(exactly_k("aabccadef",3))