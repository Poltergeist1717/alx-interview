#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
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

