# Python Tech Challenge - Exercise 1: Tree Structure with Heaviest Path Calculation in Python

This Python code defines a simple tree data structure and provides functionality to add nodes, display the tree hierarchy, and find the heaviest path based on node weights. The heaviest path is defined as the path from the root to any leaf node that has the maximum total weight.

## Getting Started

### Prerequisites

Ensure you have the latest version of Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Installation

Once Python is installed, no additional installation is required for this project. Simply download this code to your local machine.

### Running the Code

Navigate to the directory containing the script and execute it using Python:

```bash
python ejercicio_1.py
```

An alternative way of running the code is using the "Run Python File on Terminal" function located in your code editor with a right-click on the code file.

### Example Usage

The provided example initializes a tree with a root node named "root" with a weight of 10. It adds several child nodes and then displays the tree structure. It also prints the heaviest path in the tree along with its total weight. In this case, for convenience of testing, it is also included on the code itself.

```python
# Test
tree = Tree("root", 10)
tree.add_child("root", "child1", 5)
tree.add_child("root", "child2", 15)
tree.add_child("child1", "child1_1", 10)
tree.add_child("child1", "child1_2", 5)
tree.add_child("child2", "child2_1", 10)
tree.add_child("child2", "child2_2", 20)

tree.display()
print("Heaviest Path:", tree.find_heaviest_path())
