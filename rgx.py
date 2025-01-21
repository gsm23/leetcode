"""
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial). 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

"""


#The recursion solution
def isMatch(s:str, p:str) -> bool:
    if not p:
        return not s
    
    print(f"s: {s}, p: {p}")
    
    first_match=bool(s) and p[0] in {s[0], "."}
    
    if len(p)>=2 and p[1]=="*":
        return isMatch(s, p[2:]) or first_match and isMatch(s[1:], p)
    else:
        return first_match and isMatch(s[1:], p[1:])

# the dynamic programing solution
def ismatch(t:str, p:str) -> bool:
    c={}
    print(f"t: {t}, p: {p}")
    def dp(i:int, j:int) -> bool:
        if (i,j) not in c:
            if j==len(p):
                ans=i==len(t)
            else:
                first_match=i<len(t) and p[j] in {t[i], "."}
                if j+1<len(p) and p[j+1]=="*":
                    ans=dp(i,j+2) or first_match and dp(i+1,j)
                else:
                    ans=first_match and dp(i+1,j+1)
            c[i,j]=ans
        return c[i,j]
    return dp(0,0)
    
if __name__=="__main__":
    print(ismatch("mission","mis*io"))