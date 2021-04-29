#Interprets the tree
from nodes import *
from values import Number

class Interpreter:
    #Pass in the root node of our tree. It will be processed and then return a number
    def visit(self, node):
        