""""
Leetcode 49: Group Anagrams

Problem Description:
Given an array of strings `strs`, group the anagrams together. An anagram is a word formed by rearranging the letters of another word using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach:
1. **Hash Map with Sorted Strings**: 
   - Use a dictionary to group strings by their sorted character representation.
2. **Iterate Through the List**:
   - For each string, sort its characters and use the sorted string as a key in the dictionary.
   - Append the original string to the corresponding key's list.
3. **Return Values**: 
   - Finally, return all the grouped lists as the result.

Time Complexity: **O(n * k log k)** where `n` is the number of strings and `k` is the maximum length of a string.
Space Complexity: **O(nk)** for the grouped anagrams storage.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to hold sorted string as key and list of anagrams as value
        anagrams = defaultdict(list)

        # Iterate through each word in the list
        for word in strs:
            # Sort the word and use the sorted string as the key
            sorted_word = ''.join(sorted(word))

            # Append the original word to the corresponding anagram group
            anagrams[sorted_word].append(word)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

# Example usage
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

