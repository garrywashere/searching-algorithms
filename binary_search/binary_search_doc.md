# Binary Search

## Objective
The objective of this binary search algorithm is to efficiently find the index of a given item in a sorted array. The algorithm follows a divide-and-conquer approach, narrowing down the search space by half in each iteration.

## Steps

### 1. Initialization
- Set `low` to the first index of the array (0) and `high` to the last index (len(array) - 1).
- This defines the initial search scope from the lowest to the highest value in the array.

### 2. Enter the Loop
- Start a loop that continues as long as `low` is less than or equal to `high`.
- If `low` is greater than `high`, the search space is empty, and the loop exits.

### 3. Calculate the Middle
- Find the middle index of the current search scope using the formula `mid = (low + high) // 2`.

### 4. Compare with the Middle Value
- Retrieve the value at the middle index (`mid_value = array[mid]`).
- Compare `mid_value` with the target `item`.
  - If they are equal, the item is found, and the function returns the index (`return mid`).
  - If `mid_value` is less than the target, discard the left half by updating `low = mid + 1`.
  - If `mid_value` is greater than the target, discard the right half by updating `high = mid - 1`.

### 5. Repeat
- Repeat steps 3-4 until the target item is found or the search space is empty.

### 6. Exit Loop
- If the loop exits without finding the item, return -1 to indicate that the item is not present in the array.

## Example
Suppose we have a sorted array `arr = [2, 5, 8, 12, 16, 23, 38, 42, 50]` and we want to find the index of the item `23`.

- Initial `low = 0`, `high = 8`.
- First iteration:
  - `mid = (0 + 8) // 2 = 4`, `mid_value = arr[4] = 16`.
  - Since `16` is less than `23`, update `low = 5`.
- Second iteration:
  - `mid = (5 + 8) // 2 = 6`, `mid_value = arr[6] = 38`.
  - Since `38` is greater than `23`, update `high = 5`.
- Third iteration:
  - `mid = (5 + 5) // 2 = 5`, `mid_value = arr[5] = 23`.
  - The target item `23` is found, and the function returns the index `5`.