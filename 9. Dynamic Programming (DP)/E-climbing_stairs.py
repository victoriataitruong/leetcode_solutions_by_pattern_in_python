"""
Leetcode 70: Climbing Stairs

Problem Description:
Given an integer `n` representing the total number of steps in a staircase, you can climb either 1 or 2 steps at a time.
Your task is to return the number of distinct ways to reach the top. The solution must be solved in **O(n)** time complexity, where `n` is the number of steps.

Problem Type: Dynamic Programming

Approach:
1. **Base Cases**: If there are 0 or 1 steps, there's only one way to reach the top.
2. **Dynamic Programming**: Use two variables to keep track of the number of ways to reach the last two steps.
   For each step, the number of ways to reach it is the sum of the previous two steps.
3. **Iterate Through the Steps**: Starting from step 2, iteratively calculate the number of ways to reach each step based on the previous two steps.
4. **Return the Result**: After iterating through the steps, the result will be stored in the variable for the last step.

Example: n = 4
ways to reach step 4 = ways to step 3 + ways to step 2
We initialize steps 0 and 1 to 1, then start calculating from step 2.

i       current (ways to step i)       prev2 (ways to step i-2)    prev1 (ways to step i-1)
2       2                               1                           2
3       3                               2                           3
4       5                               3                           5

Return 5

Time Complexity: O(n)
Space Complexity: O(1)
"""

def climbStairs(n):
    if n == 0 or n == 1:
        return 1

    prev2 = 1
    prev1 = 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

# Example usage:
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
print(climbStairs(4))  # Output: 5
