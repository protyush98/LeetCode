class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        s_l = s.split()
        s_l.reverse()

        return " ".join(s_l)