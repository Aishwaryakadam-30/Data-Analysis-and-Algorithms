# ⚡ Quicksort Complexity Analysis

### 📝 Name: Aishwarya Kadam  
### 🎓 Student ID: `1002199035`  

## 📌 Overview  
Quicksort is an **efficient, divide-and-conquer sorting algorithm** that operates by selecting a pivot element and partitioning the array into smaller and larger elements. The **average-case runtime complexity** for **fixed-pivot Quicksort** is **O(n log n)**.

---

## 🔍 How Quicksort Works  
1️⃣ **Choose a Pivot** – A single element is selected as the reference.  
2️⃣ **Partition the Array** – Elements are rearranged into:
   - **Smaller** than pivot  
   - **Equal** to pivot  
   - **Greater** than pivot  
3️⃣ **Recursively Apply Quicksort** on the partitions until sorting is complete.

---

## 📊 Complexity Analysis  

The recurrence relation for Quicksort is:

T(n) = n + 2T(n/2)


Where:  
- `T(n)`: Time complexity for sorting `n` elements.  
- `n`: Time taken for **partitioning** the array (linear time).  
- `2T(n/2)`: Time taken to recursively sort the two partitions.  

---

## 📊 **Solving the Recurrence Relation**  

Using the **Master Theorem**, the recurrence:
'''
T(n) = n + 2T(n/2)
'''

Thus, the **average runtime complexity** of Quicksort is **O(n log n)**, making it efficient in most cases.

---

## 🏆 **Complexity Summary**  

| Case          | Time Complexity  |
|--------------|----------------|
| **Best Case**   | **O(n log n)**  |
| **Worst Case**  | **O(n²)**       |
| **Average Case**| **O(n log n)**  |

- **Best case:** Occurs when the pivot consistently divides the array into **two equal halves**.  
- **Worst case:** Happens when the pivot always selects the **smallest or largest element**, leading to highly **unbalanced** partitions.  
- **Average case:** Typically maintains **O(n log n)** efficiency across randomized inputs.

---

## 📚 **Conclusion**  

Quicksort is one of the most efficient **comparison-based sorting algorithms**. While the worst-case scenario can degrade to **O(n²)**, selecting an optimal pivot (or using **randomized Quicksort**) helps maintain an **O(n log n)** runtime.  

This makes Quicksort a preferred choice for **large datasets**, where its performance outperforms simpler sorting algorithms like **Bubble Sort** and **Insertion Sort**.

---



