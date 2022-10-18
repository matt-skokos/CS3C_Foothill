"""Ask in forum:
1.  These are two different helper methods used in the validation process right?
    Is the node pointing

    setter must change last node from pointing to previous target, to the
    new node
"""

class Node:
    def __init__(self, _next, value=None):
        self.value = value
        self.next = _next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, newValue):
        """ Set node value. """
        if self.validateParam(newValue):
            self.value = newValue
            return True
        else:
            return False

    def setNext(self, newNext):
        """ Set 'next' node value. """
        if self.validateParam(newNext):
            self.next = newNext
            return True
        else:
            return False

    @staticmethod
    def validateParam(param):
        """ Validate proper input received by setter ( str )."""
        return isinstance(param, str)

    @staticmethod
    def checkNodeNext(node):
        """ Validate that node points to another node ( not None )."""
        return node.next is not None
