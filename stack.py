#DAVID GARCIA
# DO NOT FORGET TO ADD COMMENTS!!!
#3/3/23
#FIX: RENAMED "calculator.py" to "Calculator.py" to accomodate the def "calculator" in "calculatorGUI.py"
class Stack:

    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# a driver program for class Stack
#FIX: RENAMED "calculator.py" to "Calculator.py" to accomodate the def "calculator" in "calculatorGUI.py"
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
