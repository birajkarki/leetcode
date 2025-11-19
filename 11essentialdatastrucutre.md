# ✅ Essential Data Structures 11 — Cheat Sheet

# ✅ 1. Array / List

**What it is**  
Ordered collection of items accessed by index.

**Real-world analogy**  
A row of numbered mailboxes.

**When to use**  
- Two pointers  
- Sliding window  
- Sorting & searching  
- Storing sequences of data

**Example**  
List of student marks → `[92, 85, 77]`

**Python code**  
```python
arr = [1, 2, 3, 4]
print(arr[0])      # 1 (O(1) access)
arr.append(5)      # Add to end
arr[2] = 10        # Update by index
```

---

# ✅ 2. Set

**What it is**  
Unordered collection of unique items with O(1) lookup.

**Real-world analogy**  
A guest list with no duplicate names.

**When to use**  
- Fast membership testing  
- Removing duplicates  
- Tracking seen elements

**Example**  
Detect duplicate numbers in a stream.

**Python code**  
```python
seen = set()
seen.add(3)
print(3 in seen)   # True (O(1))
```

---

# ✅ 3. Dictionary (HashMap)

**What it is**  
Key → value mapping with average O(1) operations.

**Real-world analogy**  
Phone book (name → number).

**When to use**  
- Frequency counting  
- Caching / memoization  
- Fast lookups by key

**Example**  
Count characters in "hello".

**Python code**  
```python
freq = {}
for c in "hello":
    freq[c] = freq.get(c, 0) + 1
print(freq)   # {'h':1, 'e':1, 'l':2, 'o':1}
```

---

# ✅ 4. Tuple

**What it is**  
Immutable ordered collection (hashable → can be used as dict/set keys).

**Real-world analogy**  
GPS coordinates (latitude, longitude) that never change.

**When to use**  
- Grid coordinates (row, col)  
- Returning multiple values from functions  
- Keys in dictionaries or sets

**Example**  
Position in a 2D grid.

**Python code**  
```python
pos = (2, 3)
visited = set()
visited.add(pos)   # Works because tuple is hashable
```

---

# ✅ 5. Stack

**What it is**  
LIFO — Last In, First Out.

**Real-world analogy**  
Stack of plates in a cafeteria.

**When to use**  
- Parentheses matching  
- Depth-First Search (DFS)  
- Backtracking / undo operations

**Example**  
Reverse a string.

**Python code**  
```python
stack = []
stack.append('a')
stack.append('b')
print(stack.pop())   # 'b'
```

---

# ✅ 6. Queue

**What it is**  
FIFO — First In, First Out.

**Real-world analogy**  
People waiting in line at a counter.

**When to use**  
- Breadth-First Search (BFS)  
- Level-order traversal  
- Task scheduling / processing

**Example**  
Processing tasks in arrival order.

**Python code**  
```python
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q.popleft())   # 1
```

---

# ✅ 7. Deque (Double-Ended Queue)

**What it is**  
Efficient append/pop from both ends.

**Real-world analogy**  
A train where cars can be added/removed from front or back.

**When to use**  
- Sliding window maximum/minimum  
- Palindrome checking with two pointers  
- Optimized BFS or any dual-end operations

**Example**  
Maintain recent k elements.

**Python code**  
```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
d.pop()       # removes 4
d.popleft()   # removes 0
```

---

# ✅ 8. Heap / Priority Queue

**What it is**  
Complete binary tree keeping smallest (min-heap) or largest (max-heap) at root.

**Real-world analogy**  
Emergency room triage — most urgent patient next.

**When to use**  
- Top K frequent/largest/smallest elements  
- Dijkstra’s / Prim’s algorithms  
- Scheduling by priority

**Example**  
Always get the smallest element fast.

**Python code**  
```python
import heapq
h = [5, 1, 8, 3]
heapq.heapify(h)
print(heapq.heappop(h))   # 1
heapq.heappush(h, 0)
```

---

# ✅ 9. Linked List

**What it is**  
Sequence of nodes where each points to the next.

**Real-world analogy**  
Treasure hunt clues — each clue leads to the next.

**When to use**  
- Frequent insertions/deletions at head  
- Reverse list problems  
- Cycle detection (Floyd’s tortoise & hare)

**Example**  
Singly linked list.

**Python code**  
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1 → 2 → 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
```

---

# ✅ 10. Binary Tree / Binary Search Tree

**What it is**  
Hierarchical structure; BST keeps left < root < right.

**Real-world analogy**  
Family tree or file system folders.

**When to use**  
- Fast search/insert/delete on sorted data (BST)  
- Tree traversals (pre/in/post/level)  
- Recursion practice

**Example**  
Search in a BST.

**Python code**  
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, target):
    if not root or root.val == target:
        return root
    if target < root.val:
        return searchBST(root.left, target)
    return searchBST(root.right, target)
```

---

# ✅ 11. Graph

**What it is**  
Nodes (vertices) connected by edges.

**Real-world analogy**  
Social network or city road map.

**When to use**  
- BFS/DFS traversal  
- Shortest path (BFS, Dijkstra)  
- Connected components / cycle detection  
- Grid problems (treated as graph)

**Example**  
Adjacency list + BFS.

**Python code**  
```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

from collections import deque
def bfs(start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        print(node, end=' ')
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

bfs(2)   # Output: 2 0 3 1
