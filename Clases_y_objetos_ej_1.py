class vehiculo:
    color = None
    ruedas = None
    puertas = None

    def set_color(self, color):
        self.color = color

    def set_n_ruedas(self, n_ruedas):
        self.ruedas = n_ruedas

    def set_n_puertas(self, n_puertas):
        self.puertas = n_puertas

    def show_color(self):
        print("Este vehiculo es de color: " ,self.color)

    def show_n_ruedas(self):
        print("Este vehiculo tiene " , self.ruedas , "ruedas")

    def show_n_puertas(self):
        print("Este vehiculo tiene " , self.puertas , "puertas")
    

class coche(vehiculo):
    velocidad  = None
    cilindrada = None
    
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
        
    def set_cilindrada(self, cilindrada):
        self.cilindrada = cilindrada
        
    def show_velocidad(self):
        print("Velocidad: ", self.velocidad, "Km/h")
        
    def show_cilindrada(self):
        print("Cilindrada: ", self.cilindrada, "cc")
        
c = coche()
c.set_color("amarillo")
c.set_n_puertas(5)
c.set_n_ruedas(4)
c.set_velocidad(100)
c.set_cilindrada(200)
c.show_color()
c.show_n_puertas()
c.show_n_ruedas()
c.show_velocidad()
c.show_cilindrada()