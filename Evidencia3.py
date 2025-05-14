import math

Funcion = input("Ingrese la funcion a evaluar:\n f(x) = ")
Funcion = Funcion.replace("^", "**")
Funcion = Funcion.replace("e", str(math.e))
Funcion = Funcion.lower()
Error = False
i = 0
Bucle = 0
ter = 100

xl = float(input("Ingrese el valor de xl/xi-1:\n xl = "))
xu = float(input("Ingrese el valor de xu/xi:\n xu = "))

tol = float(input("Ingrese la tolerancia deseada (%):\n tol = "))

print(f'\nFuncion: f(x) = {Funcion}')
print(f'{"iteracion":<10} {"xl":<10} {"xu":<10} {"fxl":<10} {"fxu":<10} {"xr":<10} {"ter":<10}')
while tol<ter:
    fxl = eval(Funcion.replace("x", str(xl)))
    fxu = eval(Funcion.replace("x", str(xu)))

    xr = xu-((fxu)*(xl-xu))/(fxl-fxu)

    ter = abs((xu-xl)/xu)

    print(f'{i:<10} {round(xl, 2):<10} {round(xu, 2):<10} {round(fxl, 2):<10} {round(fxu, 2):<10} {round(xr, 2):<10} {round(ter*100, 2) if Error==True else "-":<10}')
    Error = True

    xl = xu
    xu = xr

    i += 1

if ter<=tol:
    fxl = eval(Funcion.replace("x", str(xl)))
    fxu = eval(Funcion.replace("x", str(xu)))

    xr = xu-((fxu)*(xl-xu))/(fxl-fxu)

    ter = abs((xu-xl)/xu)

    print(f'{i:<10} {round(xl, 2):<10} {round(xu, 2):<10} {round(fxl, 2):<10} {round(fxu, 2):<10} {round(xr, 2):<10} {round(ter*100, 2) if Error==True else "-":<10}')