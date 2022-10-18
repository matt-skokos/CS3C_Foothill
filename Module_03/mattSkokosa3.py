from mattSkokosstack import Stack


def parChecker(symbolString):
    """Will take in a string consisting of 3 types of braces: {} [] ().
    Uses the Stack() class to check for balanced input, returns True if
    balanced and False if not
     """
    stack1 = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        try:
            if symbol in "([{":
                stack1.push(symbol)
            # if symbol in "}])":
            #     stack1.pop()
            else:
                if stack1.isEmpty():
                    balanced = False
                else:
                    top = stack1.pop()
                    if not matches(top, symbol):
                        balanced = False
        except ValueError:
            return False
        index = index + 1
    if balanced and stack1.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def main():
    stack1 = Stack()
    print(parChecker('{({([][])}())}'))
    print(parChecker('[{()]'))

    print(parChecker('([|)]'))
    print(parChecker('{{([][])}()}'))
    print(parChecker('{{([][])}()}'))


if __name__ == "__main__":
    main()
