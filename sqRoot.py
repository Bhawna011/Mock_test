# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 

#  Example 1:
# Input: x = 4 Output: 2 Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8 Output: 2 Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
# Constraints:

# 0 <= x <= 2^31 - 1


def solve(x):
    start=0
    end=x/2
    
    if x<=1:
        return x

    while start<=end:
        mid=int(start+(end-start) /2)
        if mid**2>x:
           end=mid-1
        elif mid**2<x:
           start=mid+1
        else:
           return mid        
    return end


# test code 
x=16
result=solve(x)
print(result)