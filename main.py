from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

#main program

while True:
    try:
        #store the user input for each line in the 'text' variable
        text = input("calc > ")
        #pass that into our lexer to generate our tokens (which takes text as it's only parameter)
        lexer = Lexer(text)
        #Generate the tokens from the lexer, and store them in the 'tokens' variable
        tokens = lexer.generate_tokens()
        #pass in our generated tokens list to Parser
        parser = Parser(tokens)
        #Assign the result of parser.parse() to the 'tree' variable
        tree = parser.parse()
        #If there is no tree, skip the following lines
        if not tree: continue
        #create a new interpreter, assign the 'interpreter' variable to it.
        interpreter = Interpreter()
        #Interpreter takes a tree (of nodes) and returns a value from it.
        value = interpreter.visit(tree)
        print(value)
    #If there is a problem anywhere in here, print the exception
    except Exception as e:
        print(e)