class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curr_val = nums[i]
            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:
                sum_ = curr_val + nums[lp] + nums[rp]
                if sum_ == 0:
                    res.append([curr_val, nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    # Handles duplicates
                    while nums[lp] == nums[lp - 1] and lp < rp:
                        lp += 1
                elif sum_ < 0:
                    lp += 1
                else:
                    rp -= 1
        return res
