class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, newValue):
        if isinstance(newValue, str):
            self.value = newValue

    def setNext(self, newNext):
        if isinstance(newNext, str):
            self.next = newNext

    @staticmethod
    def checkNodeNext(node):
        """ Validate that the next """
        return node.next is not None
