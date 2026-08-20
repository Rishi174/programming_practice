class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        output_list = [value for value in anagram_dict.values()]
        return output_list
