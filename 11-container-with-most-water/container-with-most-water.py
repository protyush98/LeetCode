class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        end = len(height)-1
        area =  float('-inf')
        
        while(low<end):
            area = max(area,min(height[low],height[end])*(end-low))

            if(height[low]<height[end]):
                low += 1
            else:
                end -= 1

        
        return area