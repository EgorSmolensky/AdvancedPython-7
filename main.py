class Stack:

    opening = '([{'
    closing = {')': '(', ']': '[', '}': '{'}

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return not bool(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return None

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None

    def size(self):
        return len(self.stack)


def check_sequence(seq):
    stack = Stack()
    for brace in seq:
        if brace in stack.opening:
            stack.push(brace)
        elif stack.isEmpty() or stack.peek() != stack.closing[brace]:
            return False
        else:
            stack.pop()
    return True


if __name__ == '__main__':
    braces = input()
    if check_sequence(braces):
        print("Сбалансированно")
    else:
        print("Несбалансированно")



