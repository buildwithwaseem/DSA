# Data Structures & Algorithms (DSA) Journey

Welcome to my personal Data Structures and Algorithms repository! This space serves as a daily tracker for my coding consistency, architectural deep dives, and problem-solving journey. Here, I document data structures implementations, theoretical concepts, and algorithms implemented in Python.

---

## Repository Structure

The repository is organized by core computer science concepts. It contains a mix of optimized production-ready Python scripts (`.py`) and exploratory Jupyter Notebooks (`.ipynb`) for step-by-step verification.

| Category | File Name | Format | Key Concepts Covered |
| :--- | :--- | :--- | :--- |
| **Queues** | `Queue.ipynb` | Jupyter Notebook | FIFO Principle, Linear Queue Implementation, Edge Cases |
| **Queues** | `Circular_Queue.ipynb` | Jupyter Notebook | Modulo Arithmetic (`%`), Memory Optimization, Circular Buffers |
| **Queues** | `Deque.ipynb` | Jupyter Notebook | Double-Ended Queue, Unrestricted Enqueue/Dequeue |
| **Recursion**| `Recursion.ipynb` | Jupyter Notebook | Base Cases, Call Stacks, Iterative vs Recursive Trade-offs |
| **Trees** | `tree_traversal.py` | Python Script | Binary Tree Nodes, Depth-First Search (DFS) Traversal |

---

## Core Concepts Documented

### 1. Advanced Queue Configurations
Implemented linear, circular, and double-ended queues to deeply understand memory allocation and element shift optimizations.
* **Linear Queue:** Standard First-In-First-Out (FIFO) data structure utilizing dynamic arrays.
* **Circular Queue:** Solved the limitation of memory wastage in static linear queues using front/rear pointers and pointer wrapping via:
    $$\text{rear} = (\text{rear} + 1) \pmod{\text{size}}$$
* **Deque (Double-Ended Queue):** Complete flexibility to insert and delete elements from both the `Front` and `Rear` boundaries.

### 2. Recursion & Mathematical Formulations
Explored call-stack mechanisms and mathematical inductive reasoning by converting iterative business-logic into elegant recursive flows.
* **Factorial Calculations:** Tracking function states using localized stack allocations.
* **Fibonacci Series:** Recursion tree analysis showcasing overlapping subproblems and state dependencies.

### 3. Tree Structures & Traversal Algorithms
Designed custom structural pointers to represent Hierarchical Structures. Built robust depth-first search strategies to navigate binary tree layers effectively:
* **Pre-Order Traversal:** $\text{Root} \rightarrow \text{Left} \rightarrow \text{Right}$
* **In-Order Traversal:** $\text{Left} \rightarrow \text{Root} \rightarrow \text{Right}$
* **Post-Order Traversal:** $\text{Left} \rightarrow \text{Right} \rightarrow \text{Root}$

---

## Technical Environment & Stack
* **Language:** Python 3.x
* **Environments:** Google Colab / Jupyter Notebooks (`.ipynb`), Local Python Core Scripts (`.py`)
* **Core Concepts:** Object-Oriented Programming (OOP), Custom Pointer Logic, Time & Space Complexity Optimization

---

## Continuous Improvement Log
- [x] Master Linear and Circular Queue memory management.
- [x] Implement complete Tree Traversals (Pre, In, Post Order).
- [x] Analyze recursive vs iterative performance costs.
- [ ] Implement Graph Data Structures and Search Algorithms (BFS/DFS).
- [ ] Deep dive into Dynamic Programming to optimize overlapping recursive calls.

---
*“Consistency beats talent when talent doesn’t work hard.” Happy Coding!*
