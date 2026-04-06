#ejercicio 2

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x (self):
        return self.x
    
    def eje_y (self):
        return self.y
    
    def opuesto (self):
        return Punto(-self.x, -self.y)
    
punto1 = Punto(3, 4)
print("Coordenada en el eje x:", punto1.eje_x(),
       "Coordenada en el eje y:", punto1.eje_y())

print ("Coordenada opuesta en el eje x:", punto1.opuesto().eje_x(),
       "Coordenada opuesta en el eje y:", punto1.opuesto().eje_y())
    

#ejercico 3
