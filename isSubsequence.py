'''
A subsequence is seemingly pulled from original, in same order.
1) Drop value and all before in seq after value matched
2) Match next value on the modified seq.
5) s = '' == True

'''

class Solution():
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            t_indx = t.find(char)
            if t_indx == -1:#if char DNE in t
                return False
            else:#drop all chars [0,indx], t now equal to chars not yet found with indx
                t = t.split(t[t_indx], 1)[1]
        return True


# t = "ahbgdc"
t = "baaaaaa"
# t = "baab"

# s = "abc"
# s = "axc"
# s = ""
# s = "abdc"
# s = "aaaaaaaaaa"
s = "ab"


# s = input("Enter a string: \n")

soln = Solution()
print(soln.isSubsequence(s,t))