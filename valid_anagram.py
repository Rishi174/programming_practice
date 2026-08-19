class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_1 = {}
        dict_2 = {}
        for i in range(len(s)):
            dict_1[s[i]] = dict_1.get(s[i], 0) + 1
            dict_2[t[i]] = dict_2.get(t[i], 0) + 1
        for i in dict_1:
            if dict_1.get(i, 0) != dict_2.get(i, 0):
                return False
        return True
