class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_l = -1
        res=[]

        for can in candies:
            max_l = max(max_l,can)

        for can in candies:
            if can + extraCandies >= max_l:
                res.append(True)
            else:
                res.append(False)
        
        return res