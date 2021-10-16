
class MaxStack:

    def __init__(self):
        self.__main_stack = []
        self.__max_stack = []

    def push(self, item):
        self.__main_stack.append(item)
        if len(self.__max_stack) > 0:
            if self.__max_stack[-1] <= item:
                self.__max_stack.append(item)
        else:
            self.__max_stack.append(item)

    def pop(self):
        assert(len(self.__main_stack))
        item = self.__main_stack.pop()
        if self.__max_stack[-1] == item:
            self.__max_stack.pop()
            if len(self.__main_stack) and len(self.__max_stack):
                if self.__max_stack[-1] < self.__main_stack[-1]:
                    self.__max_stack.append(self.__main_stack[-1])
        return item

    def max(self):
        print(self.__max_stack[-1])

if __name__ == "__main__":
    stack = MaxStack()
    n = int(input())
    queries = [input() for _ in range(n)]
    for q in queries:
        query = q.split()
        if query[0] == 'push':
            stack.push(int(query[1]))
        elif query[0] == 'pop':
            stack.pop()
        elif query[0] == 'max':
            stack.max()
