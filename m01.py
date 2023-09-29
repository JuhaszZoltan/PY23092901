vezeteknev:str = input('írd be a vezetekneved: ')
keresztnev:str = input('írd be a keresztneved: ')
print(f'{vezeteknev} {keresztnev}')
print(f'{keresztnev} {vezeteknev}')
# -----------------------------------------------
szam:int = int(input('írj be egy számot: '))
print(f'előző szám: {szam - 1}')
print(f'következő szám: {szam + 1}')
# -----------------------------------------------
n01:int = int(input('egyik szám: '))
n02:int = int(input('másik szám: '))
print(f'{n01} + {n02} = {n01 + n02}')
print(f'{n01} - {n02} = {n01 - n02}')
print(f'{n01} * {n02} = {n01 * n02}')
print(f'{n01} / {n02} = {n01 / n02}')
# -----------------------------------------------
a:int = int(input('"a" értéke: '))
b:int = int(input('"b" értéke: '))
c:int = 2*a + 3*b
d:int = c - 2*a - 3*b
print(f'"c" értéke: {c}')
print(f'"d" értéke: {d}')