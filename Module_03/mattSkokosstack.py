from mattSkokosnode import Node


class isEmptyError(Exception):
    pass


class Stack:

    def __init__(self, head=None, data=None):
        self.data = None
        self.head = head
        if self.data is not None:
            self.push(data)
        self.size = 0

    def push(self, data):
        """ Pushes data to top of stack. """
        self.head = Node(self.head, data)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise isEmptyError("Stack is empty, cannot pop an item.")
            return False
        else:
            temp = self.head.getValue()
            self.head = self.head.getNext()
            self.size -= 1
            return temp

    def peek(self):
        if self.isEmpty():
            raise isEmptyError("Stack is empty, cannot peek an item.")
            return False
        else:
            return self.head.getValue()

    def isEmpty(self):
        return self.size == 0
    # or head == None

    @classmethod
    def createStack(cls, name):
        name = Stack()
        return name

    def deleteStack(self, name):
        name.clear()

