from lexer import Lexer
from parser_ import Parser

#main program

while True:
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
    print(tree)