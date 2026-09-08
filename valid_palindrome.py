class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for char in s:
            if char.isdigit() or char.isalpha():
                new_s += char
        lp = 0
        rp = len(new_s) - 1
        while lp < rp:
            if new_s[lp] != new_s[rp]:
                return False
            lp += 1
            rp -= 1
        return True
