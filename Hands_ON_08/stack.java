import java.util.Scanner;

public class Stack {

    private final int[] stackArray = new int[10];  // Fixed-size stack with capacity 10
    private int topIndex = -1;                     // Tracks the top element

    // Push method: Adds an element to the stack
    public void push(int value) {
        if (topIndex == stackArray.length - 1) {
            System.out.println("Stack is full! Cannot push.");
        } else {
            stackArray[++topIndex] = value;
            System.out.println(value + " pushed onto the stack.");
        }
    }

    // Pop method: Removes and returns the top element
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty! Cannot pop.");
            return -1;
        } else {
            int removedElement = stackArray[topIndex--];
            System.out.println("Popped: " + removedElement);
            return removedElement;
        }
    }

    // Peek method: Retrieves the top element without removing it
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty. No top element.");
            return -1;
        }
        return stackArray[topIndex];
    }

    // Method to check if the stack is empty
    public boolean isEmpty() {
        return topIndex == -1;
    }

    // Method to get the number of elements in the stack
    public int getSize() {
        return topIndex + 1;
    }

    // Main method to allow user interaction
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack stack = new Stack();
        int userChoice;

        while (true) {
            System.out.println("\nStack Operations:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Check if Empty");
            System.out.println("5. Get Size");
            System.out.println("6. Exit");
            
            System.out.print("Select an option: ");
            userChoice = scanner.nextInt();
            
            switch (userChoice) {
                case 1:
                    System.out.print("Enter value to push: ");
                    int val = scanner.nextInt();
                    stack.push(val);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    int topValue = stack.peek();
                    if (topValue != -1) {
                        System.out.println("Top element: " + topValue);
                    }
                    break;
                case 4:
                    System.out.println(stack.isEmpty() ? "Stack is empty." : "Stack is not empty.");
                    break;
                case 5:
                    System.out.println("Stack size: " + stack.getSize());
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
