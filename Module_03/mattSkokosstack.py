"""Questions for Stack class:
1.  What?


Time Complexity: O(1), for all push(), pop(), and peek(), as we are not
performing any kind of traversal over the list. We perform all the
operations through the current pointer only.
Auxiliary Space: O(N), where N is the size of the stack
"""
from mattSkokosnode import Node


class Stack:
    def __init__(self):
        self.head = 'data'
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return False
        else:
            return self.pop()

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.stack[:-1]

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    @classmethod
    def createStack(cls, name):
        return Stack(name)

    def deleteStack(self, name):
        name.clear()
