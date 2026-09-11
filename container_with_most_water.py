class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            area = length * height

            max_area = max(area, max_area)

            # move pointers
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
