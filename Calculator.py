#DAVID GARCIA
# DO NOT FORGET TO ADD COMMENTS!!!
#3/3/23
#FIX: RENAMED "calculator.py" to "Calculator.py" to accomodate the def "calculator" in "calculatorGUI.py"
from stack import Stack
from tree import ExpTree
def infix_to_postfix(infix):
    opStack = Stack()
    prio = {'*':3,'/':3,'-':2,'+':2,'(':1} #priority heiracrchy dictionary 1 being highest priority
    num = ''
    postfix = ''
    for i in range(len(infix)):
        if infix[i] in '0123456789.':
            num+=infix[i]
        elif infix[i] not in '0123456789.':
            if num != '':
                postfix+=num+" "
                num=''
            if infix[i] == '(':
                opStack.push(infix[i])
            elif infix[i] == ')':
                while opStack.peek() != '(':
                    postfix+=opStack.pop()+" "
                opStack.pop()
            elif infix[i] in '*/+-':
                if opStack.isEmpty() or prio[infix[i]] > prio[opStack.peek()]:
                    opStack.push(infix[i])
                else:
                    postfix+=opStack.pop()+" "
                    opStack.push(infix[i])
    postfix+=num+' '+' '.join(opStack.items[::-1])
    return postfix

def calculate(infix):
    return ExpTree.evaluate(ExpTree.make_tree(infix_to_postfix(infix)))

# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    
    
