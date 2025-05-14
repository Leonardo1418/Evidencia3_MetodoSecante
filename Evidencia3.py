import math

def Evaluar_Funcion(Funcion, x):
    return eval(Funcion.replace("x", str(x)))

Funcion = input("Ingrese la funcion a evaluar:\n f(x) = ")
Funcion = Funcion.replace("^", "**").replace("e", str(math.e)).lower()

Error = False
i = 0
ter = 100

xl = float(input("Ingrese el valor de xl/xi-1:\n xl = "))
xu = float(input("Ingrese el valor de xu/xi:\n xu = "))
tol = float(input("Ingrese la tolerancia deseada (%):\n tol = "))

print(f'\nFuncion: f(x) = {Funcion}')
print(f'{"iteracion":<12} {"xl":<12} {"xu":<12} {"fxl":<12} {"fxu":<12} {"xr":<12} {"ter":<12}')
while ter > tol:
    fxl = Evaluar_Funcion(Funcion, xl)
    fxu = Evaluar_Funcion(Funcion, xu)

    xr = xu - ((fxu) * (xl-xu)) / (fxl-fxu)

    ter = abs((xu-xl) / xu) * 100

    print(f'{i:<12} {round(xl, 6):<12} {round(xu, 6):<12} {round(fxl, 6):<12} {round(fxu, 6):<12} {round(xr, 6):<12} {round(ter, 6) if Error==True else "-":<12}%')
    Error = True

    i +=1
    xl = xu
    xu = xr