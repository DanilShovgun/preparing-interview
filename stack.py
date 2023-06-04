class Stack:
    
    def __init__(self) -> list:
        self.stack = []
    
    def is_empy(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()    
            
    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)        