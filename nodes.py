from dataclasses import dataclass
#This file defines all of our differnet node types

#the number node is the most simple.
@dataclass
class NumberNode:
    #It only has a value that is a float.
    value: float

    #the repr method makes it easy to print out (simply a number as a string here)
    def __repr__(self):
        return f"{self.value}"


#used to add two nodes together
@dataclass
class AddNode:
    #either added node can be of any type
    node_a: any
    node_b: any

    #allows us to print this node to the screen in parens
    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


#used to subtract two nodes.
@dataclass
class SubtractNode:
    #either added node can be of any type
    node_a: any
    node_b: any

    #allows us to print this node to the screen in parens
    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


#used to multiply two nodes together.
@dataclass
class MultiplyNode:
    #either node can be of any type
    node_a: any
    node_b: any

    #allows us to print this node to the screen in parens
    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


#used to divide two nodes
@dataclass
class DivideNode:
    #either node can be of any type
    node_a: any
    node_b: any

    #allows us to print this node to the screen in parens
    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"

#doesn't really do anything..but for example if you said +5
@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

#Adds a minus
@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"