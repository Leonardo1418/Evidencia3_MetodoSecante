import math

#Evaluar la funcion remplazando x por el valor de la variable x
def Evaluar_Funcion(Funcion, x):
    return eval(Funcion.replace("x", str(x)))

#Entrada de la funcion y remplazo a posibles valores insertados dentro de la misma, como "e" por el valor de euler o "^" por "**" para que funcione el eval
Funcion = input("Ingrese la funcion a evaluar:\n f(x) = ")
Funcion = Funcion.replace("^", "**").replace("e", str(math.e)).lower()

#Inicializacion de variables para las iteraciones
Error = False
i = 0
ter = 100

#Entrada de Valores iniciales xi-1, xi y tolerancia deseada
xl = float(input("Ingrese el valor de xl/xi-1:\n xl = "))
xu = float(input("Ingrese el valor de xu/xi:\n xu = "))
tol = float(input("Ingrese la tolerancia deseada (%):\n tol = "))

#Impresion en formato de tabla las iteracines hechas mediante el metodo de la secante
print(f'\nFuncion: f(x) = {Funcion}')
print(f'{"iteracion":<12} {"xl":<12} {"xu":<12} {"fxl":<12} {"fxu":<12} {"xr":<12} {"ter":<12}')
while ter > tol:
    #Funcion convertida con los valores de xl y xu
    fxl = Evaluar_Funcion(Funcion, xl)
    fxu = Evaluar_Funcion(Funcion, xu)

    #Creacion y calculo de la variable xr o xi+1 
    xr = xu - ((fxu) * (xl-xu)) / (fxl-fxu)

    #Calculo de la tasa de error
    ter = abs((xu-xl) / xu) * 100

    #Impresion de los resultados dados en su respectiva iteracion
    print(f'{i:<12} {round(xl, 6):<12} {round(xu, 6):<12} {round(fxl, 6):<12} {round(fxu, 6):<12} {round(xr, 6):<12} {round(ter, 6) if Error==True else "-":<12}%')
    #Booleano de error para no mostrar la tasa de error en la primera iteracion
    Error = True

    #Aumento de i y asignacion de nuevos valores a xl/xi-1 y xu/xi para la siguiente iteracion
    i +=1
    xl = xu
    xu = xr