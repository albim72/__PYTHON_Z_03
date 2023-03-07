class InFloatValueError(Exception):
    def __init__(self,value):
        self.value=value
        
    def __str__(self):
        return f"wartość {self.value} is niewłaściwa. Dopuszczalne są tylko wartości int i float"
    
    
class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f"klucze i wartości mogą być definiowane tylko przez krotki lub listy.\n" \
               f"{self.key} jest typu: {type(self.key)}.\n" \
               f"{self.value} jest typu: {type(self.value)}."
        
