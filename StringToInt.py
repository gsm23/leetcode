
"""
https://leetcode.com/problems/string-to-integer-atoi/description/
    
Implement the myAtoI(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoI(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

"""


def myAtoI(s: str) -> int:
        s = s.lstrip()
       
        flag = -1 if s[:1] == '-' else 1
        
        s = s[1:] if s.startswith('-') or s.startswith('+') else s
        if not s[:1].isdigit():
            return 0

        result=""
        for chr in s:
            if chr.isdigit():
                result+=chr
            else:
                break
        if int(result)*flag < -(2**31):
            return (2**31)*flag
        elif int(result)*flag> (2**31)-1:
            return (2**31)-1*flag
        else:
            return(int(result) * flag)
    
if "__name__"=="__name__":
    print(myAtoI("-91283472332"))

