import math
class Case:
    PI = 3.142
    G = 9.81
    def __init__(self, wall = 2, recycle =True,width = 0,length =0):
        self.width = width
        self.length = length
        self.wall = wall
        self.recycle = recycle

    def setWall(self,wall):
        self.wall = wall
    def setRecycle(self,recycle):
        self.recycle = recycle
    def setWidth(self,width):
        self.width = width
    def setLength(self,length):
        self.length = length

    #BCT = G*W*SF*PL
    def calculateBoxCompression(self,load,pallet,safety_factor):
        self.pallet = pallet
        self.safety_factor = safety_factor
        self.load = load

        if self.wall == 2:
            print("double wall")
            self.value = self.load*self.pallet*self.G*self.safety_factor
            return self.value
        else:
            print("single wall")
            self.value = self.width*self.length*0.5
            return self.value

    def calculateEdgeCompression(self, boxCompression, caliper):
        edgeCompression = boxCompression*math.sqrt(caliper)

class Carton(Case):
    pass