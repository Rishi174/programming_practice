class Solution:
    def trap(self, height: List[int]) -> int:

        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)

        prefix_max[0], suffix_max[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])

        total_water = 0
        for i in range(1, len(height) - 1):
            total_water += min(prefix_max[i], suffix_max[i]) - height[i]

        return total_water


# Two pointer approach
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        ml, mr = height[l], height[r]
        trapped_water = 0

        while l < r:
            if ml <= mr:
                l += 1
                ml = max(height[l], ml)
                trapped_water += ml - height[l]
            else:
                r -= 1
                mr = max(height[r], mr)
                trapped_water += mr - height[r]
        return trapped_water
