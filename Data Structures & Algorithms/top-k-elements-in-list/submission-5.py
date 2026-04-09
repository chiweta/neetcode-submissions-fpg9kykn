class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: #[2,3,3,3,3,4,4,4] k=2
                                                                  #0 1 2 3 4 5 6 7 8 
                                                                  #  2   4 3
        count = {}

        for num in nums:
            count[num]=1+count.get(num,0)
        freq=[[] for x in range (len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res