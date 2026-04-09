class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen= set() #creates a hashset and these are great for checking uniqueness
        for num in nums: #you iterate through each number in the list of numbers 
            if num in seen: # you check if that number youre on is in the hashset already
                return True # if its already in the hashset you return True
            seen.add(num) # if its not in the hashset yet you add it to the hashset so that you continue to iterate and if that number is in there again it will return true.
        return False # if its not in the hashset then you return it as false as it contains no duplicates.
