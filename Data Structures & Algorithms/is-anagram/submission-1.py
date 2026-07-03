class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        word1 = {}
        word2 = {}

        # Add each letter of `s` to  dictionary
        for letter in s:
            if word1.get(letter) is not None:
                word1[letter] += 1 # Increment each count
            else:
                word1[letter] = 1 # Starting counter

        for letter in t:
            if word2.get(letter) is not None:
                word2[letter] += 1
            else:
                word2[letter] = 1

        # If dictionaries are equal (anagram), it will return true
        # If dictionaries are not equal, it will return false
        return word1 == word2