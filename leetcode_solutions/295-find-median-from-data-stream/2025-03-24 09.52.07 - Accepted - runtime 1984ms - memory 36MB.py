class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        top = self.heap[0]
        end = self.heap.pop()
        if self.heap:
            self.heap[0] = end
            self._bubble_down(0)
        return top

    def peek(self):
        return self.heap[0] if self.heap else None

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _bubble_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def __len__(self):
        return len(self.heap)


class MaxHeap:
    def __init__(self):
        self.min_heap = MinHeap()

    def push(self, val):
        # Simulate max-heap using negative values
        self.min_heap.push(-val)

    def pop(self):
        return -self.min_heap.pop()

    def peek(self):
        top = self.min_heap.peek()
        return -top if top is not None else None

    def __len__(self):
        return len(self.min_heap)


# ---------------- MedianFinder using two heaps ----------------

class MedianFinder(object):
    def __init__(self):
        # maxHeap for lower half
        self.small = MaxHeap()
        # minHeap for upper half
        self.large = MinHeap()

    def addNum(self, num):
        # Step 1: Add to max heap
        self.small.push(num)

        # Step 2: Balance max and min heaps
        self.large.push(self.small.pop())

        # Step 3: Maintain size property
        if len(self.large) > len(self.small):
            self.small.push(self.large.pop())

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(self.small.peek())
        else:
            return (self.small.peek() + self.large.peek()) / 2.0
