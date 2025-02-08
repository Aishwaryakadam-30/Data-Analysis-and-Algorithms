### Name: Aishwarya Kadam
### Student ID: `1002199035`

## Step-by-Step Breakdown of Recursive Calls for `fibonacci(5)`:

- The function `fibonacci(5)` initiates calls to `fibonacci(4)` and `fibonacci(3)`.
- `fibonacci(4)` then calls `fibonacci(3)` and `fibonacci(2)`.
- `fibonacci(3)` proceeds with calls to `fibonacci(2)` and `fibonacci(1)`.
- `fibonacci(2)` invokes `fibonacci(1)` and `fibonacci(0)`, which return `1` and `0`, respectively.
- The result of `fibonacci(2)` is computed as `1 + 0 = 1`.
- Moving back, `fibonacci(3)` sums up `fibonacci(2) (1)` and `fibonacci(1) (1)`, yielding `2`.
- At `fibonacci(4)`, the previously computed `fibonacci(3) (2)` is added to `fibonacci(2) (1)`, resulting in `3`.
- Finally, at `fibonacci(5)`, the values from `fibonacci(4) (3)` and `fibonacci(3) (2)` sum up to `5`.

### (A more in-depth explanation of the function call stack is available in the `fibonacci.py` file)

## Time Complexity of the Recursive Fibonacci Function

The time complexity of this recursive Fibonacci approach is `O(2^n)`, which is exponential.

### Why is it Exponential?
#### Repeated Function Calls:
- Each `fibonacci(n)` call results in two recursive calls: `fibonacci(n-1)` and `fibonacci(n-2)`, forming a binary tree of calls.

#### Redundant Calculations:
- Many Fibonacci numbers are recomputed multiple times. For instance, `fibonacci(2)` and `fibonacci(1)` appear in multiple branches of the recursion tree.
- Due to this duplication, the number of recursive calls increases exponentially, leading to `O(2^n)` complexity.

## Optimized Approaches to Improve Fibonacci Computation

### 1. Memoization (Top-Down Approach):
- By storing previously computed values in a dictionary or list, we avoid redundant computations.
- This reduces the time complexity to `O(n)`, as retrieving stored values is `O(1)`.

### 2. Dynamic Programming (Bottom-Up Approach):
- Instead of recursion, we store Fibonacci values in an array and compute results iteratively up to `n`.
- This approach also runs in `O(n)` time complexity but eliminates the overhead of recursive function calls.

These optimizations make Fibonacci calculations significantly more efficient, especially for large values of `n`.

