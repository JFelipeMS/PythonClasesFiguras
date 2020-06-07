import math

class Punto:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def getX(self):
        return self.X
    def getY(self):
        return self.Y

class Linea:
    def __init__(self, PntIni, PntFin):
        self.PntIni = PntIni
        self.PntFin = PntFin
    def getLongitud(self):
        dx = self.PntIni.getX() - self.PntFin.getX()
        dy = self.PntIni.getY() - self.PntFin.getY()
        return math.sqrt(dx**2 + pow(dy,2))

class Poligono:
    def __init__(self, Vertices):
        self.Vertices = Vertices
    def getArea(self):
        nver = len(self.Vertices)
        diaga = self.Vertices[nver-1].getX()*self.Vertices[0].getY()
        diagb = self.Vertices[nver-1].getY()*self.Vertices[0].getX()
        for x in range(nver-1):
            diaga += self.Vertices[x].getX()*self.Vertices[x+1].getY()
            diagb += self.Vertices[x].getY()*self.Vertices[x+1].getX()
        return abs(diaga - diagb) / 2
    def getPerimetro(self):
        nver = len(self.Vertices)
        longi = Linea(self.Vertices[0],self.Vertices[nver-1]).getLongitud()
        for x in range(nver-1):
            longi += Linea(self.Vertices[x],self.Vertices[x+1]).getLongitud()
        return longi

class Cuadrilatero(Poligono):
    def __init__(self, Vertices):
        Poligono.__init__(self,Vertices)
    def getTipo(self):
        nver = len(self.Vertices)
        if nver != 4: 
            return False
        a = Linea(self.Vertices[0],self.Vertices[1]).getLongitud()
        b = Linea(self.Vertices[1],self.Vertices[2]).getLongitud()
        c = Linea(self.Vertices[2],self.Vertices[3]).getLongitud()
        d = Linea(self.Vertices[3],self.Vertices[0]).getLongitud()
        if a == b and a == c and a == d:
            return "Cuadrado"
        elif a == c and b == d:
            return "Rectangulo"
        elif a == c or b == d:
            return "Trapecio"
        else:
            return "Trapezoide"
            

pnt01 = Punto(0,0)
pnt02 = Punto(3,4)
print (pnt02.getX())
print (pnt02.getY())

pnt03 = Punto(3,0)
pnt04 = Punto(0,4)

lin01 = Linea(pnt01,pnt02)
print (lin01.getLongitud())

vertices = [pnt01, pnt03, pnt02, pnt04]

pol01 = Poligono(vertices)
print (pol01.getPerimetro())
print (pol01.getArea())

cua01 = Cuadrilatero(vertices)
print (cua01.getPerimetro())
print (cua01.getArea())
print (cua01.getTipo())
