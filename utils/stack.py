from collections import deque

class Stack:

  def __init__(self):
    self._items = deque()

  def empty(self):
    return len(self._items) == 0

  def push(self, item):
    self._items.append(item)

  def pop(self):
    return self._items.pop()
