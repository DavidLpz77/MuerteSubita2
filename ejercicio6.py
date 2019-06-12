from functools import reduce

class tupla:
    def __init__(self, valx, valy):
        self.valx = valx
        self.valy = valy

tuplas = [tupla(4,2), tupla(1,1), tupla(15,5), tupla(21,6), tupla(3,2),tupla(55,10)]        
L = (reduce(lambda x,y: x+y, map(lambda w:w.valx,filter(lambda z: z.valx==(z.valy*(z.valy+1))/2,tuplas))))

print (L)
