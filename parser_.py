from tokens import TokenType
from nodes import *
#this parser transforms the tokens generator list objext passed into it into nodes

'''
Example of a generator object list that is passed into Parser (tokens) for reference

Exmaple call: parser = Parser(tokens)

the text input would be: 
5 + ( 4 * 8 )

Tokens generator list would look like: 
[NUMBER:5.0, PLUS, LPAREN, NUMBER:4.0, MULTIPLY, NUMBER:8.0, RPAREN]

TokenType.NUMBER is the type, 5.0 is the TokenType.value

'''
class Parser:
    #parser takes in tokens (will be a generator object that we can iterate through)

    def __init__(self, tokens):
        #self.tokens is a generator object (essentially a list) that we can now iteratre through
        self.tokens = iter(tokens)
        #advances to the first token for us to look at
        self.advance()

    #advances to the next token in the generator object list of tokens in self.tokens
    def advance(self):
        #advance in every case but when we are on the last token (catch the exception)
        try:
            #self.current_token will be defined as the token that the parser is currently looking at
            #move to the next token and set it to the current one
            self.current_token = next(self.tokens)
        except StopIteration:
            #If we are at the end of the tokens list and we tried to move to the next one, catch the error and set it to none
            self.current_token = None

    #raises an error
    def raise_error(self):
        raise Exception("Invalid Syntax")

    #the entry point into the parser
    def parse(self):
        #If the user has not input anything,
        if self.current_token == None:
            #return nothing
            return None
        #self.expr() returns a node, passes that node into result (after this line calls, there should be no more tokens left to parse)
        #and self.current_token should be set to None (because it reached the last token in self.tokens)
        result = self.expr()
        #ERROR CHECKING
        #check if current_token is not equal to none (this would be caused by invalid syntax and leftover tokens)
        if self.current_token != None:
            #Throw an invalid syntax error
            self.raise_error()
        #return the node
        return result

    #returns an expression to be parsed by self.parse()
    def expr(self):
        #this result is a term node, pass that into 'result', look for a term
        result = self.term()

        #next, we want to look for 0 or more +/- operators to build the expression
        #When we get to a plus or a minus TokenType in our generator list:
        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            #If it's a plus operator:
            if self.current_token.type == TokenType.PLUS:
                #advance to the next token
                self.advance()
                #Then we need to create an AddNode() and reassign it to the result veriable
                result = AddNode(result, self.term())
            #If it's a minus operator:
            elif self.current_token.type == TokenType.MINUS:
                #advance to the next token
                self.advance()
                #Create a SubtractNode(), and reassign it to the result variable
                result = SubtractNode(result, self.term())                

            #return the result (which will be either an AddNode() or a SubtractNode() )
        return result
        
    #Returns a term to be evaluated by self.expression()
    def term(self):
        #the result is a factor node, pass that into 'result', look for a factor
        result = self.factor()


        #next, we want to look for 0 or more * or / operators to build the expression
        #When we get to a multiply or a divide TokenType in our generator list:
        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            #If it's a plus operator:
            if self.current_token.type == TokenType.MULTIPLY:
                #advance to the next token
                self.advance()
                #Then we need to create a MultiplyNode() and reassign it to the result veriable
                result = MultiplyNode(result, self.factor())
            #If it's a divide operator:
            elif self.current_token.type == TokenType.DIVIDE:
                #advance to the next token
                self.advance()
                #Create a DivideNode(), and reassign it to the result variable
                result = DivideNode(result, self.factor())                

            #return the result (which will be either a DivideNode() or a MultiplyNode() )
            #print(result)
        return result
    
    #returns a factor to be evaluated by self.term()
    def factor(self):
        #store the current_token in a new 'token' variable
        token = self.current_token

        #If the current token type is a left parenthesis
        if token.type == TokenType.LPAREN:
            #advance to the next token
            self.advance()
            #store the following expression into 'result'
            result = self.expr()

            #After parsing the expression, we should be left with a right parenthesis
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            
            self.advance()
            return result
        #if the current token type is a number:
        elif token.type == TokenType.NUMBER:
            #advance to the next token
            self.advance()
            #create and retutrn a new NumberNode() with the value of token.value
            return NumberNode(token.value)
        
        #If the current token type is a PlusNode (+5, for example)
        elif token.type == TokenType.PLUS:
            #advance to the next token
            self.advance()
            #recursively call this function until you have all of the +'s sorted out (Ex. +++++5)
            return PlusNode(self.factor())
        
        #If the current token type is a minus node:
        elif token.type == TokenType.MINUS:
            #advance to the next token
            self.advance()
            #recursively call this function until you have all the -'s sorted out (Ex. ---5)
            return MinusNode(self.factor())
        #If there is no number (two **, for example), we want to raise a syntax error
        self.raise_error()
        
        