from tokens import Token, TokenType

#the lexer generates tokens from the text input and returns them

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    #Init takes in the text line that we are currently processing (into 'text')
    def __init__(self, text):
        #The current text line is stored in the 'text' iterator which allows us to move through it
        self.text = iter(text)
        #Before we do anything, we need to advance to the very first character
        self.advance()
    #The advance method will move on to the next character and save it in self.current_char
    def advance(self):
        #Once we reach the end of the text field we are processing, an error will be thrown (StopIteration)
        try:
            self.current_char = next(self.text)
        #We want to catch that error and reset the current_char to None
        except StopIteration:
            self.current_char = None
    def generate_tokens(self):
        #Until we have reached the end of the input:
        while self.current_char != None:
            #Skip whitespace characters
            if self.current_char in WHITESPACE:
                #and just go to the next character
                self.advance()

            #NUMBER token
            elif self.current_char == '.' or self.current_char in DIGITS:
                #Use a generator to return the number token to whoever calls the .generate_tokens() method
                yield self.generate_number()

            #PLUS Token
            elif self.current_char == '+':
                #advance past the plus token
                self.advance()
                #yield the plus token (without any value)
                yield Token(TokenType.PLUS)

            #MINUS Token
            elif self.current_char == '-':
                #advance past the minus token
                self.advance()
                #yield the minues token (without any value)
                yield Token(TokenType.MINUS)

            #MULTIPLY Token
            elif self.current_char == '*':
                #advance past the multiply token
                self.advance()
                #yield the multiply token (without any value)
                yield Token(TokenType.MULTIPLY)

            #DIVIDE Token
            elif self.current_char == '/':
                #advance past the divide token
                self.advance()
                #yield the divide token (without any value)
                yield Token(TokenType.DIVIDE)

            #LPAREN Token
            elif self.current_char == '(':
                #advance past the lparen token
                self.advance()
                #yield the lparen token (without any value)
                yield Token(TokenType.LPAREN)

            #RPAREN Token
            elif self.current_char == ')':
                #advance past the rparen token
                self.advance()
                #yield the rparen token (without any value)
                yield Token(TokenType.RPAREN)
            
            #If we do not understand the current character
            else:
                #raise and Exception
                raise Exception(f"Illegal Character '{self.current_char}'")
    #returns number tokens
    def generate_number(self):
        #variable to keep track of how many decimal points we have come across (we can only have 1 in a number)
        decimal_point_count = 0
        #number_str will keep track of the built up number string
        number_str = self.current_char
        #Go to the next character
        self.advance()
        #until we reach the end of the input AND we are currently on a decimal point or a digit
        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            #if the current character is a decimal point,
            if self.current_char == '.':
                #increase the decimal point count number
                decimal_point_count += 1
                #if this is the second decimal point, we are done with this number
                if decimal_point_count > 1:
                    #So we break out of the loop
                    break
            #if the current character is not a decimal point, build up the string
            number_str += self.current_char
            #and then advance the iterator
            self.advance()

        #trailing/leading 0 handler once we have the entire number inside of number_str

        #if our number string starts with a '.'
        if number_str.startswith('.'):
            #put a zero on the end of it
            number_str = '0' + number_str
        
        #if our number string ends with a '.'
        if number_str.endswith('.'):
            #add a zero onto the end of it
            number_str += '0'

        #Now that we have built up our number, we can create a token and then return it
        #creates a token with the NUMBER type (ID of 0) and a value of float(number_str)
        return Token(TokenType.NUMBER, float(number_str))