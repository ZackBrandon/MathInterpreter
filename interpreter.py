#Interprets the tree
from nodes import *
from values import Number

#The interpreter will take the base node (the 'top' node) and recursively call the .visit()
#method on all of the corresponding nodes, ultimately returning a number.
class Interpreter:
    #Pass in the root node of our tree. It will be processed and then return a number
    def visit(self, node):
        #Create a string of the method that we want to call based on the node passed to .visit()
        #Ex. AddNode => visit_AddNode
        method_name = f'visit_{type(node).__name__}'
        #Method will now be the method that we need to call based on what was passed into .visit()
        method = getattr(self, method_name) #if an addNode is passed in, then method now equals visit_AddNode()
        #return the appropriate method called on the passed in node
        #method(node) returns 
        return method(node)
    
    #Returns the value of a NumberNode()
    def visit_NumberNode(self,node):
        #Returns a number value of the passed in number node
        return Number(node.value)
    
    #Returns the value of an AddNode()
    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    #Returns the value of a SubtractNode()
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    #Returns the value of a MultiplyNode()
    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    #Returns the value of a DivideNode()
    def visit_DivideNode(self, node):
        #Error catching (for math divide by zero)
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    #Returns the value of a PowerNode()
    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    #returns the value of a PlusNode()
    def visit_PlusNode(self, node):
        return self.visit(node.node)
    
    #returns a negated version of the node value
    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)