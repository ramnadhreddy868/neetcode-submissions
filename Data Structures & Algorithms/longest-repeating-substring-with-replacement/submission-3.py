class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=0
        h={}
        max_freq=0
        max_len=0
        for i in range(len(s)):
            h[s[i]]=h.get(s[i],0)+1
            max_freq = max(max_freq, h[s[i]])
            replacements=i-l+1-max_freq
            while replacements>k:
                h[s[l]]-=1
                l+=1

                replacements = (i - l + 1) - max_freq
            if i - l + 1 > max_len:
                max_len = i - l + 1
        return max_len
            

