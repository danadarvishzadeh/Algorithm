#types: [] () {}
#print the exact place of error
#1->unmatched closing with no opening
#2->closing the wrong opening
#3->opening with no closing
#4->printing Success

def check(string):
    paren = {'(': ')', '[': ']', '{': '}'}
    stack = list()
    for i in range(len(string)):
        char = string[i]
        if char in '({[':
            stack.append((char, i+1))
        elif char in ')}]':
            if len(stack) == 0:
                return i+1
            if paren[stack[-1][0]] == char:
                stack.pop(-1)
            else:
                return i+1
    if len(stack) != 0:
        return stack[-1][1]
    else:
        return 'Success'

if __name__ == "__main__":
    string = input()
    print(check(string))
