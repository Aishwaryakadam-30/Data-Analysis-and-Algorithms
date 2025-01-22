
**Author:** Aishwarya Kadam  
**ID:** 1002199035  

# Selection Sort Algorithm: Proof of Correctness


## Selection Sort Algorithm

### Description

1. Traverse the array from the beginning to the end.  
2. identify the smallest element within the unsorted portion at each position.  
3. Swap the identified smallest element with the element at the current position.  
4. Repeat this process until the entire array is sorted.  

## Proof of Correctness

To establish the correctness of Selection Sort, we will validate the following aspects:  

### 1. Partial Correctness  

- **Base Case:**  
  Initially, the sorted section is empty, which is inherently considered sorted.  

- **Inductive Step:**  
  Assume that after the \( k \)-th iteration, the first \( k \) elements are sorted, while the remaining elements remain unsorted.  

- **Finding the Minimum:**  
  In the \( k \)-th iteration, the smallest element from the unsorted portion (index \( k \) to \( n-1 \)) is located and placed at position \( k \). This guarantees that the first \( k+1 \) elements are sorted.  

- **Swapping:**  
  Exchanging the smallest element with the element at position \( k \) preserves the sorted order of the initial \( k \) elements.  

- **Conclusion:**  
  After completing \( n-1 \) iterations, the entire array is sorted.  

### 2. Termination  

- **Number of Iterations:**  
  The algorithm executes \( n-1 \) iterations, where \( n \) represents the number of elements.  

- **Loop Behavior:**  
  Each iteration reduces the unsorted segment by one element until the entire array is processed.  

- **Termination:**  
  Once \( n-1 \) iterations are completed, the array is fully sorted, and the algorithm concludes.  

## Conclusion  

Selection Sort is proven to be correct based on the following factors:  

- **Partial Correctness:**  
  The sorted section progressively expands with each iteration, ensuring the array is completely sorted after \( n-1 \) steps.  

- **Termination:**  
  The algorithm finishes within a defined number of iterations, leading to a fully sorted array.  

Thus, **Selection Sort** is a correct and complete sorting algorithm.
