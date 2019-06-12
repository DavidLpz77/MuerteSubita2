lista = [4,24,31,12,22,5678,875,2222,8888,2468,862]

L = filter((lambda x: x%2==0 and x/10)%2==0 and (x/100)%2==0 and (x/1000)%2==0,lista)
print (L)
