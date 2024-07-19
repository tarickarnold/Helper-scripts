from collections import deque
from heapq import heappop, heappush
from itertools import count

class IterableMixin:
    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    def enqueue(self, element) -> None:
        self._elements.append(element)

    def dequeue(self)-> any:
        return self._elements.popleft()

class Stack(Queue):
  def dequeue(self) -> any:
        return self._elements.pop()

class PriorityQueue(IterableMixin):
    def __init__(self) -> None:
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value) -> None:
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self) -> any:
        return heappop(self._elements)[-1]
