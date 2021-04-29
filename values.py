#Holds the differnet value types that the interpreter is able to produce
from dataclasses import dataclass

#Since we are only working with numbers, this is all we needed for this.
@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"
