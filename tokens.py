from enum import Enum
from dataclasses import dataclass
#Enums allow us to associate a name with a certain ID
class TokenType(Enum):
    NUMBER      = 0
    PLUS        = 1
    MINUS       = 2
    MULTIPLY    = 3
    DIVIDE      = 4
    LPAREN      = 5
    RPAREN      = 6
    POWER       = 7

#A dataclass is a structure that can hold different fields and values
@dataclass
class Token:
    type: TokenType
    value: any = None

    #Useful for debugging, if we need to print the token list it will make it pretty for us
    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")