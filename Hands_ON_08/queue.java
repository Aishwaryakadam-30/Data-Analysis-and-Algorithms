import java.util.Scanner;

class Queue {

    private int[] queueArray = new int[10];  // Fixed-size queue with capacity 10
    private int frontIndex = -1;             // Front pointer
    private int rearIndex = -1;              // Rear pointer

    // Method to add an element to the queue
    public void enqueue(int value) {
        if (rearIndex == queueArray.length - 1) {
            System.out.println("Queue is full! Cannot enqueue.");
        } else {
            if (frontIndex == -1) {
                frontIndex = 0;
            }
            queueArray[++rearIndex] = value;
            System.out.println(value + " added to the queue.");
        }
    }

    // Method to remove and return the front element
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty! Cannot dequeue.");
            return -1;
        } else {
            int removedElement = queueArray[frontIndex];
            if (frontIndex == rearIndex) {
                frontIndex = rearIndex = -1;
            } else {
                frontIndex++;
            }
            System.out.println("Removed: " + removedElement);
            return removedElement;
        }
    }

    // Method to retrieve the front element without removing it
    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty. No front element.");
            return -1;
        }
        return queueArray[frontIndex];
    }

    // Method to check if the queue is empty
    public boolean isEmpty() {
        return frontIndex == -1;
    }

    // Method to get the number of elements in the queue
    public int getSize() {
        return isEmpty() ? 0 : (rearIndex - frontIndex + 1);
    }

    // Main method for user interaction
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue queue = new Queue();
        int userChoice;

        while (true) {
            System.out.println("\nQueue Operations:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Check if Empty");
            System.out.println("5. Get Size");
            System.out.println("6. Exit");
            
            System.out.print("Select an option: ");
            userChoice = scanner.nextInt();
            
            switch (userChoice) {
                case 1:
                    System.out.print("Enter value to enqueue: ");
                    int val = scanner.nextInt();
                    queue.enqueue(val);
                    break;
                case 2:
                    queue.dequeue();
                    break;
                case 3:
                    int frontValue = queue.peek();
                    if (frontValue != -1) {
                        System.out.println("Front element: " + frontValue);
                    }
                    break;
                case 4:
                    System.out.println(queue.isEmpty() ? "Queue is empty." : "Queue is not empty.");
                    break;
                case 5:
                    System.out.println("Queue size: " + queue.getSize());
                    break;
                case 6:
                    System.out.println("Exiting program...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid input! Please enter a valid option.");
            }
        }
    }
}
