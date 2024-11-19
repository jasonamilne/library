from typing import List

class Solution:
    def two_sum(self,nums: List[int], target: int) -> List[int]:
        """
        @Description:

        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        @Pseudocode:
        - - Check if the input is valid: (list of integers, all entries are integers, list length > 2 and target is an integer).
        - Create an empty dictionary to store the numbers and their indices.
        - Iterate through the list of numbers.
        - Calculate the complement of the current number with respect to the target.
        - Check if the complement is already in the dictionary.
        - If the complement is found, return the indices of the complement and the current number.
        - If the complement is not found, add the current number to the dictionary with its index.
        - If no solution is found, return None.

        @Applications:

        1. Algorithmic Challenges: Commonly used in coding interviews and competitive programming to test problem-solving skills.
        2. Financial Analysis: Finding pairs of transactions that sum to a specific value, such as detecting fraudulent activities.
        3. Data Analysis: Identifying pairs of data points that meet a specific criterion, such as finding pairs of products whose prices sum to a target value.
        4. Game Development: Matching pairs of game elements that meet certain conditions, such as combining resources or items.
        5. E-commerce: Recommending product pairs that together meet a customer's budget.

        @Complexity:
        - Time: O(n)
        - Space: O(n)
        - Algorithm: Hash Table
        
        @Contraints:
        - 2 <= nums.length <= 10^4
        - -10^9 <= nums[i] <= 10^9
        - -10^9 <= target <= 10^9

        @Params:
        - nums: List[int]
        - target: int

        @Returns: 
        - List[int]

        @Example:
        >>> nums = [2,7,11,15]
        >>> target = 9
        >>> two_sum(nums, target)
        [0,1]
        """

        # - Check if the input is valid: (list of integers, all entries are integers, list length > 2 and target is an integer).
        if type(nums) != list or not all(isinstance(x, int) for x in nums) or type(target) != int or len(nums) < 2:
            raise ValueError("Input must be a list of integers")
        # - Create an empty dictionary to store the numbers and their indices.
        num_to_index = {}
        # - Iterate through the list of numbers.
        for index, num in enumerate(nums):
            # - Calculate the complement of the current number with respect to the target.
            complement = target - num
            # - Check if the complement is already in the dictionary.
            if complement in num_to_index:
                # - If the complement is found, return the indices of the complement and the current number.
                return [num_to_index[complement], index]
             # - If the complement is not found, add the current number to the dictionary with its index.
            num_to_index[num] = index
        # - If no solution is found, return None.
        return None
        
def main():
    nums = [2,7,11,15]
    target = 9
    print(Solution().two_sum(nums, target))

if __name__ == "__main__":
    main()
