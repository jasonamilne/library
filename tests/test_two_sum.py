
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from two_sum import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_two_sum(solution):
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1] # i = 0, j = 0:1
    assert solution.two_sum([3, 2, 4], 6) == [1, 2] # i = 1, j = 0:2
    assert solution.two_sum([3, 3], 6) == [0, 1] # i = 0, j = 0:1
    assert solution.two_sum([1,2,3,4,5,6,7,8,9,10], 19) == [8, 9] # i = 8, j = 9

def test_input_error_cases(solution):
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        solution.two_sum(['a', 2, 3, 4, 5, 6, 7, 8, 9, 10], 19)
    
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        solution.two_sum([2, 3, 4, 5, 6, 7, 8, 9, 10], 'a')

    with pytest.raises(ValueError, match="Input must be a list of integers"):
        solution.two_sum([2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3])

    with pytest.raises(ValueError, match="Input must be a list of integers"):
        solution.two_sum([], 1)

    with pytest.raises(ValueError, match="Input must be a list of integers"):
        solution.two_sum([1], 1)

def test_time_complexity(solution):
    import time
    import random

    def generate_large_input(size):
        return [random.randint(1, 1000000) for _ in range(size)]

    sizes = [1000, 2000, 4000, 8000]
    times = []

    for size in sizes:
        nums = generate_large_input(size)
        target = nums[0] + nums[-1]  # Ensure worst-case scenario
        
        start_time = time.time()
        solution.two_sum(nums, target)
        end_time = time.time()
        
        times.append(end_time - start_time)

    # Check if time complexity is quadratic (O(n^2))
    ratios = [times[i+1]/times[i] for i in range(len(times)-1)]
    average_ratio = sum(ratios) / len(ratios)

    # If the average ratio is close to 4, it suggests quadratic time complexity
    assert average_ratio < 4.5, f"Expected quadratic time complexity, but got ratio: {average_ratio}"
