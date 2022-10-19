"""Questions for Stack class:
1.  What?


Time Complexity: O(1), for all push(), pop(), and peek(), as we are not
performing any kind of traversal over the list. We perform all the
operations through the current pointer only.
Auxiliary Space: O(N), where N is the size of the stack
"""
from mattSkokosnode import Node

class isEmptyError(Exception):
    """Will raise if empty stack is detected while attempting
    operations.
    """
    pass

class Stack:
    def __init__(self, nodes=None):
        self.head = None
        self.size = 0
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next


    def push(self, node):
        #if list is empty, make a node
        if self.head is None:
            self.head = node
            return
        # if list has items, append behind the last one
        for current_node in self:
            pass
        current_node.next = node
        self.head = Node(node)
        self.size += 1

        # self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise isEmptyError("Stack is empty, cannot pop an item.")
            return False
        else:
            return self.pop()

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.stack[:-1]

    def isEmpty(self):
        return self.size == 0
        # if len(self.stack) == 0:
        #     raise Exception('Linked List is empty')
        #     return True
        # else:
        #     return False

    @classmethod
    def createStack(cls, name):
        name = Stack()
        return name

    def deleteStack(self, name):
        name.clear()
