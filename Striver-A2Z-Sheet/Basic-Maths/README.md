# Basic Maths - Count Digits

This folder contains a simple implementation of a classic basic-maths problem: finding the number of digits in a positive integer.

## Problem Statement
Given an integer N, determine how many digits it contains.

Example:
- Input: 329823
- Output: 6

## File Overview
- count_digits.py: contains two ways to solve the problem
- main.py: a basic starter file for the folder

## Approach 1: Brute Force
The first method repeatedly divides the number by 10 until it becomes 0, counting each division.

```python
def countDigits(N):
    count = 0
    while N > 0:
        count += 1
        N //= 10
    return count
```

### How it works
- Each loop removes one digit from the number.
- The loop continues until no digits are left.
- The variable count stores the total number of digits.

### Time Complexity
- O(d), where d is the number of digits in N

### Space Complexity
- O(1)

## Approach 2: Optimal Approach
The second method uses Python's math module to calculate the result more directly.

```python
import math

def countDigits(N):
    return math.floor(math.log10(N)) + 1
```

### How it works
- log10(N) gives the approximate number of digits in N.
- Taking the floor and adding 1 gives the exact digit count.

### Time Complexity
- O(1)

### Space Complexity
- O(1)

## Example Run
```python
N = 329823
print("N:", N)
digits = countDigits(N)
print("Number of Digits in N:", digits)
```

Output:
```text
N: 329823
Number of Digits in N: 6
```

## Notes
- This solution works for positive integers.
- For N = 0, the brute-force logic returns 0, while the logarithmic approach is not valid for 0.
- For negative numbers, you may first convert them to their absolute value.

## Learning Summary
This problem is a great beginner exercise because it teaches:
- loops and iteration
- integer division
- mathematical reasoning
- time and space complexity analysis
