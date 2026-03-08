# Queue – Data Structure Practice

This directory contains my implementations and problem solutions related to the **Queue Data Structure**.

A queue follows the **FIFO (First In First Out)** principle — the first element inserted into the queue is the first element removed.

Example flow:

enqueue → 10 → 20 → 30
dequeue → 10

---

# Core Queue Operations

| Operation    | Description                             |
| ------------ | --------------------------------------- |
| Enqueue      | Insert element at the rear of the queue |
| Dequeue      | Remove element from the front           |
| Front / Peek | View the front element                  |
| Empty        | Check if queue is empty                 |

---

# Queue Implementations

This section includes implementations of queues using different approaches.

### 1. Queue using Python List

Basic implementation to understand queue mechanics.

Limitation:

* `pop(0)` takes **O(n)** time due to element shifting.

### 2. Queue using `collections.deque`

Python's optimal queue structure.

Operations:

```python
from collections import deque

q = deque()
q.append(10)      # enqueue
q.popleft()       # dequeue
```

Time Complexity:

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |

---

### 3. Queue using Two Stacks

Classic interview design problem.

Idea:

* Use one stack for **push**
* Use another stack for **pop**

Amortized Complexity:

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |

---

# Queue Patterns in DSA

Queues appear in several algorithmic patterns:

### Breadth First Search (BFS)

Used in graph traversal and tree level-order traversal.

### Sliding Window Problems

Used to maintain elements in a specific window of size **k**.

### Monotonic Queue

Important for problems like **Sliding Window Maximum**.

### Scheduling Systems

Queues are widely used in operating systems and task scheduling.

---


---

# Objective

The goal of this section is to develop strong intuition around **queue-based patterns**, which frequently appear in:

* BFS algorithms
* Sliding window problems
* Real-time streaming systems
* Scheduling and buffering systems


