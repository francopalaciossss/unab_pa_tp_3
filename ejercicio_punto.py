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
class Linea:
    def __init__ (self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha (self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia

    def mueve_izquierda (self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia

    def mueve_arriba (self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia

    def mueve_abajo (self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia

punto_a = Punto(1, 2)
punto_b = Punto(3, 4)
linea = Linea(punto_a, punto_b)
print("Coordenadas iniciales:")
print("Punto A: (", linea.punto_a.eje_x(), ",", linea.punto_a.eje_y(), ")")
print("Punto B: (", linea.punto_b.eje_x(), ",", linea.punto_b.eje_y(), ")")
linea.mueve_derecha(2)
linea.mueve_arriba(1)
print("Coordenadas después del movimiento:")
print("Punto A: (", linea.punto_a.eje_x(), ",", linea.punto_a.eje_y(), ")")
print("Punto B: (", linea.punto_b.eje_x(), ",", linea.punto_b.eje_y(), ")")


#ejercicio 4
class Cancion:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    
