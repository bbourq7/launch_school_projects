from datetime import datetime

dt = datetime.now()
print(str(dt))
print(repr(dt))

class Cat:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Cat({repr(self.name)})'
    
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
            
        return self.name == other.name
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented    
        
        return self.name != other.name
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name < other.name
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name <= other.name
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name > other.name
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name >= other.name
    
    

    

cat = Cat('Fuzzy')
print(str(cat))
print(repr(cat))
