class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        size = len(flowerbed)

        if(size==1 and flowerbed[0]==0):
            n -= 1
            return True
        else:
            for i in range(0,size):
                if(i==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                    n -= 1
                    flowerbed[i]=1
                elif(i==size-1 and flowerbed[i]==0 and flowerbed[i-1]==0):
                    n -= 1
                    flowerbed[i]=1

                elif(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    n -= 1
                    flowerbed[i]=1
            
        if n<=0:
            return True

        return False         