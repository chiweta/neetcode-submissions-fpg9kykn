class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        FreqS={} 
        FreqT= {}
        for i in range(len(s)):
            FreqS[s[i]]=1+FreqS.get(s[i],0)
            FreqT[t[i]]=1+FreqT.get(t[i],0)
        return FreqS==FreqT