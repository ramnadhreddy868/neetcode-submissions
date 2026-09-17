class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        h = {}
        max_len = 0

        for i in range(len(s)):
            # Add current character
            h[s[i]] = h.get(s[i], 0) + 1

            # Find most frequent character
            max_freq = max(h.values())

            # Number of replacements needed
            replacements = (i - l + 1) - max_freq

            # Shrink window if replacements exceed k
            while replacements > k:
                h[s[l]] -= 1
                l += 1

                max_freq = max(h.values())
                replacements = (i - l + 1) - max_freq

            # Update maximum length
            if i - l + 1 > max_len:
                max_len = i - l + 1

        return max_len