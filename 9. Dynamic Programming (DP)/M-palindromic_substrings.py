"""
Leetcode 647: Palindromic Substrings

Problem Description:
Given a string `s`, return the number of palindromic substrings in it. A string is a palindrome if it reads the same forward and backward. 

A substring is a contiguous sequence of characters within the string. The input string's length will not exceed 1000.

Approach:
1. **Expand Around Center**: 
   - For each character in the string, consider it as the center of a potential palindrome.
   - Since palindromes can be of odd or even length, expand from both single characters and pairs of adjacent characters.
2. **Count Palindromes**: Expand outward from each center while the substring remains a palindrome, and count each valid expansion.
3. **Complexity**: This method runs in **O(n²)** time complexity with **O(1)** space complexity.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Helper function to count palindromes centered at left and right
        def expandAroundCenter(s, left, right):
            count = 0
            # Expand while the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # Found a valid palindrome
                left -= 1    # Expand left
                right += 1   # Expand right
            return count
        
        total_palindromes = 0
        # Iterate through each character in the string
        for i in range(len(s)):
            # Count odd-length palindromes centered at index i
            total_palindromes += expandAroundCenter(s, i, i)
            # Count even-length palindromes centered between i and i+1
            total_palindromes += expandAroundCenter(s, i, i + 1)
        
        return total_palindromes

solution = Solution()

# Example 1
s1 = "abc"
print(solution.countSubstrings(s1))  # Output: 3 ('a', 'b', 'c')

# Example 2
s2 = "aaa"
print(solution.countSubstrings(s2))  # Output: 6 ('a', 'a', 'a', 'aa', 'aa', 'aaa')


