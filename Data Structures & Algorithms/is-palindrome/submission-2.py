class Solution:
    def isPalindrome(self, s: str) -> bool:

        # declaring ints as pointers for front and back
        front: int = 0
        back: int = len(s) - 1

        # trace pointers through string
        while (front < back):

            # check front and back and see if they're alphanumeric
            if not s[front].isalnum():

                # skip non-alphanumeric chars
                front += 1

            elif not s[back].isalnum():
                back -= 1

            #
            else:

                # Compare front and back
                # if not equal, return false
                if not s[front].lower() == s[back].lower():
                    return False

                # move pointers closer inwards
                front += 1
                back -= 1

        return True