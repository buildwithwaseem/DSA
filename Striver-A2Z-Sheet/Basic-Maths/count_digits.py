'''	Count all Digits of a Number '''

#Brute Force Approach
def countDigits(N):
    count = 0
    while N > 0:
        count += 1
        N //= 10
    return count
if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)



#Optimal Approach

import math
def countDigits(N):
    return math.floor(math.log10(N)) + 1



if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)
