class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_area = 0

        while (left < right):
            curr_area = min(height[left], height[right]) * abs(left - right)
            if max_area < curr_area:
                max_area = curr_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area