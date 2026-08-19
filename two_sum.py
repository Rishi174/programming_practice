class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in prev_dict:
                return [prev_dict[diff], index]
            prev_dict[value] = index
        return []
