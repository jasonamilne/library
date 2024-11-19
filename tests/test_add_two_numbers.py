import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from add_two_numbers import Solution
from structs.ListNode import ListNode

import pytest

@pytest.fixture
def solution():
    return Solution()

# Test cases: test functionality
def test_add_two_numbers(solution):
    l1, l2 = [2,4,3], [5,6,4]
    l1, l2 = ListNode().list_to_nodes(l1), ListNode().list_to_nodes(l2)
    l2 = ListNode().list_to_nodes(l2)
    result = solution.add_two_numbers(l1, l2)
    assert ListNode().nodes_to_list(result) == [7, 0, 8]

# Test cases: Basic functionality
def test_add_two_numbers(solution):
    l1, l2 = [0], [0]
    l1, l2 = ListNode().list_to_nodes(l1), ListNode().list_to_nodes(l2)
    result = solution.add_two_numbers(l1, l2)
    assert ListNode().nodes_to_list(result) == [0]

# Test cases: Basic functionality
def test_additional_tests(solution):
    l1, l2 = [9,9,9,9,9,9,9], [9,9,9,9]
    l1, l2 = ListNode().list_to_nodes(l1), ListNode().list_to_nodes(l2)
    result = solution.add_two_numbers(l1, l2)
    assert ListNode().nodes_to_list(result) == [8,9,9,9,0,0,0,1]

# Test cases: test input error cases
def test_data_types(solution):
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        l1 = ListNode().list_to_nodes(['a', 4, 3])
        l2 = ListNode().list_to_nodes([5, 6, 4])
        solution.add_two_numbers(l1, l2)

    with pytest.raises(ValueError, match="Input must be a list of integers"):
        l1 = ListNode().list_to_nodes([2, 4, 3])
        l2 = ListNode().list_to_nodes(['a', 6, 4])
        solution.add_two_numbers(l1, l2)

    with pytest.raises(ValueError, match="Input must be a list of integers"):
        l1 = ListNode().list_to_nodes(['b', 4, 3])
        l2 = ListNode().list_to_nodes([5, 6, 'a'])
        solution.add_two_numbers(l1, l2)
