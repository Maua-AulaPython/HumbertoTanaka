##--------Exercicio 1---------##
import math

def distancia(P1x,P1y,P2x,P2y):
    d = math.sqrt(math.pow((P2x-P1x),2)+math.pow((P2y-P1y),2))
    print 'd = ',d
    return d
    
##--------Exercicio 2----------##

def M_dist():
    x=[]
    y=[]
    b=0
    print 'Informe o numero de pontos'
    n = int(raw_input())
    if(n>0):
        print 'informe as abcissas dos pontos'
        for i in range(1,n+1):
            z=float(raw_input())
            x.append(z)
        print 'informe as ordenadas dos pontos'
        for j in range(1,n+1):
            z=float(raw_input())
            y.append(z)
        for k in range(1,n+1):
            for l in range(1,n+1):
                d=distancia(x[k-1],y[k-1],x[l-1],y[l-1])
                if(d>b):
                    b=d
    return b

##--------Exercicio 3----------##

def Polar(P1x,P1y,P2x,P2y):
    d1 = distancia(0,0,P1x,P1y)
    d2 = distancia(0,0,P2x,P2y)
    a1 = math.degrees(math.atan2(float(P1y), float(P1x)))
    a2 = math.degrees(math.atan2(float(P2y), float(P2x)))
    print 'Ponto 1: (',d1,',',a1,')' 
    print 'Ponto 2: (',d2,',',a2,')'

##--------Exercicio 4----------##

def triangulo(a,b,c):
    if(c^2!=a^2+b^2):
        print 'os valores ',a,', ',b,' e ',c,'nao formam um triangulo retangulo'
    else:
        s=float(a*b)/2
        print 'A area desse triangulo e: ',s,' u.a.'


##--------Exercicio 5----------##

def GPS():
    print 'Digite as coordenadas geograficas x, y e z'
    x=float(raw_input())
    y=float(raw_input())
    z=float(raw_input())
    a=6378160
    e=0.00669454185
    lamb= math.atan2(y,x)
    p=math.sqrt(math.fabs(math.pow(x,2)+math.pow(y,2)))
    h=0
    n=1
    oi=z/(p*(1-e*n/(n+h)))
    teta=math.atan(oi)
    for i in range(1,5):
        n=float(a)/math.sqrt(1-e*math.pow(math.sin(teta),2))
        h=float(p)/math.cos(teta)-n
        oi=float(z)/(p*(1-e*n/(n+h)))
        teta=math.atan(oi)
    ra=math.degrees(teta)
    rb=math.degrees(lamb)
    print 'Latitude: ',rb,' graus'
    print 'Longitude: ',ra,' graus'
    print 'Altitude: ',1000*h,'m'

















        
