"""Ask in forum:
1.  These are two different helper methods used in the validation process right?
    Is the node pointing

    setter must change last node from pointing to previous target, to the
    new node
"""

class Node:
    def __init__(self, _next, data=None):
        self.next = _next
        self.data = data


    def getValue(self):
        """ Return Node data. """
        return self.data

    def getNext(self):
        """ Return Node pointer value. """
        return self.next

    def setValue(self, newValue):
        """ Set node value. """
        if self.validateParam(newValue):
            self.value = newValue
            return True
        else:
            return False

# Check this out again
    def setNext(self, newNext):
        """ Set 'next' node value. """
        if self.checkNodeNext(newNext):
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
