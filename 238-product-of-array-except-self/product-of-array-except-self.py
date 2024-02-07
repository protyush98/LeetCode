class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_p=[1]
        mul_s=[1]
        
        for num in nums:
            mul_p.append(mul_p[-1]*num)
        
        for num in nums[::-1]:
            mul_s.append(mul_s[-1]*num)
        
        mul_s.reverse()
        
        ans = [(mul_s[i+1] * mul_p[i]) for i in range(0,len(nums))]

        return ans