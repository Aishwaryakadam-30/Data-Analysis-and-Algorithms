import java.util.Scanner;

// Node structure for the linked list
class Node {
    int value;
    Node next;

    Node(int value) {
        this.value = value;
        this.next = null;
    }
}

// LinkedList class with fundamental operations
class LinkedList {
    private Node head;

    // Add a node at the start of the list
    public void addAtStart(int value) {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
        System.out.println(value + " inserted at the start.");
    }

    // Append a node to the end of the list
    public void addAtEnd(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
        System.out.println(value + " inserted at the end.");
    }

    // Remove a node containing a specific value
    public void removeNode(int value) {
        Node temp = head, prev = null;

        if (temp != null && temp.value == value) {
            head = temp.next;
            System.out.println(value + " removed from the list.");
            return;
        }

        while (temp != null && temp.value != value) {
            prev = temp;
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println(value + " not found in the list.");
            return;
        }

        prev.next = temp.next;
        System.out.println(value + " removed from the list.");
    }

    // Search for an element in the list
    public boolean find(int value) {
        Node temp = head;
        while (temp != null) {
            if (temp.value == value) {
                return true;
            }
            temp = temp.next;
        }
        return false;
    }

    // Display the elements in the list
    public void showList() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }
        Node temp = head;
        System.out.print("Linked List: ");
        while (temp != null) {
            System.out.print(temp.value + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }

    // Main method to execute linked list operations
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LinkedList list = new LinkedList();
        int choice;

        while (true) {
            System.out.println("\nLinked List Operations:");
            System.out.println("1. Insert at start");
            System.out.println("2. Insert at end");
            System.out.println("3. Delete an element");
            System.out.println("4. Search for an element");
            System.out.println("5. Display the list");
            System.out.println("6. Exit");
            
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter value to insert at start: ");
                    int val1 = scanner.nextInt();
                    list.addAtStart(val1);
                    break;
                case 2:
                    System.out.print("Enter value to insert at end: ");
                    int val2 = scanner.nextInt();
                    list.addAtEnd(val2);
                    break;
                case 3:
                    System.out.print("Enter value to delete: ");
                    int delVal = scanner.nextInt();
                    list.removeNode(delVal);
                    break;
                case 4:
                    System.out.print("Enter value to search: ");
                    int searchVal = scanner.nextInt();
                    if (list.find(searchVal)) {
                        System.out.println(searchVal + " exists in the list.");
                    } else {
                        System.out.println(searchVal + " not found.");
                    }
                    break;
                case 5:
                    list.showList();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice! Please select a valid option.");
            }
        }
    }
}
