class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for w in strs:
            count=[0]*26
            for l in w:
                count[ord(l)-ord('a')]+=1
            result[tuple(count)].append(w)
        return list(result.values())