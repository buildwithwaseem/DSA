""" Check if a number is Palindrome or Not """
def isPalindrome(n):
    revNum = 0
    dup = n
    while n > 0:
        id = n % 10
        revNum = (revNum * 10) + id
        n = n // 10

    return revNum == dup

number = int(input("Enter a number: "))
if isPalindrome(number):
    print(f"{number} is a Palindrome number.")
else:
    print(f"{number} is not a Palindrome number.")  
    