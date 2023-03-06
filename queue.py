from collections import deque
print("List as a queue data structure in python")

queue = deque(["apple", "Banana", "orange"])
print(queue)
queue.append("grapes")
print(queue)
queue.append("mango")
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
