"""
Analysis:
If string s1 and s2 are scramble strings, there must be a point that breaks s1 to two parts s11, s12, and a point that breaks s2 to two parts, s21, s22, and isScramble(s11, s21) && isScramble(s12, s22) is true, or isScramble(s11, s22) && isScramble(s12, s21) is true.

So we can make it recursively. We just break s1 at different position to check if there exists one position satisfies the requirement.

Some checks are needed otherwise it will time out. For example, if the lengths of two strings are different, they can’t be scramble. And if the characters in two strings are different, they can’t be scramble either.

Another way is to use DP. I use a three dimension array scramble[][][] to save the states. What scramble[k][i][j] means is that two substrings of length k, one starts from i of string s1, another one starts from j of string s2, are scramble. We are trying to find scramble[L][0][0]. For every length k, we try to divide the string to two parts differently, checking if there is a way that can make it true.
"""
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
        
        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]): 
                return True
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]): 
                return True
        return False
            
