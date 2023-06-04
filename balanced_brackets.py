from stack import Stack

def is_balanced(text):
    stack = Stack()
    for i in text:
        if i in ['(', '[', '{']:
            stack.push(i)
        elif i in [')', ']', '}']:
            if stack.is_empty():
                return False
            elif (stack.peek() == "(" and i == ")") or \
                    (stack.peek() == "[" and i == "]") or \
                    (stack.peek() == "{" and i == "}"):
                stack.pop()
            else:
                return False
    return stack.is_empty()


text = "(((([{}])))))"
print(is_balanced(text))