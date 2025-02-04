### Name: Aishwarya Kadam
### Student ID: `1002199035`

## Code

```
function x = f(n)
   x = 1;
   for i = 1:n
       for j = 1:n
           x = x + 1;
```

## Runtime of the Algorithm mathematically

![1]([https://github.com/Aishwaryakadam-30/Data-Analysis-and-Algorithms/blob/main/Hands_On_3/IMG_6954.HEIC])

## Plot time vs n and curve of the polynomial

![time_vs_n](https://github.com/user-attachments/assets/813d9f27-5b12-47ea-84e9-2ee91fa29757)

## Upper Bound and Lower Bound ploynomial curves

![upper_lower_bound](https://github.com/user-attachments/assets/90045542-e17a-4056-b736-8851e838db47)

## Results

### Big-O Notation (O)
The function `f(n)` is \( O(n^2) \) because the runtime grows quadratically with \( n \).

### Big-Omega Notation (Ω)
The function `f(n)` is \( Ω(n^2) \) because the runtime has a lower bound that grows quadratically with \( n \).

### Big-Theta Notation (Θ)
The function `f(n)` is \( Θ(n^2) \) because the runtime grows quadratically with \( n \), and both the upper and lower bounds are \( n^2 \).

## Approx location on n_0

![approx_n0_full](https://github.com/user-attachments/assets/2ae7cd13-62c1-4a1e-92e2-895e7977c26c)

![approx_n0_zoomed](https://github.com/user-attachments/assets/8a5dc853-532c-453c-9e02-70ffec5cf3bb)

This value of 𝑛 is approximately where the function starts behaving quadratically.

## Modified Code

```
x = f(n)
   x = 1;
   y = 1;
   for i = 1:n
        for j = 1:n
             x = x + 1;
             y = i + j;
```

### Time Complexity:
Even though there's an additional operation `y = i + j`, this does not affect the number of iterations of the nested loops.

Each loop still iterates `n × n` times, and the additional operation inside each iteration does not increase the overall time complexity. Hence, the time complexity of the modified function remains `O(n²)`. 
However, the constant factor involved in the execution time might be slightly higher due to the extra computation of y.

## Effect on #1 results

In the original function analysis `(#1)`, the runtime was determined to be `O(n²)` based on the number of iterations in the nested loops.

The additional operation in the modified function does not change this result:
- The time complexity remains O(n²) since the number of iterations remains the same.
- However, the extra computation inside the loop means that the actual runtime will increase slightly, although this is a constant factor and does not affect the asymptotic complexity.
