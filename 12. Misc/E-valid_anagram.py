"""
Leetcode 242: Valid Anagram

Problem Description:
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s` and `false` otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once. You must solve the problem in **O(n)** time complexity, where `n` is the length of the strings.

Approach:
1. **Check Lengths**: First, if the lengths of `s` and `t` are not the same, they cannot be anagrams.
2. **Use Counter**: Utilize a `Counter` from Python's `collections` module to count the frequency of characters in both strings.
3. **Compare Counters**: If the `Counter` objects of both strings are equal, then the strings are anagrams; otherwise, they are not.
"""
from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        # If the lengths of the strings differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Use Counter to count the frequency of characters in both strings
        s_count = Counter(s)
        t_count = Counter(t)

        # Compare the two Counters
        return s_count == t_count

# Example usage
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))  # Output: False

