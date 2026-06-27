class Stack:
    def __init__(self):
        self.data = []  # 내부 리스트로 스택 구현

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if(self.is_empty()):
            return None
        value = self.data[-1]
        self.data = self.data[:-1]
        return value

    def peek(self):
        if(self.is_empty()):
            return None
        return self.data[-1]

    def is_empty(self):
        return self.data == []

    def size(self):
        return len(self.data)