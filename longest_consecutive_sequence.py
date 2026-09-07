class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        current_length = 0
        for num in nums:
            if num - 1 not in nums:
                current_length = 1
                while num + 1 in nums:
                    current_length += 1
                    num += 1
            max_length = max(current_length, max_length)
        return max_length
