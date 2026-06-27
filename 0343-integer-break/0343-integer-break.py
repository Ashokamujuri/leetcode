class Solution:
    def integerBreak(self, n: int) -> int:
        # Base cases for n = 2 and n = 3 because the problem requires k >= 2 splits
        if n == 2:
            return 1  # 1 + 1 -> 1 * 1 = 1
        if n == 3:
            return 2  # 2 + 1 -> 2 * 1 = 2
        
        # For n >= 4, we want to maximize the number of 3s
        remainder = n % 3
        
        if remainder == 0:
            # Perfectly divisible by 3
            return 3 ** (n // 3)
        elif remainder == 1:
            # If the remainder is 1, take one 3 back and combine it into a 4 (2 * 2)
            # because 3 * 1 < 2 * 2
            return (3 ** ((n // 3) - 1)) * 4
        else:
            # If the remainder is 2, just multiply the accumulated 3s by 2
            return (3 ** (n // 3)) * 2