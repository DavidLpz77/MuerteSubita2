from functools import reduce

lista = [8,4,5,7,3,1,2,10,12,15]
L =  (reduce(lambda x,y: x, lista))
D = (list (filter(lambda z: z<reduce(lambda x,y: x, lista)**5 ,lista)))
print (L)
print (D)

 
