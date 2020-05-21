'''
A modified Kaprekar number is a positive whole number with a special property. 
If you square it, then split the number into two integers and sum those integers, you have the same value you started with.

Consider a positive whole number  with  digits.
We square  to arrive at a number that is either  digits long or  digits long. 
Split the string representation of the square into two parts,  and . The right hand part,  must be  digits long. 
The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get .
'''

def kaprekar(n):
    s = str(n**2)
    r = s[len(s)//2:]
    l = '0' if s[:len(s)//2]=='' else s[:len(s)//2]
    return True if int(l)+int(r) == n else False

p,q = int(input()), int(input())
kaps =[]
while p<=q:
    if kaprekar(p):
        kaps.append(p)
    p += 1

if len(kaps) == 0:
    print("INVALID RANGE")
else:
    print(*kaps)
