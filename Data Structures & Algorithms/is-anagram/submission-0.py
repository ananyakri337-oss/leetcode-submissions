class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf, tf = {}, {}
        if len(s) != len(t):
            return False
        for char in s:
            sf[char] = sf.get(char, 0) + 1
        for char in t:
            tf[char] = tf.get(char, 0) + 1
        if sf == tf:
            return True
        return False