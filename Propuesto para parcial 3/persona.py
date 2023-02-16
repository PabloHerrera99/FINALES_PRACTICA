class Persona:
    def __init__(self, apellido, nombre):
        self._Persona__apellido = apellido
        self._Persona__nombre = nombre
        self._Persona__persona_id = None
    
    def __str__(self):
        return str(self._Persona__apellido + ', ' + self._Persona__nombre)
    
    

if __name__ == '__main__':
    p = Persona('herrera', 'pablo')
    print(p.__dict__)
    print(p)
    
    