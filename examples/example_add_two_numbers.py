
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from add_two_numbers import Solution
from structs.ListNode import ListNode

solution = Solution()

# Finance: Adding two numbers represented as linked lists
ts_stock_a = [1, 2, 3]
ts_stock_a  = ListNode().list_to_nodes(ts_stock_a )
ts_stock_b  = [4, 5, 6]
ts_stock_b= ListNode().list_to_nodes(ts_stock_b)
result = solution.add_two_numbers(ts_stock_a, ts_stock_b)
print(ListNode().nodes_to_list(result))

# Data Analysis: Summing two linked lists representing data points
data_points_a = [7, 8, 9]
data_points_a = ListNode().list_to_nodes(data_points_a)
data_points_b = [1, 1, 1]
data_points_b = ListNode().list_to_nodes(data_points_b)
result = solution.add_two_numbers(data_points_a, data_points_b)
print(ListNode().nodes_to_list(result))

# Game Development: Combining resources represented as linked lists
resources_a = [2, 4, 3]
resources_a = ListNode().list_to_nodes(resources_a)
resources_b = [5, 6, 4]
resources_b = ListNode().list_to_nodes(resources_b)
result = solution.add_two_numbers(resources_a, resources_b)
print(ListNode().nodes_to_list(result))

# E-commerce: Adding prices represented as linked lists
prices_a = [9, 8, 8]
prices_a = ListNode().list_to_nodes(prices_a)
prices_b = [1]
prices_b = ListNode().list_to_nodes(prices_b)
result = solution.add_two_numbers(prices_a, prices_b)
print(ListNode().nodes_to_list(result))

# E-commerce: Adding prices represented as linked lists
prices_a = [9, 9, 9]
prices_a = ListNode().list_to_nodes(prices_a)
prices_b = [1]
prices_b = ListNode().list_to_nodes(prices_b)
result = solution.add_two_numbers(prices_a, prices_b)
print(ListNode().nodes_to_list(result))

# E-commerce: Adding prices represented as linked lists
prices_a = [9, 9, 9]
prices_a = ListNode().list_to_nodes(prices_a)
prices_b = [1, 0, 0]
prices_b = ListNode().list_to_nodes(prices_b)
result = solution.add_two_numbers(prices_a, prices_b)
print(ListNode().nodes_to_list(result))

# E-commerce: Adding prices represented as linked lists
prices_a = [9, 9, 9]
prices_a = ListNode().list_to_nodes(prices_a)
prices_b = [0, 0, 1]
prices_b = ListNode().list_to_nodes(prices_b)
result = solution.add_two_numbers(prices_a, prices_b)
print(ListNode().nodes_to_list(result))
