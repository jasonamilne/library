
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from two_sum import Solution
solution = Solution()

"""
Financial analysis:
Given a porfolio of n = 4 assets, we have a budget of 500 to purchase two assets that sum to the target amount.
Find the indices of the two assets that meet the target amount.
"""
transactions = [100, 200, 300, 400]
target_amount = 500
problem = solution.two_sum(transactions, target_amount)
print(problem)

"""
Data analysis:
Given a dataset of n = 4 data points, we have a target value of 50.
Find the indices of the two data points that sum to the target value.
"""
data_points = [10, 20, 30, 40]
target_value = 50
problem = solution.two_sum(data_points, target_value)
print(problem)

"""
Game development
Given a list of n = 4 resources, we have a target combination of 25.
Find the indices of the two resources that sum to the target combination.
"""
resources = [5, 10, 156, 20]
target_combination = 25
print(solution.two_sum(resources, target_combination))

"""
E-commerce
Given a list of n = 4 product prices, we have a budget of 175.
Find the indices of the two products that sum to the budget amount.
"""
prices = [50, 75, 110, 125]
budget = 175
print(solution.two_sum(prices, budget))
