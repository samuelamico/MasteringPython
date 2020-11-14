from collections import namedtuple


# ListComprehensions:
titulo = 'smartphones'
empresas = ['Xiomi','Nokia','Apple','Samsung']
cores = ['preto','azul','branco']

letras_titulo = [letra for letra in titulo]
print(letras_titulo)

## Produto Cartesiano
celulares = [(marca,cor) for marca in empresas for cor in cores]
print(celulares)

# Expressoes Geradoras -- ela economiza memoria:
tuple_celulares = tuple(letra for letra in titulo)

for celulares in ((marca,cor) for marca in empresas for cor in cores):
    print(celulares) ### -----> A expressao geradora gera intens um por um, economizando espaço na memoria <-------

print("\n")
# Tuplas como registros:
info_cidade = ('Brasil','RN','Natal','Lagoa Nova','Av. Miguel Castro')
pais,estado,*rest = info_cidade
print(f"Pais = {pais} e Estado = {estado} e Resto = {rest}")

# Tuplas nomeadas
City = namedtuple('City','country state city district avenue')
meu_lar = City(*info_cidade)
print(meu_lar)
print(f"País do meu lar = {meu_lar.country}")

## Atributos e Metodos:
print(meu_lar._fields)

info_floripa = ('Brasil','SC','Florianopolis','Trindade','Rua Lauro Linhares')
meu_lar2 = City._make(info_floripa)
print(meu_lar2._asdict())

#### _fields, _make(), _asdict()