# MCOC-Proyecto-0

# Introducción
En este trabajo se mostrará el error producido por la pérdida de significancia debido al *.float32* y *.float64*

# Funcion Cuadrática
Aqui podemos ver que la funcion *x^2* pierde significancia, aumentando la negatividad de la potencia, es decir, mientras más decimales posea, mayor es el error.

Se implementaron y compararon:
1. Una solución exacta calculada a mano.
2. Una solución con *.float32*
3. Una solución con *.float64*

# Resultados

Se define el error relativo como:

```
error = resultados_float - resultados_exactos/resultados_exactos
```

Podemos ver que el error aumenta en mayor medida en el tipo *.float32* esto se debe a que no posee memoria suficiente par almacenar todos los decimales, entonces debe truncar o redondear su resultado, lo que genera una pequeña variación.



Output Consola:

```
Valores exactos:  [6.0516e-10, 1.39129e-11, 1.86624e-13] 

Valores float 64: 
[6.051600000000001e-10, 1.3912899999999999e-11, 1.86624e-13] 

Errores float 64: 
[1.7085989914919766e-16, 1.161215227517363e-16, 0.0] 

Valores float 32: 
[6.0516e-10, 1.39129e-11, 1.86624e-13] 

Errores float 32: 
[3.687517069682931e-08, 2.4846847363452724e-08, 2.4396648621704925e-08] 
