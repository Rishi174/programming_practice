# Two pointer approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            sum_ = numbers[lp] + numbers[rp]
            if sum_ == target:
                return [lp + 1, rp + 1]
            elif sum_ < target:
                lp += 1
            else:
                rp -= 1


# Hash Map approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_ = {}
        for index in range(len(numbers)):
            number = numbers[index]
            if number in dict_:
                return [dict_[number] + 1, index + 1]
            diff = target - number
            dict_[diff] = index
