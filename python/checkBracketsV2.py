class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top =[]

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]


def checkBracketsV2(lines):
    stack = Stack()
    for line in lines:
        if line in ('{', '[', '('):
            stack.push(line)
        elif line in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (line == "}" and left != "{") or (line == "]" and left != "[") or (line == "(" and left != ")"):
                    return False

    return stack.isEmpty()


filename = "4.1.py"
infile = open(filename,"r",encoding=('UTF'))
lines = infile.readlines()
infile.close()

result = checkBracketsV2(lines)
print(filename, "--->", result)