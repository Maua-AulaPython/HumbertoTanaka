import sys
notas = []
n=0

while n>=0:
    while True:
        try:
            n = int(raw_input("digite a nota: "))
            break
        except:
            print "vc n digitou um numero valido"
    notas.append(n)
        
notas.remove(-1)   

soma = 0
for i in notas:
    soma =soma + i

if len(notas):
    print 'Media = ',soma/len(notas)
    print 'Maior Nota = ', max(notas)


        
