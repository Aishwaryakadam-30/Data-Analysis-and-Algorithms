# NAME: Aishwarya Kadam
# ID: 1002199035

---

## 🚀 Algorithms Included

### 1. 📦 Bellman-Ford Algorithm (`bellman_ford.py`)
- Computes single-source shortest paths even with **negative edge weights**.
- Detects **negative-weight cycles**.
- Based on CLRS **Figure 24.4**.
- Uses a custom graph structure (`Network`, `Side`, and `Node` classes).

**Output Includes:**
- Whether a negative-weight cycle exists
- Final shortest distances from the source
- Predecessor tracking for path reconstruction

---

### 2. ⚡ Dijkstra’s Algorithm (`dijkstra.py`)
- Computes shortest paths from a single source **when all edge weights are non-negative**.
- Efficient for dense graphs and supports path reconstruction.
- Based on CLRS **Figure 24.6**.

**Output Includes:**
- Shortest distance from source to all nodes
- Actual path taken to reach each node

---

### 3. 🌐 Floyd-Warshall Algorithm (`floyd_warshall.py`)
- Solves the **all-pairs shortest path** problem.
- Works with negative weights (but no negative cycles).
- Includes both **iterative** and **recursive** implementations.
- Based on CLRS **Figure 25.4**.

**Features:**
- Tracks distance matrices for each step
- Generates a **parent matrix** to reconstruct shortest paths

---

## 🧪 Example Graphs

All algorithms use example graphs taken from CLRS:
- Bellman-Ford: Figure 24.4 (5-node graph with negative weights)
- Dijkstra: Figure 24.6 (non-negative edges)
- Floyd-Warshall: Figure 25.4 (with some `∞` distances and negative weights)

---

## 🛠 How to Run

### Python 3 Required

```bash
# Run Bellman-Ford
python bellman_ford.py

# Run Dijkstra’s Algorithm
python dijkstra.py

# Run Floyd-Warshall Algorithm
python floyd_warshall.py

