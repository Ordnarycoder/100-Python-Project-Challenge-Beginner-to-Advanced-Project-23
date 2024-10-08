from collections import deque

stack = deque()

stack.append("x")
stack.append("y")
stack.append("z")

print(f"Stack example: {stack}")

print("Elements removed from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

