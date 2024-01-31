# Linear Search Step-by-Step Explanation

## Objective
The objective of the linear search algorithm is to find the index of a given item in an array by sequentially checking each element until a match is found.

## Steps

### 1. Initialization
- Set an index variable `current_index` to the first index of the array (0).
- This defines the initial position to start the search.

### 2. Enter the Loop
- Start a loop that continues until the end of the array is reached or the target item is found.

### 3. Compare with the Current Element
- Retrieve the value at the current index (`current_value = array[current_index]`).
- Compare `current_value` with the target `item`.
  - If they are equal, the item is found, and the function returns the current index (`return current_index`).

### 4. Move to the Next Element
- Increment `current_index` to move to the next element in the array.

### 5. Repeat
- Repeat steps 3-4 until the end of the array is reached or the target item is found.

### 6. Exit Loop
- If the loop exits without finding the item, return -1 to indicate that the item is not present in the array.

## Example
Suppose we have an array `arr = [12, 8, 5, 23, 16, 38, 2, 50, 42]` and we want to find the index of the item `23`.

- Initial `current_index = 0`.
- First iteration:
  - `current_value = arr[0] = 12`.
  - Since `12` is not equal to `23`, increment `current_index` to 1.
- Second iteration:
  - `current_value = arr[1] = 8`.
  - Since `8` is not equal to `23`, increment `current_index` to 2.
- Third iteration:
  - `current_value = arr[2] = 5`.
  - Since `5` is not equal to `23`, increment `current_index` to 3.
- Fourth iteration:
  - `current_value = arr[3] = 23`.
  - The target item `23` is found, and the function returns the index `3`.