# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    words = S.split(" ")
    stack = []
    for word in words:
        try:
            number = int(word)
            stack.append(number)
        except ValueError:
            if len(stack) == 0:
                return -1
            if word == "DUP":
                new_num = stack[-1]
                stack.append(new_num)
            elif word == "POP":
                stack.pop()
            elif word == "+":
                if len(stack) < 2:
                    return -1
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif word == "-":
                if len(stack) < 2:
                    return -1
                num1 = stack.pop()
                num2 = stack.pop()
                if num1 < num2:
                    return -1
                stack.append(num1 - num2)
            else:
                print("I don't know this word")
                return -1
    return stack[-1]