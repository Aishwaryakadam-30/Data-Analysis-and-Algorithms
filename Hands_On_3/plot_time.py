import time
import matplotlib.pyplot as plt

# Function to analyze
def calculate_operations(size):
    count = 1
    for row in range(1, size + 1):
        for column in range(1, size + 1):
            count += 1
    return count

def compute_execution_time(size):
    start = time.time()
    calculate_operations(size)
    end = time.time()
    return end - start

if __name__ == "__main__":
    input_sizes = list(range(1, 1000))
    execution_times = [compute_execution_time(n) for n in input_sizes]
    
    # Plot input size vs execution time
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, execution_times, label='Measured Execution Time')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Input Size')
    plt.legend()
    plt.grid(True)
    plt.show()

 # Ensure plot displays correctly
    plt.show(block=True)
    
    print("Script executed successfully! Plot displayed.")
