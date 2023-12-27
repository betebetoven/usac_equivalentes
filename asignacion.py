#class asignacion, it will have an id and a value for a constructor, and when
#called as a funciton, it will add the value to a dict passed to it
class asignacion:
    def __init__(self, id, value):
        self.id = id
        self.value = value
    def __call__(self, context):
        #if self value is instance of serie or paralelo, we call it as a function
        if isinstance(self.value, serie) or isinstance(self.value, paralelo):
            self.value = self.value(context)
        
        context[self.id] = self.value
        return f'Asignacion de {self.id} a {str(self.value)}'
        
# class serie it will have two values as a constructor, it either can be a variable in the dict or an object from the class 
#serie or this clas(paralelo), each class also has a call function that will return the value of the object
# and we also will pass the context if we are working to know the resistance, or the capacitance
class serie:
    def __init__(self, value1, value2):
        #print("serie")
        self.value1 = value1
        self.value2 = value2
    def __call__(self, symbol_table):
        #validacion valor 1
        if isinstance(self.value1, serie) or isinstance(self.value1, paralelo):
            value1 = self.value1(symbol_table)
        elif isinstance(self.value1, int) or isinstance(self.value1, float):
            value1 = self.value1
        else:
            value1 = symbol_table[self.value1]
            
        #validacion valor 2
        if isinstance(self.value2, serie) or isinstance(self.value2, paralelo):
            value2 = self.value2(symbol_table)
        elif isinstance(self.value2, int) or isinstance(self.value2, float):
            value2 = self.value2
        else:
            value2 = symbol_table[self.value2]
            
        
        #now lets check if we are working with capacitance or resistance
        if symbol_table['contexto'] == 'R':
            return value1 + value2
        elif symbol_table['contexto'] == 'C':
            return (1/value1 + 1/value2)**-1
    def __str__(self):
        return f' objeto serie {self.value1} + {self.value2}'
class paralelo:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def __call__(self, symbol_table):
        #validacion valor 1
        if isinstance(self.value1, serie) or isinstance(self.value1, paralelo):
            value1 = self.value1(symbol_table)
        elif isinstance(self.value1, int) or isinstance(self.value1, float):
            value1 = self.value1
        else:
            value1 = symbol_table[self.value1]
            
        #validacion valor 2
        if isinstance(self.value2, serie) or isinstance(self.value2, paralelo):
            value2 = self.value2(symbol_table)
        elif isinstance(self.value2, int) or isinstance(self.value2, float):
            value2 = self.value2
        else:
            value2 = symbol_table[self.value2]
        #now lets check if we are working with capacitance or resistance
        if symbol_table['contexto'] == 'R':
            return (1/value1 + 1/value2)**-1
        elif symbol_table['contexto'] == 'C':
            return value1 + value2
    def __str__(self):
        return f' objeto paralelo {self.value1} + {self.value2}'