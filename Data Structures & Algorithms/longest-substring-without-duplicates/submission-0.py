class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        h=set()
        maxlen=0
        for i in range(len(s)):
            while s[i] in h:
                h.remove(s[l])
                l+=1
            h.add(s[i])
            maxlen=max(maxlen,i-l+1)
        return maxlen


        