
from max_subarray.algorithms.divide_conquer import (
    divide_and_conquer_max_subarray,
)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = divide_and_conquer_max_subarray(arr)

print("Algorithm:", result.algorithm)
print("Start Index:", result.start_index)
print("End Index:", result.end_index)
print("Maximum Sum:", result.max_sum)
print("Time Complexity:", result.time_complexity)
print("Space Complexity:", result.space_complexity)