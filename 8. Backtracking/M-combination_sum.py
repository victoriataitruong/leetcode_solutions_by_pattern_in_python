"""
Leetcode 39: Combination Sum

Problem Description:
Given an array of distinct integers `candidates` and a target integer `target`, 
return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. 
You may reuse the same number from `candidates` an unlimited number of times.

Approach:
1. **Backtracking**: We will use a backtracking approach to explore all possible combinations of numbers from `candidates` that sum up to `target`.
2. **Recursion**: The recursion will try to add elements from `candidates` repeatedly until the target is reached or exceeded.
3. **Pruning**: If at any point the sum exceeds the target, we backtrack and try different combinations.
4. **Storing Results**: Whenever a valid combination (sum equals target) is found, it will be added to the result list.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, target: int, current_combination: List[int]):
            if target == 0:
                result.append(list(current_combination))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                current_combination.append(candidates[i])
                backtrack(i, target - candidates[i], current_combination)
                current_combination.pop()
        
        backtrack(0, target, [])
        return result

# Example usage
solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
