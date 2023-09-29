from math import pi

a:int = int(input('"a" oldal hossza (cm): '))
b:int = int(input('"b" oldal hossza (cm): '))
print(f'téglalap kerülete: {2*(a+b)} cm')
print(f'téglalap területe: {a*b} cm^2')
# -------------------------------------------
r:int = int(input('kör sugarának hossza (cm): '))
print(f'kör kerülete: {2*r*pi} cm')
print(f'kör területe: {r**2*pi} cm^2')
# -------------------------------------------
a:int = int(input('"a" oldal hossza (cm): '))
b:int = int(input('"b" oldal hossza (cm): '))
c:int = int(input('"c" oldal hossza (cm): '))
k:int = a + b + c
print(f'háromszög kerülete: {k} cm')
s:float = k/2
t:float = (s * (s-a) * (s-b) * (s-c)) ** .5
print(f'háromszög területe: {t} cm^2')
