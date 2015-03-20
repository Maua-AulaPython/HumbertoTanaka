a=0
soma=0
media=0
b=1
while b>0 :
    c=float(raw_input("digite uma nota = "))
    if c>0:
        a+=1
        soma+= c
    else:
        b=0
media = soma/a
print 'media =' , media
    

        
