class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap ={} #creating hashmap
        for i, n in enumerate(nums): #loops through nums by creating an index and value for each integer
            diff= target - n #creating a variable diff that is equal to the target number minus the value in nums
            if diff in prevmap: #if diff is in the hashmap already then 
                return [prevmap[diff],i] #return that diff number and the current index we're on
            prevmap[n]=i # regardless store the current number and its index in the prevmap
