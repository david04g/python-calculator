#DAVID GARCIA
# DO NOT FORGET TO ADD COMMENTS!!!
#3/3/23
#FIX: RENAMED "calculator.py" to "Calculator.py" to accomodate the def "calculator" in "calculatorGUI.py"
from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):
    def make_tree(postfix):
        bigStack = Stack()
        for i in range(len(postfix)):
            if postfix[i] in ".0123456789":
                bigStack.push(ExpTree(postfix[i]))
            elif postfix[i] in "+-/*":
                temp = ExpTree(postfix[i])
                temp.rightChild = bigStack.pop()
                temp.leftChild = bigStack.pop()
                bigStack.push(temp)
        return bigStack.pop()
    def preorder(tree):
        s = ''
        if tree != None:
            if tree.getRootVal() != None:
                s += tree.getRootVal()
            if tree.getLeftChild() != None:
                s += ExpTree.preorder(tree.getLeftChild())
            if tree.getRightChild() != None:
                s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''
        if tree != None:
            if tree.getLeftChild() != None:
                s = '('
                s+=ExpTree.inorder(tree.getLeftChild())
            if tree.getRootVal() != None:
                s+= tree.getRootVal()
            if tree.getRightChild() != None:
                s+=ExpTree.inorder(tree.getRightChild())
                s+=')'
        return s
      
    def postorder(tree):
        s = ''
        if tree != None:
            if tree.getLeftChild() != None:
                s+= ExpTree.postorder(tree.getLeftChild())
            if tree.getRightChild() != None:
                s+=ExpTree.postorder(tree.getRightChild())
            if tree.getRootVal() != None:
                s+=tree.getRootVal()
        return s

    def evaluate(tree):
        if tree != None:
            if tree.getRootVal() in '.0123456789':
                return tree.getRootVal()
            else:
                a = float(ExpTree.evaluate(tree.getLeftChild()))
                b = float(ExpTree.evaluate(tree.getRightChild()))
                if tree.getRootVal() =='*':
                    runval = a * b
                elif tree.getRootVal() =='/':
                    runval = a / b
                elif tree.getRootVal() == '+':
                    runval = a + b
                elif tree.getRootVal() == '-':
                    runval = a - b
                return runval

            
    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    
    
