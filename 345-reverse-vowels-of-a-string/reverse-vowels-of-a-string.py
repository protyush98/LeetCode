class Solution:
    def reverseVowels(self, s: str) -> str:
        v_l=[]
        v_s={'a','e','i','o','u'}

        for i in range(0,len(s)):
            if(s[i].lower() in v_s):
                v_l.append(i)
        
        start = 0
        last = len(v_l) - 1
        ch_l= [ch for ch in s]

        while start < last:
            ch_l[v_l[start]],ch_l[v_l[last]] = ch_l[v_l[last]],ch_l[v_l[start]]
            start += 1
            last -= 1


        
        return "".join(ch_l)
