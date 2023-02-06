class Alumno:
    nombre = None
    nota = None
    
    def __init__(self):
        self.nombre = "nadie"
        self.nota = 0
        
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_nota(self, nota):
        if nota in range(0,10):
            self.nota =  nota
        else:
            self.nota = 0
    
    def get_alumno(self):
        return self.alumno
    
    def get_nota(self):
        return self.nota
    
    def show_alumno (self):
        print("El alumno ", self.nombre, "tiene nota : ", self.nota)
        if self.nota>=5 :
            print("Por lo tanto ha aprobado")
        else: 
            print("Por lo tanto ha suspendido")
            
A = Alumno()
A.show_alumno()
A.set_nombre("Pedro")
A.set_nota(-6)
A.show_alumno()
A.set_nota(6)
A.show_alumno()