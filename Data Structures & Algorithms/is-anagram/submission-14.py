class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #checks if the two strings are the same length
            return False #if they aren't the same length they automatically arent anagrams

        countS = {} # creating a key value pair for string s
        countT = {} # creating a key value pair for string t

        for i in range (len(s)): #iterating through letters both in that of length s/t
            countS[s[i]]= 1 + countS.get(s[i],0) #goes into hashmap of string s and the exact index youre iterating through and adding +1 to that count
            countT[t[i]]= 1 + countT.get(t[i],0) #goes into hashmap of string t and the exact index youre iterating through and adding +1 to that count
        return countS==countT #returns true or false if its equal or not