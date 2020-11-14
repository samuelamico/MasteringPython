# Capitulo 2 - Coleção de Sêquencias

## Tuplas

Tuplas têm dupla função: podem ser usadas como listas imutaveis e tambem como registros sem nomes de campos.

* Tuplas armazenam registros: 
Cada item da tupla armazena os dados de um campo e a posição do item na tupla confere o seu significado, por exemplo:

```python
lax_coordinates = (33.92,-118.408) # 1
city, year, pop, chg, area = ('Tokyo',2003,32450,0.66,8014) # 2
```

1) Latitude e Longitude;
2) Dados sobre Tokyo com posições especificas.

* Desempacotamento de tuplas:
O desempacotamento de tuplas funciona com qualquer objeto iterável, o único requisito é que o iterável gere exatamente um item por váriavel
na tupla receptora, a menos que você use um asterisco (*) para capturar os itens excedentes.

```python
lat, lon = (33.92,-118.408)
lat, _ = (33.92,-118.408)

divmod(20,8)
t = (20,8)
divmod(*t)

a,b, *rest = ('ola mundo','python','sequencial','paralela')
```

As vezes, quando estivermos interessados somente em determinadas partes de uma tupla ao fazer o desempacotamento, uma  váriavel descartável como _, poderá
ser usada para ocupar um lugar na tupla. Para mais de uma variavel descatável usamos o atributo *, seguido do nome qualquer.


* Tuplas nomeadas:
A função collections.namedtuple é uma fábrica (factory) que gera subclasses de tupla melhoradas com nomes de campos e um nome de classe

Dois parametros são necessarios para criar uma tupla nomeada: um nome de classe e uma lista de nomes de campo especificados como um interavel de strins ou como
uma unica string delimitada por espaços.

```python
from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP',36.933,(35.1321,139.8321))
print(tokyo)
tokyo.population
```

Uma tupla nomeada tem alguns atributos:
a)  _fields => mostra os nomes do campo;
b) _make() => permite instanciar uma tupla nomeada a partir de um iteravel; City(*nome) faria o mesmo;
c) _asdict() => retorna um OrderdDict criado a partir da instancia da tupla nomeada.


## Arrays

Se a lista contiver somente números, um array.array será mais eficiente que uma list: ele aceita todas as operações 
de sequências mutáveis, além de ter métodos adicionais para carregar e salvar rapidamente: .frombytes, .tofile

Ao criar um array, você deve fornecer um typecode (código de tipo), isto é, uma letra para determinar o tipo C
subjacente usado para armazenar cada item do array.


'b' -> signed char, tipo int, tamanho 1 byte
'l' -> unsigned inte, int, tamanho 4 bytes
'f' -> float, tamanho 4 bytes
'd' -> double, tamanho de 8 bytes

```python
from array import array
floats = array('d',(i for i in range(10**7)))

fp = open('flaots.bin',wb)
floats.tofile(fp)
fp.close()
```

## Deque:
A classe collections.deque é uma fila dupla thread-safe, criada para proprocionar inserção
e remoção rápidas de ambas as extremidades.

```python
from collections import deque
dq = deque(range(10),maxlen=10)

dq.rotate(3)

dq.appendleft(-1)

dq.extend([11,22,33])
```

Concatenar um deque que esteja cheio (len(d) == d.maxlen) faz com que os itens da outra extremidade
sejam descartados.
Deque é otimizado para inserção e remoção de itens das extremidades, porém remover itens do meio não
é tao rapido assim.