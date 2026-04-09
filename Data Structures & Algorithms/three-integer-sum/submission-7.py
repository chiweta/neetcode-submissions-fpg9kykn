class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break                       # nothing beyond here can sum to 0
            if i > 0 and a == nums[i - 1]:
                continue                    # skip duplicate 'a'

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate left values (must check l < r first!)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # (optional) also skip duplicate right values:
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1

        return res
