#include <iostream>
#include <cmath>

struct Node {
    int key;
    int value;
    Node* next;
    Node* prev;
    Node(int k, int v) : key(k), value(v), next(nullptr), prev(nullptr) {}
};

// HashTable class
class HashTable {
private:
    Node** table;
    int cap;
    int size;
    const float lft = 0.75f; 
    const float sft = 0.25f;

    int hash(int key, int capacity) {
        const float mcons = 0.6180339887f;
        float fp = (key * mcons) - floor(key * mcons);
        return floor(capacity * fp);
    }

    void resize(int new_capacity) {
        Node** obj = new Node*[new_capacity]();
        for (int i = 0; i < new_capacity; ++i) {
            obj[i] = nullptr;
        }
        int old_capacity = cap;
        cap = new_capacity;
        
        for (int i = 0; i < old_capacity; ++i) {
            Node* crr = table[i];
            while (crr != nullptr) {
                Node* temp = crr->next;
                int h = hash(crr->key, new_capacity);
                crr->next = obj[h];
                if (obj[h] != nullptr)
                    obj[h]->prev = crr;
                obj[h] = crr;
                crr->prev = nullptr;
                crr = temp;
            }
        }
        delete[] table;
        table = obj;
    }

public:
    HashTable() : cap(8), size(0) {
        table = new Node*[cap]();
    }

    ~HashTable() {
        for (int i = 0; i < cap; ++i) {
            Node* crr = table[i];
            while (crr != nullptr) {
                Node* temp = crr->next;
                delete crr;
                crr = temp;
            }
        }
        delete[] table;
    }

    void insert(int key, int value) {
        int h = hash(key, cap);
        Node* crr = table[h];
        
        while (crr != nullptr) {
            if (crr->key == key) { 
                crr->value = value;
                return;
            }
            crr = crr->next;
        }

        Node* newNode = new Node(key, value);
        if (table[h] != nullptr) {
            newNode->next = table[h];
            table[h]->prev = newNode;
        }
        table[h] = newNode;
        size++;

        if (size >= lft * cap)
            resize(2 * cap);
    }

    void remove(int key) {
        int h = hash(key, cap);
        Node* crr = table[h];
        while (crr != nullptr) {
            if (crr->key == key) {
                if (crr->prev != nullptr)
                    crr->prev->next = crr->next;
                else
                    table[h] = crr->next;
                if (crr->next != nullptr)
                    crr->next->prev = crr->prev;
                delete crr;
                size--;
                break;
            }
            crr = crr->next;
        }

        // Resize if shrink factor exceeds threshold
        if (size <= sft * cap && cap > 8)
            resize(cap / 2);
    }

    int search(int key) {
        int h = hash(key, cap);
        Node* crr = table[h];
        while (crr != nullptr) {
            if (crr->key == key)
                return crr->value;
            crr = crr->next;
        }
        return -1;
    }
};

int main() {
    HashTable hash_table;
    hash_table.insert(5, 10);
    hash_table.insert(15, 20);
    hash_table.insert(25, 30);
    
    std::cout << "Value for key 5: " << hash_table.search(5) << std::endl;
    std::cout << "Value for key 15: " << hash_table.search(15) << std::endl;
    std::cout << "Value for key 25: " << hash_table.search(25) << std::endl;

    hash_table.remove(15);

    std::cout << "Value for key 15 after removal: " << hash_table.search(15) << std::endl;

     return 0;
}