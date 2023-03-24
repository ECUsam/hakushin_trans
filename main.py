# 创建一个Stack的类
# 对栈进行初始化参数设计
class Stack(object):
    def __init__(self, limit=114514):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    # 进栈
    def push(self, data):
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    # 退栈
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            # 空栈不能被弹出元素
            raise IndexError('pop from an empty stack')

    def peek(self):
        # 查看栈的栈顶元素（最上面的元素）
        if self.stack:
            return self.stack[-1]

    # 判断栈是否为空
    def is_empty(self):
        return not self.stack

    def size(self):
        # 返回栈的大小
        return len(self.stack)


def jinzhi(n, base):
    stack = Stack()
    while n > 0:
        remainder = n % base
        stack.push(remainder)
        n = int(n / base)

    while not stack.is_empty():
        print(stack.pop(), end='')
