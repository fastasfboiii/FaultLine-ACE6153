# FaultLine-ACE6153

Simulation of **page replacement algorithms** for ACE6153 (Operating Systems) Assignment 2.

This project models a **cache (page frames)** of fixed size and runs three classic replacement strategies:

- **FIFO** (First-In, First-Out)
- **LRU** (Least Recently Used)
- **LFU** (Least Frequently Used)

It prints the **cache state after every page request**, and reports:
- **Total page faults**
- **Total page hits**

---

## What the assignment is about

When a system has limited memory (cache frames), it can only hold a certain number of pages at a time (here: **5**).  
As pages are requested, the algorithm decides whether the request is:

- **Hit**: the page is already in cache 
- **Fault**: the page is not in cache (must be loaded)

If the cache is full and a fault happens, the algorithm must **evict** a page to make space.

---

## Algorithms (simple explanation)

### FIFO — First-In, First-Out
Evicts the **oldest page** in the cache (the one that entered first), regardless of how often it was used.

### LRU — Least Recently Used
Evicts the page that **has not been used for the longest time**.

### LFU — Least Frequently Used
Evicts the page with the **lowest usage count** (fewest hits).  
If there’s a tie, the code keeps the default tie behavior of Python’s `min()` on the current cache order.

---

## Input / Configuration

The program uses:

- `CACHE_SIZE = 5`
- Example input string:
```

8, 2, 6, 4, 7, 8, 9, 2, 0, 1, 6, 4, 0, 8, 5

````

You can edit these at the top of the main Python file:

```python
CACHE_SIZE = 5
PAGES = [8, 2, 6, 4, 7, 8, 9, 2, 0, 1, 6, 4, 0, 8, 5]
````

---

## How to run

### Requirements

* Python 3.10+ (recommended)

### Run the program

```bash
python3 main.py
```

It will run FIFO, LRU, and LFU in order and print:

* Cache state after each request
* Total page faults
* Total page hits

---

## Output format (example)

Example output structure:

```
FIFO Page Replacement Algorithm Simulation:
Cache state: [8]
Cache state: [8, 2]
...
Total page faults: X
Total page hits: Y
```

---

## Notes / Important detail

**Page faults are counted whenever a requested page is NOT in cache**
This includes when the cache is still being filled (first few unique pages).

---

## Repo structure

Typical structure:

```
FaultLine-ACE6153/
  main.py
  README.md
```

---

## Author

Ahmed Yasser
Rian Salem
Yaquob

