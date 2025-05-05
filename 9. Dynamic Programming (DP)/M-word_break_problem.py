"""
Leetcode 139: Word Break

Problem Description:
Given a string `s` and a dictionary of words `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The dictionary `wordDict` may contain additional words that are not part of the string `s`. The solution must return `True` if the string `s` can be segmented, otherwise return `False`.

Approach:
1. **Dynamic Programming (DP)**: We will use a DP array where `dp[i]` will be `True` if the substring `s[0:i]` can be segmented into words from `wordDict`.
2. **Iterate Through the String**: For each position `i`, check if any substring `s[j:i]` (for `j < i`) is a valid word in the dictionary, and if `dp[j]` is `True`.
3. **Return Result**: If `dp[len(s)]` is `True`, return `True` (indicating that the entire string can be segmented). Otherwise, return `False`.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)  # Convert wordDict to set for O(1) lookup
        
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can be segmented
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

#EXAMPLE USAGE:
s = "leetcode"
wordDict = ["leet", "code"]

solution = Solution()
print(solution.wordBreak(s, wordDict))  # Output: True


