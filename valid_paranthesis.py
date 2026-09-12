class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1:
            return False
        map_dict = {')': '(', ']':'[', '}':'{'}
        char_list = []
        for i in s:
            if i in ['(', '{', '[']:
                char_list.append(i)
            else:
                if len(char_list)==0 or char_list.pop() != map_dict[i]:
                    return False
        if len(char_list)!=0:
            return False
        return True
