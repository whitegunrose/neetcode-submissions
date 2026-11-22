import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # get rid of punctuation
        s = s.translate(s.maketrans("", "", string.punctuation))

        # get rid of spaces
        s = ''.join(s.split(' '))

        # make all lowercase
        s = s.lower()

        # pointer indicies
        fIdx = 0
        bIdx = len(s) -1

        while (fIdx != bIdx and fIdx < len(s) and bIdx > -1):

            # pointers
            pFront = s[fIdx]
            pBack = s[bIdx]
            
            if pFront != pBack:
                return False
            
            else:
                fIdx += 1
                bIdx -= 1

        return True