from mattSkokosstack import Stack


def checkSymbolBalanced(symbolString):
    """Will take in a string consisting of 3 types of braces: {} [] ().
    Uses the Stack() class to check for balanced input, returns True if
    balanced and False if not
     """
    symbolStack = Stack()
    balanced = True
    index = 0
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
    stack1 = Stack()
    stack1.createStack('letters')
    stack1.push('a')
    stack1.push('b')
    print(stack1.data)
    print(stack1.size)
    print(checkSymbolBalanced('[]'))
    print(checkSymbolBalanced('{({([][])}())}'))
    print(checkSymbolBalanced('[{()]'))
    # you neeed to deal with "bad input" more in the proper way
    print(checkSymbolBalanced('([|)]'))
    print(checkSymbolBalanced('{{([][])}()}'))
    print(checkSymbolBalanced('{{([][])}()}'))


if __name__ == "__main__":
    main()
