"""
Time Complexity for:
1. Node Class:
T(n) = 7 ---> Big-O = O(1)

2. Stack Class:
Since operations (pop and push) are only performed at head:
T(n) = 16 --->  Big-O = O(1)

3. Test Driver:
T(n) = 2(n) + 8 ---> Big-O = O(n)

4. Overall: Big-O = O(n) where 'n' is size of the string.

Space Complexity for all operations ---> O(1)

"""

from mattSkokosstack import Stack


def checkSymbolBalanced(symbolString):
    """ Takes in a string and filters for 3 types of braces: {} [] ().
    Uses the Stack() class to check for balanced input, returns True if
    balanced and False if not
     """
    symbolStack = Stack()
    balanced = True
    index = 0
    symbolString = ''.join((char for char in symbolString if char
                            in '{}[]()'))

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        try:
            if symbol in "([{":
                symbolStack.push(symbol)
            else:
                if symbolStack.isEmpty():
                    balanced = False
                else:
                    top = symbolStack.pop()
                    if not matches(top, symbol):
                        balanced = False
        except ValueError:
            return 0
        index = index + 1
    if balanced and symbolStack.isEmpty():
        return 1
    else:
        return 0


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def main():
    # createStack() demo
    stack1 = Stack()
    stack1.createStack('letters')
    stack1.push('a')
    stack1.push('b')

    # balanced symbol demo
    print("Balanced Symbol Check Demo: \n")

    print("Test Case 1 ('[]'): ", checkSymbolBalanced('[]'))
    print("Test Case 2 ('{({([][])}())}'): ",
          checkSymbolBalanced('{({([][])}())}'))
    print("Test Case 3 ('[{()]'): ", checkSymbolBalanced('[{()]'))
    print("Test Case 4 ('([|)]'): ", checkSymbolBalanced('([|)]'))
    print("Test Case 5 ('(asdf)'): ", checkSymbolBalanced('(asdf)'))
    print("Test Case 6 ('{{([][])}()}'): ",
          checkSymbolBalanced('{{([][])}()}'))
    print("Test Case 7 ('['): ", checkSymbolBalanced('['))


if __name__ == "__main__":
    main()


"""
Sample Run #1: 
Balanced Symbol Check Demo: 

Test Case 1 ('[]'):  1
Test Case 2 ('{({([][])}())}'):  1
Test Case 3 ('[{()]'):  0
Test Case 4 ('([|)]'):  0
Test Case 5 ('(asdf)'):  1
Test Case 6 ('{{([][])}()}'):  1
Test Case 7 ('['):  0

Process finished with exit code 0
"""