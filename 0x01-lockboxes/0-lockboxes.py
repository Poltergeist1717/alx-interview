#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each inner list represents a box and contains keys as positive integers.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # Initialize a list to keep track of visited boxes
    visited[0] = True  # Mark the first box as visited

    queue = deque([0])  # Initialize a queue with the first box

    while queue:
        current_box = queue.popleft()  # Get the current box
        keys = boxes[current_box]  # Get the keys inside the current box

        for key in keys:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)  # Return True if all boxes are visited, else return False

# Example usage:
# boxes = [[1], [2], [3], []]
# print(canUnlockAll(boxes))
