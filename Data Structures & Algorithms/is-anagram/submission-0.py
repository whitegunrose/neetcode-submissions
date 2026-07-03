class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        word1 = {}
        word2 = {}

        for letter in s:
            if word1.get(letter) is not None:
                word1[letter] += 1
            else:
                word1[letter] = 1

        for letter in t:
            if word2.get(letter) is not None:
                word2[letter] += 1
            else:
                word2[letter] = 1

        return word1 == word2