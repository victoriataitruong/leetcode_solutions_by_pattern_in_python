"""
Leetcode 198: House Robber

Problem Description:
You are a robber planning to rob houses along a street. Each house has a certain amount of money stashed, but there are two important rules:
1. You cannot rob two adjacent houses because they will alert the police.
2. You need to maximize the amount of money you can rob.

Given an array of non-negative integers representing the amount of money in each house, return the maximum amount of money you can rob without alerting the police. The solution must be solved in **O(n)** time complexity, where `n` is the number of houses.

Approach:
1. **Dynamic Programming (Optimized)**: Use two variables to track the maximum money we can rob up to the current house, without storing the entire dynamic programming table.
2. **Iterate Through the Houses**: For each house, calculate the maximum money we can rob if we either rob it or skip it.
3. **Return Maximum Money**: At the end of the loop, return the maximum money that can be robbed.

"""

def rob(nums):
    # If there are no houses, return 0 (nothing to rob)
    if not nums:
        return 0

    # If there is only one house, return the amount in that house
    if len(nums) == 1:
        return nums[0]

    # Initialize two variables to track the maximum money we can rob
    # 'prev2' keeps track of the maximum money we can rob up to two houses ago
    # 'prev1' keeps track of the maximum money we can rob up to the previous house
    prev2, prev1 = 0, 0

    # Loop through each house in the list
    for num in nums:
        # For the current house, decide whether to rob it or skip it
        # If we rob the current house, we add its money to the max amount we could have robbed two houses ago
        # If we skip the current house, we carry forward the max amount from the previous house
        curr = max(prev1, prev2 + num)

        # Update prev2 and prev1 for the next iteration
        prev2 = prev1
        prev1 = curr

    # After the loop, prev1 will contain the maximum money that can be robbed
    return prev1
