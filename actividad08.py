def factos(x):
    if x==1
        return 1
    else:
        return x * factos(x-1)
def fibo(x):
    if x==1:
        return 1
    else:
        return fibo(x-2)+fibo(x-1)
def suma(x):
    if x==0:
        return 0
    else:
        return x+suma(x-1)
def potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base*potencia(base, exponente-1)
def invertir(palabra):
    if len(palabra)==1:
        return palabra[0]
    else:
        nuevaPalabra = []
        return nuevaPalabra.append(invertir(palabra.pop()))
