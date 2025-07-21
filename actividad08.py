def factos(x):
    if x==1:
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
    nuevaPalabra = []
    if len(palabra)==1:
        return palabra[0]
    else:
        palabra.pop()
        return nuevaPalabra.append(invertir(palabra))

while True:
    print("1.Calcular el factorial de un numero.")
    print("2.Calcular la suma de sus numeros anteriores.")
    print("3.Calcular el fibonacci de un numero.")
    print("4.Calcular cuantas veces existe una letra en una palabra")
    print("5.Invertir una palabra.")
    print("6.Calcular la potencia de un numero.")
    print("7.SALIR")
    opcion = int(input("Seleccine una opcion: "))
    match opcion:
        case 1:
            n = int(input("Ingrese el numero para calcular el factorial: "))
            print(f"El factorial de {n} es: {factos(n)}")
        case 2:
            n = int(input("Ingrese el numero para calcular la suma de sus numeros anteriores: "))
            print(f"La suma hasta {n} es: {suma(n)}")
        case 3:
            n = int(input("Ingrese el numero para mostrar su fibonacci: "))
            print(f"El fibonaci de {n} es: {fibo(n)}")
        case 4:
            palabra = input("Ingrese la palabra: ")
            letra = input("Ingrese la letra que desea saber cuantas veces se repite: ")
        case 5:
            palabraInvertir = input("Ingrese la palabra para invertirla: ")
            palabraInvertir = palabraInvertir.split()
            print(invertir(palabraInvertir))
        case 6:
            base = int(input("Ingrese la base: "))
            exponente = int(input("Ingrese la exponente: "))
            print(f"El resultado de {base} a la {exponente} es: {potencia(base, exponente)}")
        case 7:
            print("Saliendo del programa")
            break