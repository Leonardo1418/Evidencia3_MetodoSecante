Funcion = "x^2 - 4"
Funcion = Funcion.replace("^", "**")
Error = False

xl = 1.5
xu = 2.5

fxl = eval(Funcion.replace("x", str(xl)))
fxu = eval(Funcion.replace("x", str(xu)))

xr = xu-((fxu)*(xl-xu))/(fxl-fxu)

print("fxl: ", fxl)
print("fxu: ", fxu)
print("xr: ", xr)

ter = abs((xr-xu)/xr)

print("ter: ", ter)



