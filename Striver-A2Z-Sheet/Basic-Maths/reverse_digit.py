class Solution:
    def reverseNumber(self, n):
        revNum = 0
        while n > 0:
            revNum = revNum * 10 + n % 10
            n //= 10

        return revNum

obj = Solution()
n = 12345
print(f"The reverse of {n} is {obj.reverseNumber(n)}")


