class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res=''

        for indx in range(0,min(len(word1),len(word2))):
            res += word1[indx] + word2[indx]
        
        res += word1[indx+1:]
        res += word2[indx+1:]

        return res 