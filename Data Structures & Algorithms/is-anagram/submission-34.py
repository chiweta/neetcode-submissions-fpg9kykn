class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS={}
        countT={}
        if len(s)!=len(t):
            return False
        for c in range(len(s)):
            countT[t[c]]=1+countT.get(t[c],0)
            countS[s[c]]=1+countS.get(s[c],0)
        return countS==countT