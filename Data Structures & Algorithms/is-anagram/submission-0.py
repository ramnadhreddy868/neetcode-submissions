class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h={}
        for char in s:
            if char in h:
                h[char]+=1
            else:
                h[char]=1
        for char in t:
            if char not in h:
                return False
            h[char]-=1
            if h[char] < 0:
                return False
        return True

            