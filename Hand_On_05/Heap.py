from typing import TypeVar, Generic, List

T = TypeVar('T')

class MinHeap(Generic[T]):
    
    def __init__(self, elements: List[T]) -> None:
        self.data = elements
        self.construct_min_heap()
    
    def insert(self, value: T):
        self.data.append(value)
        current = len(self.data) - 1
        parent = (current - 1) // 2
        
        while current > 0 and self.data[current] < self.data[parent]:
            self.data[current], self.data[parent] = self.data[parent], self.data[current]
            current = parent
            parent = (current - 1) // 2

    def heapify_down(self, size: int, index: int):
        smallest = index
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2

        if left_child < size and self.data[left_child] < self.data[smallest]:
            smallest = left_child

        if right_child < size and self.data[right_child] < self.data[smallest]:
            smallest = right_child

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(size, smallest)

    def construct_min_heap(self):
        size = len(self.data)
        for i in range(size // 2 - 1, -1, -1):
            self.heapify_down(size, i)
    
    def get_min(self) -> T:
        return self.data[0] if self.data else None
    
    def remove_min(self) -> T:
        if not self.data:
            return None
        
        self.data[0] = self.data[-1]
        self.data.pop()
        self.heapify_down(len(self.data), 0)
        
    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    
    test_cases = [
        [50, 20, 30, 10, 15, 5, 25],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [5.6, 2.3, 9.8, 7.1, 1.2, 4.5, 8.9],
        [50, 20, 30, 10, 15, 5, 25, 70, 65, 60, 55, 85, 90, 40, 35, 100, 45, 80, 95, 75],
        [],
    ]
    
    for case in test_cases:
        heap = MinHeap(case)
        print("Min Heap:", heap)
    
    print("\nInserting into Heap:")
    heap = MinHeap([5, 10, 25, 20, 15, 30, 50])
    heap.insert(2)
    print("After inserting 2:", heap)
    heap.insert(8)
    print("After inserting 8:", heap)
    
    print("\nGetting Root:")
    heap = MinHeap([9, 4, 7, 1, 3, 2, 6])
    print("Heap:", heap)
    print("Root Element:", heap.get_min())
    
    print("\nRemoving Root:")
    heap.remove_min()
    print("Heap after removing root:", heap)
