"""
Leetcode 347: Top K Frequent Elements

Problem Description:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. 
You may return the answer in any order. The solution must run in **O(n)** time complexity, 
where `n` is the number of elements in the array.

Approach:
1. **Hash Map for Frequency Count**: Create a dictionary to count the frequency of each element in `nums`.
2. **Bucket Sort**: Use an array where the index represents frequency, and each entry stores the elements with that frequency.
3. **Build the Result**: Iterate through the bucket array from highest frequency to lowest, appending elements to the result list until it reaches `k` elements.
"""
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Frequency map
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Bucket sort (index represents frequency)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Collect top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # from high freq to low
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

#EXAMPLE USAGE:
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(solution.topKFrequent([1], 1))            # Output: [1]

