from uuidmanager import UUIDManager

class SymbolTable():
    def __init__(self, father=None):
        self.table = {}
        self.father = father
        self.identifier = UUIDManager.get_new()


    def type_check(self, vartype, value):
        if vartype == "CHAR":
            return str(value).isalpha()
        elif vartype == "INT":
            return isinstance(value, int)

    def get_var(self, varname):
        if varname not in self.table.keys():
            if self.father:
                return self.father.get_var(varname)
            else:
                raise ValueError(f"Variable {varname} does not exist!")
        else:
            return self.table[varname][1], self.identifier


    def set_var(self, varname, value):
        if varname not in self.table.keys():
            if self.father:
                return self.father.set_var(varname, value)
            else:
                raise ValueError(f"Variable {varname} does not exist!")
        
        stored_type = self.table[varname][0]
        if stored_type != "FUNCTION":
            if not self.type_check(stored_type, value):
                raise ValueError(f"You are trying to insert value of wrong type in your variable {varname}")
        
        self.table[varname][1] = value
        return self.identifier
    
    def create_var(self, varname, vartype):
        self.table[varname] = [vartype, 0]
    


