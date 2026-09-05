class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            length = str(len(s))
            encoded_str += length + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        output_list = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_of_string = int(s[i:j])
            output_list.append(s[j + 1 : j + 1 + length_of_string])
            i = j + 1 + length_of_string
        return output_list
