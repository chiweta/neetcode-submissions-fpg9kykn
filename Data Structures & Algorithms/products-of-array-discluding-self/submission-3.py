class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        default = [1]*len(nums)
        prefix = 1
        for num in range (len(nums)):
            default[num]=prefix
            prefix *= nums[num]
        postfix =1
        for num in range (len(nums)-1,-1,-1):
            default[num]*=postfix
            postfix*= nums[num]
        return default         
