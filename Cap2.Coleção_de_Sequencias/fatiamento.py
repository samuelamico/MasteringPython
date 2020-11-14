board = [['_']*3 for i in range(3)]
print(board)

board[1][2] = 0
print(board)

t = (1,2,3)
print(t)
t *= 2
print(t)


frutas = ['banana','melao','uva','abacate']
print(sorted(frutas,reverse=True))
print(sorted(frutas,key=len,reverse=True))
frutas.sort()
print(frutas)


#### Trocar Lista por Array:

from array import array

floats = array('d', (i for i in range(1,2*10**7 )))
print(floats[-1])