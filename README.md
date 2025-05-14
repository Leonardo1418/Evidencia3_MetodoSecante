# METODO DE LA SECANTE MEDIANTE PYTHON
Este programa implementa el ***Metodo de la secante*** para encontrar las raices de una funcion no lineal, dadas dos estimaciones iniciales

## FUNCIONAMIENTO
- Se inserta la funcion, estimaciones iniciales y tolerancia deseada
- Mediante la funcion integrada ***eval*** de python se evalua la funcion con las estimaciones seleccionadas
- Se calcula *xr* mediante la formula de la secante: $x_r = x_u - \frac{f(x_u) \cdot (x_l - x_u)}{f(x_l) - f(x_u)}$
- Se calcula la tasa de error con la formula: $TER = \left| \frac{x_u - x_l}{x_u} \right| \times 100$ siendo multiplicada por 100 para dar el resultado como porcentaje
- Se muestra como forma de tabla cada iteracion, la cual cada una muestra los valores de *xl*, *xu*, *f(xl)*, *f(xu)*, *xr* y *ter(Tasa de error)*
- Se continuan haciendo iteraciones hasta que la tasa de error sea menor a la tolerancia deseada

## EJEMPLO DE USO
#### Proporciona los valores
- ##### **Ingrese la funcion a evaluar:**
  f(x) = e^-x -x
- ##### **Ingrese el valor de xl/xi-1:**
  xl = 0
- ##### **Ingrese el valor de xu/xi:**
  xu = 1
- ##### **Ingrese la tolerancia deseada (%):**
  tol = 0.01
  
#### Resultado de la ejecución
**El programa imprimirá un resumen de las iteraciones realizadas y el resultado final:**

Funcion: f(x) = 2.718281828459045**-x -x
| Iteración | xl       | xu       | fxl       | fxu       | xr       | ter       |
| --------- | -------- | -------- | --------- | --------- | -------- | --------- |
| 0         | 0.0      | 1.0      | 1.0       | -0.632121 | 0.6127   | -         |
| 1         | 1.0      | 0.6127   | -0.632121 | -0.070814 | 0.563838 | 63.212056 |
| 2         | 0.6127   | 0.563838 | -0.070814 | 0.005182  | 0.56717  | 8.66586   |
| 3         | 0.563838 | 0.56717  | 0.005182  | -4.2e-05  | 0.567143 | 0.587472  |
| 4         | 0.56717  | 0.567143 | -4.2e-05  | -0.0      | 0.567143 | 0.00477   |
