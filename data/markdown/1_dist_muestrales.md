```
#EN EL SCRIPT BASTA CON PONER UNA VEZ LAS LIBRERÍAS EN LA CABECERA
library(Rcmdr)
#para el que quiera utilizar R-Commander (incluye librerías por defecto)
library(nortest)#para poder hacer contrastes avanzados de normalidad
#SI NO CARGAS Rcmdr se incluyen estas librerías en la cabecera
library(MASS)
library(car)
#a
pnorm(53, 50, 2)-pnorm(47, 50,2)
#b
pchisq(144.5*35/12^2,35)
```
# 1 Distribuciones muestrales

Este apartado tiene como objetivo:

- Aprender los comandos básicos de R para el cálculo de probabilidades (probabilidad acumulada, percentiles, gráficos de densidad, probabilidades en valores discretos)
- Repasar esquema pg7 de la presentación de teoría: Teorema central del límite y chi-cuadrado.

***Ejercicio 1***. Se toma una muestra aleatoria de 36 observaciones de una distribución de media 50 y desviación estándar 12 que representa el peso de una raza de perros.

1. Calcula la probabilidad de que la media muestral tome valores entre 47 y 53
2. Asumiendo la normalidad de la variable en estudio, calcula la probabilidad de que la varianza muestral tome un valor inferior a 144.5

**Solución**

La forma habitual de trabajar una sesión de RStudio es mediante un Script (una hoja en blanco donde de forma ordenada se van escribiendo los comandos. Resultamente un documento puramente de programación donde los comentarios se introducen con almohadilla (#) para que no sean compilados. La manera en que visualizas las prácticas mezcla texto con código, es un Markdown que es un documento para realizar presentaciones e informes.

Abre un Script desde File: New File, y copia el siguiente código

*Aviso*: los exámenes son escritos, R es una herramienta imprescindible para resolverlos pero NO se considera una solución escribir la orden de R utilizada. Solo se valorarán ejercicios que expliquen el razonamiento seguido y que utilicen R como accesorio para realizar cálculos. El ejercicio anterior, para que sea válido en un examen, debe escribirse de manera desarrollada. Por ejemplo, como sigue a continuación

1. Consideramos la variable 

1. Se plantea un probabilidad para el estadístico varianza muestral, 

***Ejercicio 2***.Comprobación, mediante simulación, de los resultados de distribuciones muestrales.

Generamos 300 muestras de tamaño 5 de una población normal de media 8 y desviación típica 3. Guarda la media y la desviación típica de cada muestra. Posteriormente comprueba, mediante los gráficos qqplot, que 

```
set.seed(50) #fija la semilla de la simulación para que todos tengamos el mismo resultado del azar
data<-as.data.frame(matrix(rnorm(300*5, 8,3),300,5))#genera 300 filas, muestras, con 5 columnas
mean<-rowMeans(data)#calcula en cada fila la media, se podría poner apply(data,1, mean)
S<-apply(data[,1:5], 1,sd)#calcula en cada fila, por eso el 1, la desviación típica
estad1<-sqrt(5)*(mean-8)/3
estad2<-sqrt(5)*(mean-8)/S
#x11()
library(car)
par(mfrow=c(2,2))
qqPlot( estad1, dist="norm", id=FALSE)
qqPlot( estad1, dist="t",df=4, id=FALSE)
qqPlot( estad2, dist="t",df=4, id=FALSE)
qqPlot( estad2, dist="norm", id=FALSE)
```