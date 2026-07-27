class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        FreqS,FreqT={},{}
        for x in range (len(s)):
            FreqS[s[x]]=1+FreqS.get(s[x],0)
            FreqT[t[x]]=1+FreqT.get(t[x],0)
        return FreqS==FreqT