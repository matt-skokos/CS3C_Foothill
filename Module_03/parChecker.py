from mattSkokosstack import Stack


def parChecker(symbolString):
    """Will take in a string consisting of 3 types of braces: {} [] ().
    Uses the Stack() class to check for balanced input, returns True if
    balanced and False if not
     """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        try:
            if symbol in "([{":
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    top = s.pop()
                    if not matches(top, symbol):
                        balanced = False
        except ValueError:
            return False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))

print(parChecker('([|)]'))
print(parChecker('{{([][])}()}'))
print(parChecker('{{([][])}()}'))
