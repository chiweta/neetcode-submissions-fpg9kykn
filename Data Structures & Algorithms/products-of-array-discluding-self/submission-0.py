class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        default = [1] * (len(nums))
        prefix=1
        for i in range (len(nums)):
            default[i]= prefix
            prefix *= nums[i]
        postfix=1
        for i in range (len(nums) -1, -1, -1 ):
            default[i]*= postfix
            postfix*= nums[i]
        return default

