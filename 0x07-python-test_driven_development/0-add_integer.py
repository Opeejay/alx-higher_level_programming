#!/usr/bin/python3

def add_integer(a,b=98):  
   if isinstance(a, int) or isinstance(a, float) and isinstance(b, int) or isinstance(b, float):
     if not isinstance(a, float) and not isinstance(a, int):
       raise TypeError('a must be an integer')
     if not isinstance(b, float) and not isinstance(b, int):
       raise TypeError('b must be an integer')
      
     """write add program"""
     return (int(a)+int(b))
   else:
     raise TypeError('a must be an integer or b must be an integer')

def add_integer(a, b=98):
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
