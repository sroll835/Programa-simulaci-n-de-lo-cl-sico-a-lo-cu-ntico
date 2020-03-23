import math

""" Libreria que realiza operaciones entre numeros complejos.

    La libreria soporta por lo menos las siguientes operaciones:
    
        1. Suma
        2. Producto
        3. Resta
        4. Division
        5. Modulo
        6. Conjugado
        7. Conversion entre representacion polar
        8. Retornar la fase de un número complejo
        9. Imprimir de forma a+bi - Forma complejo
        10. [a,b], n entrada y retorna (a+bi)^n
"""

def suma(a,b):
    
    """ Esta funcion retorna la suma de dos numeros complejos """
    
    suma = []
    suma.append((a[0]+b[0]))
    suma.append((a[1]+b[1]))
    return suma
    
    
def producto(a,b):

    """ Esta funcion retorna el producto de dos numeros complejos """

    producto = []
    producto.append((a[0]*b[0]-a[1]*b[1]))
    producto.append((a[0]*b[1]+a[1]*b[0]))
    return producto

def resta(a,b):

    """ Esta funcion retorna la resta de dos numeros complejos """

    resta = []
    resta.append((a[0]-b[0]))
    resta.append((a[1]-b[1]))
    return resta

def division(a,b):

    """ Esta funcion retorna la division de dos numeros complejos """

    division = []
    division.append(((a[0]*b[0]+a[1]*b[1])/(b[0]*b[0]+b[1]*b[1])))
    division.append(((a[1]*b[0]-a[0]*b[1])/(b[0]*b[0]+b[1]*b[1])))
    return division

def modulo(a):

    """ Esta funcion retorna el modulo de un numero complejo """

    modulo = []
    modulo.append(math.sqrt(a[0]**2+a[1]**2))
    return modulo

def conjugado(a):

    """ Esta funcion retorna el conjugado de un numero complejo """

    conjugado = []
    conjugado.append(a[0])
    conjugado.append(-1*a[1])
    return conjugado

def complejoAPolar(a):

    """ Esta funcion convierte un numero complejo a polar """

    aPolar = []
    aPolar.append(modulo(a))
    aPolar.append(math.atan(a[1]/a[0]))
    return aPolar

def polarAComplejo(c):

    """Esta funcion convierte un numero polar a complejo """

    complejo = []
    a = c[0]*math.cos(math.radians(c[1]))
    b = c[0]*math.sin(math.radians(c[1]))
    complejo.append(round(a,2))
    complejo.append(round(b,2))
    return complejo
    

def fase(a):

    """ Esta funcion calcula la fase de un numero complejo """

    fase = []
    fase.append(math.atan((a[1]/a[0]))*(180/math.pi))
    return fase

def imprimir(c):

    """ Esta funcion imprime un numero complejo de la forma a+bi """

    print("El numero es:",str(c[0]),"+",str(c[1])+"i")

def potencia(c,n):
    
    """ Esta funcion calcula c**n, siendo c un numero complejo """
    
    potencia = []
    polar = complejoAPolar(c)
    complejo = polarAComplejo([round(polar[0]**n,2),round(polar[1]*n,2)])
    return complejo

def sumaVectores(a,b):
    """ Esta funcion calcula la suma entre dos vectores """
    
    if len(a) != len(b):
        return " No es posible calcular esta operacion "
    
    suma  = []
    
    for i in range(len(a)):
        suma.append(suma(a[i],b[i]))
        
    return suma     



def restaVectores(a,b):
    
    """ Esta funcion calcula la resta entre dos vectores """
    
    if len(a) != len(b):
        return " No es posible calcular esta operacion "
    
    resta = []
    
    for i in range(len(a)):
        resta.append(resta(a[i],b[i]))
        
    return resta

def productoInternoVectores(a,b):

    """ Se ingresan 2 vectores complejos de longitud n, retorna el producto interno entre estos """

    if len(a) != len(b):
        return " No es posible calcular esta operacion "
    
    producto = (0,0)
    
    for i in range(len(a)): 
        producto = suma(producto,multiplicacion(a[i],b[i]))
        
    return producto;

def sumaMatricesComplejas(a,b):
    
    """ ingresan 2 matrices de M x N, retorna la resta de cada matriz compleja. """
    
    if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
        return " No es posible calcular esta operacion "
    
    val = []
    
    for i in range(len(a)):
        val.append(sumaVectores(a[i],b[i]))
        
    return val

def moduloVector(a):
    
    """ Esta funcion calcula el modulo de un vector """
    
    mod = 0
    for i in a:
       mod += modulo(i)**2
       
    return round(mod**0.5,3)

def matrizInversa(a):
    
    """ Calcula la daga de una matriz """
    
    inversa = []
    
    for i in range(len(a)):
        fila = []
        for j in range (len(a[0])):
            fila.append(multiplicacion((-1,0),a[i][j]))
        inversa.append(fila)
        
    return inversa

def matrizAdjunta(a):
    
    """ Calcula la matriz adjunta """
    
    return matrizTranspuesta(matrizConjugada(a))

def matrizConjugada(a):
    
    """ Calcula la matriz conjugada de una matriz de complejos """
    
    conjugada = []
    
    for i in range(len(a)):
        fila = []
        for j in range(len(a[0])):
            fila.append(conjugado(a[i][j]))
        conjugada.append(fila)
        
    return conjugada

def normaMatriz(matriz):

    """ Esta funcion calcula la norma de una matriz """
    
    return round(math.sqrt(productoInternoMatrices(matriz,matriz)),3)

def productoInternoMatrices(a,b):
    
    adjunta = matrizAdjunta(a)
    producto = multiplicacionMatrices(adjunta,b)
    pInterno = (0,0)
    
    for i in range(len (producto)):
        pInterno = suma(pInterno,producto[i][i])
        
    return modulo(pInterno)

def multiplicacionMatrices(a,b):

    """ Esta funcion calcula la multiplicacion de dos matrices y retorna la matriz resultante """

    if len(b) == len(a[0]):
        
        matriz = [[[0, 0]] * len(b[0]) for x in range(len(a))]
        
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):          
                    m = producto(a[i][k], b[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = [m[0]+n[0], m[1]+n[1]]
                    
        return matriz
    
    else:
        
        raise "No se puede realizar esta operacion"

def matrizTranspuesta(matriz):
                           
    """ Esta funcion calcula la matriz transpuesta de una matriz dada y la retorna """
                           
    transpuesta = []
                           
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)
                           
    return transpuesta

def inversoAditivo(a):
                           
    """ Calcula el inverso aditvo de un vector dado y lo retorna """
                           
    for i in range (len(a)):
        for j in range (len(a[i])):
            a[i][j] = -1*a[i][j]
        
    return a

def sumaMatricesComplejas(a,b):
                           
   """ Esta funcion calcula la suma entre dos matrices y la retorna como una matriz"""

   if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
        return "No se puede realizar la operacion"
   suma = []
                           
   for i in range(len(a)):
        suma.append(sumaVectores(a[i],b[i]))

   return suma

def prod_tensor(mc_1, mc_2):
    """
    La función recibe 2 matrices de números complejos (sin importar sus tamaños) y retorna su producto tensor.
    """
    rta = crear_matriz1(len(mc_1)*len(mc_2), len(mc_1[0])*len(mc_2[0]))
    
    for i in range(len(rta)):
        for j in range(len(rta[0])):
            rta[i][j] = producto(mc_1[i//len(mc_2)][j//len(mc_2[0])], mc_2[i%len(mc_2)][j%len(mc_2[0])])
    return rta

def crear_matriz1(filas, columnas):
    """
    La función recibe el número de filas y el número de columnas e inicializa una matriz compuesta de ceros, es decir, de la siguente manera: [0,0].
    """
    matriz = []
    for i in range(filas):
        matriz.append([[0,0]] * columnas)
    return matriz

def moduloAlCuadrado(v):
    """ Calcula el modula al cuadrado de un vector """
    
    vector = []
    for i in v:
        vector.append([[round(pow(i[0][0],2)+pow(i[0][1],2),3),0]])

    return vector

def main():
    
    v = [[[0,0]],
     [[0,0]],
     [[1,0]],
     [[0,0]],
     [[0,0]],
     [[0,0]]]
    
    matriz = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
              [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
              [[0,0],[1,0],[0,0],[0,0],[0,0],[1,0]],
              [[0,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
              [[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
              [[1,0],[0,0],[0,0],[0,0],[1,0],[0,0]]]


    v = [[[-1/math.sqrt(8),1/math.sqrt(8)]],
         [[1/math.sqrt(8),-1/math.sqrt(8)]],
         [[0,0]],
         [[0,1/math.sqrt(2)]]]

    matriz = [[[0,0],[1/math.sqrt(2),0],[1/math.sqrt(2),0],[0,0]],
              [[1/math.sqrt(2),0],[0,0],[0,0],[-1/math.sqrt(2),0]],
              [[1/math.sqrt(2),0],[1,0],[0,0],[1/math.sqrt(2),0]],
              [[0,0],[-1/math.sqrt(2),0],[1/math.sqrt(2),0],[1,0]]]
    
    v = [[[0,0]],
         [[0,1]],
         [[0,0]],
         [[0,0]]]

    m = [[[7/34,0],[14/34,0],[4/34,0],[9/34,0]],
         [[15/34,0],[6/34,0],[12/34,0],[1/34,0]],
         [[2/34,0],[3/34,0],[13/34,0],[16/34,0]],
         [[10/34,0],[11/34,0],[5/34,0],[8/34,0]]]

    n = [[[0,0],[0.61,0],[0.39,0]],
         [[0.5,0],[0.09,0],[0.41,0]],
         [[0.5,0],[0.3,0],[0.2,0]]]

    print(len(prod_tensor(m,n)),len(prod_tensor(m,n)[0]))
    
    vectorM = [[[0,0]],
               [[0,0]],
               [[0,0]],
               [[1,0]]]
    
    vectorN = [[[0,0]],
               [[1,0]],
               [[0,0]]]

    print(prod_tensor(vectorM,vectorN))
    print(len(prod_tensor(vectorM,vectorN)),len(prod_tensor(vectorM,vectorN)[0]))
    
main()


    
    
    
