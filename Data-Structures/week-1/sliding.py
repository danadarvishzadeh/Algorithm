
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
        if len(self.__max_stack):
            return self.__max_stack[-1]
        else:
            return -1

    def len(self):
        return len(self.__main_stack)


class Queue:

    def __init__(self):
        self.s1 = MaxStack()
        self.s2 = MaxStack()
        self.n = int(input())
        self.nums = list(map(int, input().split()))
        self.m = int(input())
        self.result = []


    def transfer(self):
        for _ in range(self.s2.len()):
            self.s1.push(self.s2.pop())

    def compute(self):
        for i in range(self.m):
            pointer = i
            self.s2.push(self.nums[pointer])
        self.result.append(max(self.s1.max(), self.s2.max()))
        while pointer < self.n-1:
            if self.s2.len() == self.m:
                self.transfer()
            self.s1.pop()
            pointer += 1
            self.s2.push(self.nums[pointer])
            self.result.append(max(self.s1.max(), self.s2.max()))

    def show_results(self):
        [print(_, end=' ') for _ in self.result]
        print()
            

if __name__ == "__main__":
    q = Queue()
    q.compute()
    q.show_results()
