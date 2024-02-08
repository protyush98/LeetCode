class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = 2**31

        for num in nums:
            if num > b:
                return True
            if a > num:
                a = num
            if a < num and num < b:
                b = num
        
        return False
