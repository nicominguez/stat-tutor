# Capítulo 1 Estadística Paramétrica y No Paramétrica

Este primer tema de la asignatura presenta una gran cantidad de técnicas estadísticas que sirven para responder a las cuestiones más habituales que se plantean a la vista de una base de datos en cualquier disciplina.

Es importante señalar que estas técnicas no son apropiadas para:

- Datos de corte longitudinal: observaciones de una variable en un individuo a intervalos regulares de tiempo.
- Grandes tamaños muestrales
- Relaciones que implican a más de dos variables: análisis multivariante
- Modelización estadística: relaciones entre variables para explicar fenómenos y obtener predicciones.

## 1.1 Conceptos de repaso

La inferencia estadística es el conjunto de métodos, técnicas y herramientas utilizadas para extraer conclusiones sobre toda la población a partir de los datos.

En Estadística I se aprendió el procedimiento básico seguido en los estudios inferenciales. Este procedimiento responde al siguiente esquema:

El esquema anterior establece una notación que mantendremos en el resto del tema: representa el tamaño muestral y es la observación de la variable en el individuo de la muestra. Aunque la rapidez del lenguaje lo dificulta, es conveniente no confundir en las explicaciones el concepto de muestra con el de observaciones de la muestra .

La manera de extraer la muestra es determinante en el estudio futuro. El muestreo básico se denomina **muestreo aleatorio simple** (m.a.s), es decir, se supone accesible cada individuo de la población (o universo) y cada individuo es igualmente probable de ser seleccionado. El m.a.s equivale a la situación en que cada individuo de la población se identifica con una bola de una urna y de esta urna se extraen  bolas (con o sin reemplazamiento). Si el tamaño de la población  es muy grande, es indistinto que el muestreo se haga con o sin reemplazamiento. En este tema asumimos valores de  grandes.

En la práctica, especialmente en el plano científico (ingeniería, agronomía, química, física, biología, geología, etc), la observaciones se obtienen mediante experimentación. Para encajar la experimentación en el esquema propuesto en la Fig. 1 debemos identificar cada individuo con un experimento. Observemos que la población son todos los potenciales experimentos que podríamos realizar, pero son solo los que hemos llevado a cabo en el laboratorio.

Para facilitar la explicación, supondremos en el resto de la sección que la característica de interés o variable estadística  es cuantitativa. Las observaciones de la muestra se resumen mediante un **estadístico** que es una función de las observaciones. Los estadísticos que fueron estudiados el curso pasado fueron, esencialmente, dos: la media  y la varianza muestral  cuyas fórmula recordamos:


Puesto que el azar interviene en la elección de individuos que conforman la muestra, las observaciones muestrales cambiarían ante un nuevo muestreo. En consecuencia, el valor de un estadístico es una variable aleatoria que para cada muestra toma un valor que es de esperar que vaya cambiando. Ahora bien, el hecho de que hagamos un m.a.s permite obtener resultados claves para la inferencia estadística. Los recopilamos en el siguiente esquema:

Con objeto de entender la relevancia de un estadístico y su distribución, tomamos como ejemplo la media muestral . Si reflexionamos sobre su uso en Estadística I podemos destacar tres usos relevantes de la media que giran en torno a conocer el valor de que es la media poblacional (en la fórmula el sumatorio sería sobre las observaciones de toda la población, sumandos y no como sucede en la media muestral):

1. Sirve para estimar (aproximar) el valor de la media poblacional . Cuando un estadístico se utiliza con objeto de estimar un parámetro concreto pasa a denominarse estimador del parámetro. En concreto la **media muestral** es un**estimador de** y entonces se puede escribir .
2. Con el uso de las distribuciones en el muestreo podemos proporcionar un intervalo en el que con una confianza (generalmente 0.95) se encuentra el valor desconocido . Un intervalo de confianza se escribe como sigue:


Si es un requisito imprescindible para que el intervalo de confianza tenga sustento teórico que . La razón es que el Teorema Central del Límite no se puede aplicar y, entonces, no se puede garantizar que tenga una distribución normal. Cuando en lugar de se puede escribir pues la distribución se aproxima a conforme crece (ver el tercer ejercicio resuelto).

En este curso representa el percentil de la distribucion . Es conveniente memorizar estos valores y que se corresponden, respectivamente, con los grados de confianza 0.9 y 0.95. Esta notación es análoga para el resto de distribuciones que utilicemos, como , , etc.

En la expresión de un intervalo confianza aparecen dos errores que siempre están presentes en los estudios estadísticos y que son inevitables por el hecho de que el AZAR sea quien establece en última instancia los valores que toma la muestra:

1. Nivel de confianza: . Nos indica que la técnica de construcción del intervalo de confianza captura el valor en el de las muestras de tamaño . Implícitamente nos está indicando que la técnica proporciona un intervalo de confianza que no captura a en el de las muestras, lo que mide el error en términos de probabilidad.
2. Margen de error: . Es una medida de la precisión con la que podemos estimar , implícitamente, cuanto mayor es su valor más imprecisa es la información del intervalo. Observa que un aumento del tamaño muestral mejora la precisión aunque esto supone una mayor inversión en la experimentación o en el muestreo. Un descenso del nivel de confianza también la mejora, pero no es deseable. El único elemento que no es controlable por el investigador procede de variabilidad de la variable () que, si es alta, necesariamente influirá en la imprecisión de las estimaciones
3. Contrastes de hipótesis: resuelven cuestiones concretas sobre . Se denomina hipótesis alternativa () a la que refleja la propuesta del investigador, si hay evidencias muestrales para aceptar entonces el contraste es **significativo** . Por ejemplo, si el investigador sospecha que el valor  toma un valor inferior a  escribirá:


Este curso nos interesa estimar otros parámetros además de ,  y . Por esa razón, lo que hemos escrito arriba para  y  se debe generalizar con otra notación. De modo general diremos que queremos estimar un **parámetro** de interés  con un **estimador**, que es una función de las observaciones de la muestra, . Buscaremos una distribución de probabilidad para  para obtener intervalos de confianza y plantear contrastes de hipótesis.

Resolvemos algún ejercicio para ilustrar los conceptos anteriores que son los ejercicios del bloque III del curso de Estadística I.

### 1.1.1 Ejercicios modelo

**Ejercicio 1: Distribuciones en el muestreo**

Este ejercicio aplica todos los resultados recogidos en el esquema de distribuciones en el muestreo de la Fig2.

Se toma una muestra aleatoria de 36 observaciones de una variable aleatoria con distribución de media 50 y desviación estándar 12.

1. Calcula la probabilidad de que la media muestral tome valores entre 47 y 53
2. Asumiendo la normalidad de la variable en estudio, calcula la probabilidad de que la varianza muestral tome un valor inferior a 144.5
3. Supongamos que se toman 1000 muestras de tamaño 36 de la variable de interés. Calcula la probabilidad de que al menos el 30% de las muestras tenga un media superior a 51.
4. Si el valor de la media muestral fuera 53 ¿podrías decir que la muestra es anómala?[Suponemos anómalos los datos de las colas con peso 0.025].

**Solución Ejercicio 1.**

Comentarios al enunciado. Observa que de una población se hace un m.a.s de tamaño . No nos dicen cuáles son las observaciones muestrales, pero sí sabemos que la variable que se observa tiene y .

1. Trasladamos el enunciado a notación matemática y tenemos que se nos pide . Se puede eliminar el subíndice 36 de la expresión de la media muestral porque no va a haber confusión en la resolución del ejercicio. La distribución de es desconocida, pero el tamaño muestral es mayor que 30, por lo que el Teorema Central de Límite nos indica que .

```
solu<-pnorm(53, mean=50, sd=2, lower.tail=TRUE)-pnorm(47, mean=50, sd=2, lower.tail=TRUE)
print(c(solu))
```
`## [1] 0.8663856`
1. En este apartado asumimos y se nos pide . Puesto que es normal, a la vista del esquema de Fig2, disponemos de una distribución para que nos permitirá resolver la probabilidad. Antes multiplicamos por con lo que se tiene que , finalmente


`## [1] 0.5374821`
1. Para cada una de las mil muestras seleccionados observamos la variable : ser que es una variable binaria. Observamos que y el enunciado plantea . Como el tamaño muestral es 1000 y la variables de interés es binaria, por el TCL, ver Fig2, la proporción muestral, es normal de media y desviación , por lo que

`## [1] 0.7145297`
1. Si la media muestral fuera de 53, tendríamos que , es decir, hay un 6,6% de muestras que proporcionarían un valor superior a 53.

Que un valor sea anómalo requiere un contexto. Habitualmente se consideran anómalos valores poco frecuentes, en el caso de la normal son valores que se encuentran en las colas de la distribución. Si fijamos el criterio habitual de que son anómalos el 5% de valores en las colas (2,5% de valores en cada cola inferior y superior), el valor 53 claramente no se encuentra en ninguna de las colas, por lo que no es anómalo.

En la práctica, para estudiar la anomalía con observaciones que proceden de una normal, se tipifica el valor, en este caso, ; como la cola superior con masa 0.025 comienza en 1.96 (valor que conviene memorizar) decidimos que no es anómalo según el criterio establecido.

**Ejercicio 2: Inferencia a partir de la media muestral**

En este ejercicio repasamos la inferencia sobre la media y varianza de una variable. El objetivo, además de recordar conceptos, es mostrar cómo se resuelve el procedimiento con las órdenes de R.

En un instituto de investigaciones dermatológicas se está investigando una afección cutánea de tipo cancerígeno. Se eligen 40 ratas de una misma raza aleatoriamente y se les provoca el cáncer, a continuación se les frota con un medicamento. Se toma como variable respuesta el número de horas que tarda el cáncer en desaparecer. Se obtiene una media muestral de 100 horas y un desviación típica muestral de 10 horas. Responde a las siguientes cuestiones referidas al enunciado anterior (los datos que se indican en cada apartado no se mantienen en los posteriores). Indica en qué apartados requieres la hipótesis de normalidad para resolverlos.

2.1 Calcula un intervalo de confianza al 90% para la media de la variable respuesta.

2.2 Si se supiera que horas, obtén un intervalo de cofianza al 99% para la media de la variable respuesta.

2.3 Si el tamaño muestral fuera en lugar de 40, calcula el intervalo de confianza al 90% de la media de la variable respuesta.

2.4 Se tiene la sospecha de que la media es menor que 105 horas, ¿es significativo el contraste al 5%?

2.5 Obtén un intervalo de confianza al 90% para la varianza de la variable respuesta.

2.6 Contrasta la hipótesis .

**Solución Ejercicio 2**

El curso pasado se resolvían estos ejercicios de manera constructiva con objeto de dominar la técnica. Este curso ya se presupone ese dominio de las herramientas de intervalos y contrastes, por lo que se valora su uso apropiado en un contexto donde se plantean cuestiones de investigación tras la recogida de datos.

En consecuencia, este ejercicio no es propio de este curso porque no hay datos que permitan resolverlo a partir de los comandos adecuados de R y no entra en un contexto con un objetivo de preguntas de investigación. No obstante, vamos a aprovecharlo para recalcar un mensaje importante que hay en la teoría y es que solo hay una sola fórmula para intervalos y contrastes de la media y cuya estructura se repite en la mayor parte de estadísticos cuya fórmula promedia los observaciones de la muestra:

Donde representa los grados de libertad de la t-student que, generalmente, es un valor muy relacionado con el tamaño muestral y que es una estimación de la variabilidad del estadístico .

La expresión anterior es muy general, pero iremos viendo en el curso que se ajusta a muchos intervalos de confianza de nuevos parámetros que se estudiarán. Volviendo a la media, la expresión anterior toma valores que sí que nos resultan familiares:


Este ejercicio, por tanto, lo realizaremos tratando de extraer aspectos teóricos de utilidad para el resto del curso y sin métodos contructivos. Debemos aplicar la fórmula adecuadamente y señalar las condiciones teóricas que se requieren.

Del enunciado tenemos que la muestra tiene tamaño , la variable que se observa en los individuos es X: *tiempo en horas hasta la curación* y, tras la recogida de datos se obtiene  y .

2.1 , como no se requiere la normalidad de la variable ya que el teorema central del límite garantiza una buena aproximación de la distribución de a una distribución normal y sustituyendo en la fórmula se tiene

```
inferior<-100+qt(0.025,39)*10/sqrt(40)
superior<-100+qt(0.975,39)*10/sqrt(40)
a<-paste(expression(IC [0.9] (mu) ),"=(",inferior,",",superior,")" )
print(noquote(a))
```
`## [1] IC[0.9](mu) =( 96.8018448450712 , 103.198155154929 )`
Observa que al ser podriamos utilizar en lugar de y apenas cambiaría el resultado:

```
inferior<-100+qnorm(0.025)*10/sqrt(40)
superior<-100+qnorm(0.975)*10/sqrt(40)
a<-paste(expression(IC[0.9](mu)),"=(",inferior,",",superior,")" )
print(noquote(a))
```
`## [1] IC[0.9](mu) =( 96.9010248384772 , 103.098975161523 )`
La razón es que cuando y para cualquier valor que escojamos. Observa el siguiente código que refleja este resultado pues conforme los grados de libertad de la distribución aumentan, más parecida es su distribución a la de . En particular, observa como y tienen gráficos muy similares.

```
x<-seq(-3,3,0.01)#rango de valores de la variable
n<-c(5,15,40)#grados de libertad de la t-student
par(mfrow=c(1,2))#dividimos en dos la pantalla gráfica de R
plot(x,pnorm(x),type="l",lwd=1)#dibujamos la función de distribución de Z
for (i in n)
{
  lines(x,pt(x,i),col=i)#dibujamos la función de distribución de t_i
}
legend("topleft",c(as.character(n),"Z"),col=c(n,"black"),pch=17)
plot(x,dnorm(x),type="l",lwd=1)#dibujamos la función de densidad de Z
for (i in n)
{
  lines(x,dt(x,i),col=i)#dibujamos la función de densidad de t_i
}
legend("topleft",c(as.character(n),"Z"),col=c(n,"black"),pch=17)
```
2.2 , como no se requiere la normalidad de la variable y ahora se utiliza el valor de en lugar de pues es el parámetro exacto y no una estimación de la desviación

```
inferior<-100+qt(0.005,39)*9/sqrt(40)
superior<-100+qt(0.995,39)*9/sqrt(40)
a<-paste(expression(IC [0.99] (mu) ),"=(",inferior,",",superior,")" )
print(noquote(a))
```
`## [1] IC[0.99](mu) =( 96.146571985339 , 103.853428014661 )`
2.3 , como la variable debe ser normal para que sea normal (el Teorema Central del Límite requiere un valor de mayor para poder utilizarlo). Tampoco puede aproximarse por por ser demasiado pequeño.

```
inferior<-100-qt(0.975,9)*10/sqrt(10)#observa que por simetría qt(0.975,9)=-qt(0.025,9)
superior<-100+qt(0.975,9)*10/sqrt(10)
a<-paste(expression(IC [0.9] (mu) ),"=(",inferior,",",superior,")" )
print(noquote(a))
```
`## [1] IC[0.9](mu) =( 92.8464309402934 , 107.153569059707 )`
2.4 Estamos en las condiciones de 2.1. Observa que la hipótesis alternativa siempre es la sospecha del investigador, luego en este caso

```
sig<-0.05
tobs<-(100-105)/(10/sqrt(40))
p_valor<-pt(tobs, 39)        
if (p_valor<sig) {
  print (c("p_valor=", p_valor,  "SÍ es significativo"))
} else {
  print(c("p_valor=", p_valor,  "NO es significativo"))
}
```
`## [1] "p_valor="            "0.00151371124968941" "SÍ es significativo"`
2.5 y 2.6 En este caso el estadístico con el que trabajamos es y se requiere que tenga distribución normal para poder utilizar los resultados de Fig2. Como no es un promedio de las observaciones de la muestra no podemos aplicar la fórmula anterior. En este caso debemos utilizar las correspondientes fórmulas aprendidas el curso pasado

```
sig<-0.05
S<-10
n<-40
inferior<-(n-1)*S^2/qchisq(0.95,n-1)
superior<-(n-1)*S^2/qchisq(0.05,n-1)
a<-paste(expression(IC [0.9] (sigma^2) ),"=(",inferior,",",superior,")" )
print(noquote(a))
```
`## [1] IC[0.9](sigma^2) =( 71.4649219970863 , 151.778195985866 )````
chiobs<-(n-1)*S^2/9^2
 p_valor<-2*min(pchisq(chiobs, 39) ,1-pchisq(chiobs, 39) )#¿Por qué es así el p-valor?       
 
if (p_valor<sig) {
  print(c("p_valor=", p_valor,  "SÍ es significativo"))
} else {
  print(c("p_valor=", p_valor,  "NO es significativo"))
}
```
`## [1] "p_valor="            "0.298997904155689"   "NO es significativo"`
## 1.2 Inferencia con observaciones muestrales dependientes o independientes

Esta sección fue parcialmente estudiada en Estadística I. Se trata de hacer la inferencia sobre la igualdad de la media poblacional a partir de dos grupos de observaciones muestrales. Ahora bien, hay que distinguir si esos dos grupos de observaciones proceden de la misma muestra (observaciones pareadas o dependientes ) o en dos muestras diferentes (cada muestra se toma en una población diferente). En cada caso, la técnica estadística es diferente, incluso la información aparece de distinta manera en la correspondiente base de datos.

**Ejemplo**

En un instituto se están analizando los resultados académicos de los estudiantes de segundo de bachiller

¿Las variable : nota de inglés, : nota de lengua española tienen medias poblacionales iguales?

¿Los estudiantes que han seguido un programa bilingüe en inglés tienen mejor calificación en inglés que los que no lo han seguido?

La primera cuestión es de observaciones pareadas puesto que para cada individuo de la muestra observamos y y queremos estudiar el contraste . La segunda cuestión es de observaciones independientes puesto que consideramos dos poblaciones distintas (uso alto frente a uso bajo), por lo que hay dos muestras cada una extraída de cada población y planteamos.

Aunque los planteamientos de los contrastes son iguales, se resuelven de manera diferente. La clave teórica que hace que sean diferentes las técnicas estadísticas estriba en el concepto de independencia. En ambos casos podemos definir 2 variable e y hacemos inferencia sobre .

En ambos casos consideramos el estadístico . Como sabes del curso pasado pero . Cuando las observaciones son independientes mientras que si son dependientes . En consecuencia, el termino de la varianza del estimador NO es igual en ambas técnicas y, como bien sabemos, es fundamental para obtener el margen de error en los intervalos.

El esquema Fig.3 refleja la diferencia de técnicas. Esencialmente, las observaciones pareadas se reducen a técnicas de inferencia de una variable pues se construye la variable diferencia que resta para cada individuo los valores de ambas variables y permite una estimación directa de . Para las observaciones independientes hacemos .

Es muy importante que entiendas los siguientes aspectos teóricos:

1. Ambas vías responden a una misma fórmula en donde y .
2. Cuando son independientes, los grados de libertad se obtienen con la fórmula de Welch que, en el caso de que las varianzas poblacionales sean similares en ambos grupos, toma como valor máximo . El siguiente código permite visualizar la fórmula de Welch y el efecto que tiene en los grados de libertad un desequilibrio alto de las varianzas.

```
#install.packages(c("rgl", "car"))
#si no se activa Rcmdr hay que tener instalados estas dos librerías, 
#habitualmente están instaladas por defecto, solo hay que cargarlas
#library(rgl)
#library(car)
N1<-2000
N2<-2000
S1<-seq(0.5, 3, 0.1)
S2<-seq(0.5,3, 0.1)
a1<-length(S1)
a2<-length(S2)
l<-array(0, c(a1*a2,3))
r<-1
for (i in 1:length(S1))
{
  for (j in 1:length(S2))
  {
    
    l[r,1]<-S1[i]
    l[r,2]<-S2[j]
    l[r,3]<-(S1[i]/N1+S2[j]/N2)^2/(S1[i]^2/(N1^2*(N1-1))+S2[j]^2/(N2^2*(N2-1)))
    r<-r+1
  }
}
l<-as.data.frame(l)
scatter3d(l$V1,l$V2,l$V3, data=l, surface=FALSE, residuals=TRUE, bg="black", 
          axis.scales=TRUE, grid=TRUE, ellipsoid=FALSE)
```
1. En la práctica, siempre que la naturaleza del problema lo permita, se preferirá diseñar el estudio con observaciones pareadas que con observaciones independientes. Por ejemplo, si se quiere estudiar si una dieta es efectiva, es evidente que el estudio debe pesar el primer de la dieta a individuos con lo que tenemos la variable y al final del estudio debe pesar a los mismos individuos con lo que tenemos la variable . Este estudio obviamente debe pensarse para hacer análisis con observaciones pareadas. Sin embargo puede suceder que nos interese comparar la rapidez de dos algoritmos de ordenación. Se tienen dos variable e . Ahora nos planteamos si observar la variable en ordenadores y la variable en ordenadores distintos. En consecuencia tendriamos observaciones independientes. O bien, escoger ordenadores y correr ambos algoritmos en cada ordenador, con lo que las observaciones son dependientes. Es claro que este último diseño de experimentación es mejor porque si un ordenador es más lento por antigüedad de su CPU, por ejemplo, afectará igualmente a ambos algoritmos. En consecuencia, la influencia del ordenador en el algoritmo afecta igualmente a ambos algoritmos. Esto hace que e covaríen en positivo y, por tanto, , por lo que el margen de error con un diseño de observaciones pareadas es menor que si fueran independientes. Además, un estudio con independientes nunca nos dejaría claro si el efecto ordenador ha sesgado el estudio beneficiando a un algoritmo frente a otro.

### 1.2.1 Ejercicios modelo

**Ejercicio 1: Selección de diseños**

En cada una de estas situaciones debes decidir si es posible hacer una diseño con observaciones pareadas y, en su caso, cómo se haría.

1. Queremos estudiar la resistencia de una tela sometiéndola a dos pruebas una de peso y otra de estiramiento. Se cuenta el tiempo hasta la rotura de la pieza y se quiere saber si es más resistente al peso o al estiramiento.
2. Se quiere estudiar si el coche A tiene una dirección más suave que el coche B. Se hacen pruebas de aparcado, a mayor rapidez en el aparcamiento se considera mayor suavidad de la dirección.
3. Se considera una prueba de resistencia al peso a la que se someten dos tipos de tela, tela A y tela B. ¿Cuál es la más resistente?.

**Solución**

El estudio A) requiere escoger un número de piezas de la tela. Cada pieza de tela puede haber sido obtenida con una máquina diferente, en días distintos o por personal de fábrica diferente. Es preferible hacer un diseño con observaciones pareadas para eliminar el efecto que los factores máquina, día de producción o persona operaria pueden ejercer sobre la calidad de la tela. Por tanto, cada pieza de tela se divide en dos partes para ser sometida a cada prueba.

En el B) se toman individuos, es preferible que cada individuo aparque ambos coches y se cronometre el tiempo de aparcado. En este caso las observaciones son pareadas pero evitamos el factor individuo que puede beneficiar a un tipo de coche si el azar hace que los individuos con mayor pericia conduzcan uno de los tipos de coche.

En le C) no se puede hacer un diseño de observaciones pareadas porque los individuos a observar aquí proceden de poblaciones diferentes. Luego solo hay una variable : resistencia al peso, pero que se observa a un grupo de individuos de una población A y a otro grupo de individuos de otra población B, por lo que son observaciones independientes.

**Ejercicio 2: Inferencia con dos poblaciones**

Se toma una muestra de 14 individuos y se cronometra el tiempo en segundos que requieren para aparcar en paralelo dos coches distintos con objeto de estudiar cuál de los dos tiene una dirección mejor (cuanto mejor es la dirección, menos tiempo se necesita para aparcar).

| Individuo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Coche 1 | 37 | 25.8 | 16.2 | 24.2 | 22 | 33.4 | 23.8 | 58.2 | 33.6 | 24.4 | 23.4 | 21.2 | 36.2 | 29.8 | 
| Coche 2 | 17.8 | 20.2 | 16.8 | 41.4 | 21.4 | 38.4 | 16.8 | 32.2 | 27.8 | 23.2 | 29.6 | 20.6 | 32.2 | 53.8 | 

a) Estudia el contraste de igualdad de medias y proporciona el intervalo de confianza. Compara los resultados si el diseño se hubiese realizado con 28 personas, una distinta para cada observación.

b) En las condiciones del diseño planteado en el enunciado, suma 5 a todas las observaciones del coche A y estudia la hipótesis de igualdad de medias, posteriormente estudia la sospecha de que el coche A tiene una dirección más dura que el coche B. Proporciona una explicación técnica de la contradicción que proporcionan ambos contrastes. En un estudio aplicado, ¿cuál te parece la forma sensata de actuar?

**Solución**

1. y b) La parte mecánica del ejercicio se realiza con R y el código que sigue. No obstante vamos a realizar el análisis teórico que es de mayor importancia.

En esta parte es importante observar que la manera de introducir los datos refleja el diseño con el que estamos trabajando. Ambos procedimientos en este caso han dado lugar a la misma conclusión, pero está claro que el diseño con observaciones pareadas es más adecuado porque evita el sesgo que podría dar lugar el factor: “destreza del conductor” (mejores los de un grupo que de otro). Estos factores que no se tienen en cuenta y dan lugar a una confusión en los test de comparación de medias se denominan **factores de confusión**.

Observa que al sumar 5 a todos los datos del coche A estamos forzando a que la dirección sea más *dura* que la del coche B. Al hacer el contraste de igualdad, está claro que no se rechaza la igualdad, sin embargo hay evidencia significativa de que el coche A es más “duro” que el coche B porque el tiempo medio de aparcamiento es mayor en el primero que en el segundo. No es una contradicción, la razón es que la región de rechazo en el primer caso debe dividir el nivel de significación  entre las dos colas, pero no es así en los unilaterales que concentra la región de rechazo en una cola. Cuando observamos el p-valor de un contraste bilateral y es menor que , es claro que el correspondiente contraste unilateral será significativo.

De lo anterior se puede concluir que en la práctica es conveniente realizar un estudio descriptivo previo que permita esclarecer en qué sentido plantear una hipótesis unilateral. Si esta última no se rechaza, tampoco se rechazará la bilateral.

```
pareadas<-data.frame(cocheA=c(37,   25.8,   16.2,   24.2,   22, 33.4,   23.8,   58.2,   33.6,   24.4,   23.4,   21.2,   36.2,   29.8),cocheB=c(17.8,    20.2,   16.8,   41.4,   21.4,   38.4,   16.8,   32.2,   27.8,   23.2,   29.6,   20.6,   32.2,   53.8))#INTRODUCIR DATOS PAREADOS
t.test(pareadas$cocheA, pareadas$cocheB, paired=TRUE)#test pareados
```
```
## 
##  Paired t-test
## 
## data:  pareadas$cocheA and pareadas$cocheB
## t = 0.35818, df = 13, p-value = 0.726
## alternative hypothesis: true mean difference is not equal to 0
## 95 percent confidence interval:
##  -6.109775  8.538347
## sample estimates:
## mean difference 
##        1.214286
```
```
independientes<-stack(pareadas[, c("cocheA","cocheB")])#INTRODUCIR DATOS INDEPENDIENTES
names(independientes)<- c("tiempo", "coche")
t.test(tiempo~coche, data=independientes)#test independientes
```
```
## 
##  Welch Two Sample t-test
## 
## data:  tiempo by coche
## t = 0.30296, df = 25.946, p-value = 0.7643
## alternative hypothesis: true difference in means between group cocheA and group cocheB is not equal to 0
## 95 percent confidence interval:
##  -7.025283  9.453854
## sample estimates:
## mean in group cocheA mean in group cocheB 
##             29.22857             28.01429
```
```
## 
##  Paired t-test
## 
## data:  pareadas$cocheA and pareadas$cocheB
## t = 1.833, df = 13, p-value = 0.08979
## alternative hypothesis: true mean difference is not equal to 0
## 95 percent confidence interval:
##  -1.109775 13.538347
## sample estimates:
## mean difference 
##        6.214286
```
```
## 
##  Paired t-test
## 
## data:  pareadas$cocheA and pareadas$cocheB
## t = 1.833, df = 13, p-value = 0.0449
## alternative hypothesis: true mean difference is greater than 0
## 95 percent confidence interval:
##  0.2104843       Inf
## sample estimates:
## mean difference 
##        6.214286
```
**Ejercicio 3: Efectos de la diferencia de varianzas**

Se consideran la desviación de los objetivos de gasto de dos grupos de empresas, el grupo 1 lo forman 14 empresas de la industria del metal y el grupo 2 14 empresas del sector servicios. Se quiere estudiar si en ambos sectores hay un comportamiento similar en media respecto a la variable en estudio.

| G. 1 | 7.7 | -3.4 | -13 | -5 | -7.2 | 4.2 | -5.4 | 29 | 4.3 | -4.8 | -5.8 | -8 | 7 | 0.57 | 
| G. 2 | -1.7 | -0.7 | -2.7 | 21.9 | 1.9 | 18.9 | -2.7 | 12.7 | 8.3 | 3.73 | 10.1 | 1.1 | 12.7 | 34.3 | 

Estudia

1. Efectúa el contraste adecuado para decidir la igualdad de medias poblacionales.
2. Modifica los datos del grupo 2 multiplicando cada dato por 2 y restándoles la media. Vuelve a repetir el apartado a).
3. Efectúa un análisis técnico de los resultados obtenidos.

**Solución**

En este ejercicio consideramos dos grupos de empresas bien diferenciados por su actividad. La variable en estudio refleja el ajuste de una empresa a sus previsiones de gasto. Parece razonable pensar que las empresas del sector metal tienen un mercado más estable que las del sector servicios, por lo que sus previsiones de gasto se ajustan mejor a la realidad. Lo que plantea el ejercicio se puede hacer de manera mecánica con el siguiente código.

```
e1<-c(7.7,-3.4,-13,-5,-7.2,4.2,-5.4,29,4.3,-4.8,-5.8,-8,7,0.57)
e2<-c(-1.7,  0.7, -2.7, 21.9,  1.9, 18.9, -2.7, 12.7,  8.3, 3.7, 10.1 , 1.1, 12.7, 34.3)
error<-c(e1,e2)
ap<-c(rep("aUno", 14),rep("bDos", 14))
data<-data.frame(error, ap)
boxplot(error~ap,data=data)
```
```
## 
##  F test to compare two variances
## 
## data:  error by ap
## F = 0.91142, num df = 13, denom df = 13, p-value = 0.8697
## alternative hypothesis: true ratio of variances is not equal to 1
## 95 percent confidence interval:
##  0.2925889 2.8391213
## sample estimates:
## ratio of variances 
##           0.911425
```
```
## 
##  Two Sample t-test
## 
## data:  error by ap
## t = -2.1221, df = 26, p-value = 0.04351
## alternative hypothesis: true difference in means between group aUno and group bDos is not equal to 0
## 95 percent confidence interval:
##  -16.7374359  -0.2668498
## sample estimates:
## mean in group aUno mean in group bDos 
##         0.01214286         8.51428571
```
```
## 
##  Welch Two Sample t-test
## 
## data:  error by ap
## t = -2.1221, df = 25.944, p-value = 0.04354
## alternative hypothesis: true difference in means between group aUno and group bDos is not equal to 0
## 95 percent confidence interval:
##  -16.738297  -0.265989
## sample estimates:
## mean in group aUno mean in group bDos 
##         0.01214286         8.51428571
```
```
data$error[data$ap=="bDos"]<-2*data$error[data$ap=="bDos"]-mean(data$error[data$ap=="bDos"])
boxplot(error~ap,data=data)
```
```
## 
##  F test to compare two variances
## 
## data:  error by ap
## F = 0.22786, num df = 13, denom df = 13, p-value = 0.01203
## alternative hypothesis: true ratio of variances is not equal to 1
## 95 percent confidence interval:
##  0.07314723 0.70978031
## sample estimates:
## ratio of variances 
##          0.2278562
```
```
## 
##  Welch Two Sample t-test
## 
## data:  error by ap
## t = -1.3239, df = 18.632, p-value = 0.2016
## alternative hypothesis: true difference in means between group aUno and group bDos is not equal to 0
## 95 percent confidence interval:
##  -21.961857   4.957571
## sample estimates:
## mean in group aUno mean in group bDos 
##         0.01214286         8.51428571
```
Observamos que en a) hay diferencias significativas y hacerlo con igualdad de varianzas o con Welch resulta prácticamente indiferente. Cuando se puede aceptar la igualdad de varianzas, Welch no penaliza en gran medida los grados de libertad por lo que no se alteran conclusiones. Se concluye que hay una mayor media de la variable en las empresas de servicios que en las del metal. Sin embargo, en b) las empresas de servicios han aumentado su heterogeneidad respecto a la variable (aunque mantienen la misma media), pero ahora no hay evidencias para rechazar el contraste de diferencias. La diferencia en medias sigue siendo la misma, pero la discrepancia en las varianzas se refleja en una disminución drástica en los grados de libertad lo que hace que la región de rechazo disminuya, y el valor relativo de diferencia entre medias no sea significativo.

Las gráficas de cajas permiten visualizar lo anteriormás fácilmente. La diferencia en las medias en el caso a) es relevante pues la dispersión de los datos es similar en ambos grupos por lo que las posiciones de los conjuntos de datos claramente se distinguen. En el caso b), el grupo 2 es tan heterogéneo que el rango de valores en el que se mueve el grupo 1 queda dentro del grupo 2. Aunque la diferencia de medias es la misma que en el caso a), la posición del conjunto de datos queda solapada. En consecuencia, cualquier procedimiento estadístico detectará con mayor facilidad la diferencia de medias en el primer caso que en el segundo. Técnicamente son los grados de libertad los que cuantifican la “facilidad” a la que nos referíamos anteriormente para detectar diferencias, en concreto, Welch asigna los máximos grados de libertad cuando las varianzas son iguales y va disminuyendo conforme mayor es la discrepancia entre varianzas, como ocurre en este ejercicio.

En el dibujo que sigue observamos en negro y rojo una posible distribución acorde a los valores de la variable en estudio en ambos grupos de empresas : grupo 1 y grupo 2 (negro y rojo, respectivamente). En azul se representan los valores del grupo 2 con el doble de desviación típica. Observamos que la distribución en azul tiene la misma media que los datos originales, pero los valores son más dispersos y comienzan a tomar con mayor probalidad valores en el rango que era propio del grupo 1.

```
e1<-c(7.7,-3.4,-13,-5,-7.2,4.2,-5.4,29,4.3,-4.8,-5.8,-8,7,0.57)
e2<-c(-1.7,  0.7, -2.7, 21.9,  1.9, 18.9, -2.7, 12.7,  8.3, 3.7, 10.1 , 1.1, 12.7, 34.3)
x1<-e1
x2<-e2
m1<-mean(x1)
m2<-mean(x2)
s1<-sd(x1)
s2<-sd(x2)
a1<-min(x1)-10
a2<-max(x1)
b1<-min(x2)-10
b2<-max(x2)
a<-seq(a1,a2,0.05)
b<-seq(b1,b2,0.05)
plot(a,dnorm(a,m1,s1),type="l",lwd=1)
lines(b, dnorm(b,m2,s2),col="red")
lines(b, dnorm(b,m2,2*s2),col="blue")
legend("topright", c("G1","G2",paste(2,"*G2")),pch=16, col=c("black", "red","blue"))
abline(v=m2, col="red")
abline(v=m1, col="black")
```
## 1.3 Potencia de un contraste

Cuando realizamos un contraste estadístico estamos tomando una decisión entre dos opciones: aceptar o aceptar . En consecuencia podemos cometer dos errores que en estadística se denominan error de tipo I () y error de tipo II ().

Estos errores son debidos al azar, es decir, el muestreo nos ha proporcionado una muestra que lleva a confusión. Por tanto, la forma de medir cada error es obteniendo su probabilidad, puesto que es así como se mide la ocurrencia del azar. A la probabilidad de error tipo I, , se le denomina nivel de significación y es el único error que controlamos en el procedimiento de resolución de contrastes. Por tanto, el hecho de que no se controle permite clasificar procedimientos estadísticos con una misma finalidad. Por ejemplo, si hubiera dos procedimientos para determinar que la diferencia de dos distribuciones cumple , el procedimiento preferido sería el que tuviera, para una misma distribución, el valor más bajo, o, lo que es lo mismo, la potencia más alta. Por tanto, la potencia de un contraste se define como la probabilidad de que un contraste acepte cuando es cierta. La figura 4 visualiza, para un contraste particular, los conceptos anteriores. Es muy importante entender que la representación de supone un valor conocido para el parámetro, mientras que asume un valor . La potencia se va calculando para distintos valores de puesto que es un valor desconocido.

En el campo de la biotecnología se utilizan diversas pruebas con objeto de discernir si un biomarcaor predice bien la presencia de una enfermedad. Análogamente, en medicina, el personal sanitario está interesado en conocer si una prueba diagnóstica es capaz de detectar bien una enfermedad. Establecer con exactitud que significa “bien” es difícil por eso se utiliza la tabla presentada en la Fig. 5 pero con otra nomenclatura. La figura 7 muestra la denominación de los errores en este contexto.

Nota: Observa que P(+|**E**nfermo)=**S**ensibilidad; P(-|**S**ano)=**E**specificidad

En el campo de la minería de datos las tablas que aparecen en las Fig. 5 y 6 también hay que considerarlas para evaluar la calidad de las técnicas de clasificación. Estás técnicas considerar una parte de la muestra para clasificar los individuos de modo binario en “positivos” o “negativos” (donde positivo o negativo es tener o no tener una característica en estudio). El resto de la muestra se clasifica de acuerdo al aprendizaje realizado previamente y se construye la denominada matriz de confusión (figura 7). A partir de esta matriz se obtendría la sensibilidad como y la especificidad como . En la teoría de minería de datos se construyen otros muchos índices a partir de los cuatro valores de la matriz de confusión, que no estudiaremos aquí.

Los siguientes ejercicios profundizan en el concepto de potencia. El primero refleja una situación concreta para la Figura 4 dando valores a las distintas medidas y parámetros. El segundo visualiza la potencia desde otro punto de vista en el que fijamos el valor y vamos cambiando el valor que se contrasta en la hipótesis nula.

### 1.3.1 Ejercicios modelo

**Ejercicio 1: Cálculo de la potencia**

Consideramos el contraste . Supongamos que disponemos de dos muestras independientes de tamaño 100 cada una de ellas y observamos X en una de las muestras e Y en la otra. Las varianzas poblacionales tanto de X como de Y son iguales a 50. Supongamos que la diferencia REAL de las medias de ambas variables es

1. Calcula la potencia del contraste para cualquier nivel .
2. Calcula la potencia del contraste cuando

**Solución**

Por ser grande el tamaño de muestra el estadístico de contraste se distribuye como una normal y al ser las varianzas conocidas tenemos que bajo : rechazamos cuando . En consecuencia, la potencia del contraste se puede calcular como


b)Si , entonces y la potencia se puede escribir como .

**Ejercicio 2: la curva ROC**

Una de las herramientas más utilizadas en el campo “bio” para medir la potencia de una técnica de diagnóstico es la curva ROC.

Representa en el eje OX “1-especificidad” y en el eje OY la “sensibilidad”.

Consideremos una técnica de diagnóstico para la hiperglucemia. Consiste en tomar una muestra de saliva y medir la cantidad de una hormona. Obtenemos que para distintos valores de x la especificiad y la sensibilidad son

| a. Dibuja la curva ROC |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|
| x | 0 | 2 | 3 | 4 | 5 | 6 | 
|---|---|---|---|---|---|---|
| Especificidad | 1 | 0.9 | 0.8 | 0.6 | 0.4 | 0.1 | 
| Sensibilidad | 0 | 0.2 | 0.3 | 0.7 | 0.9 | 0.99 | 

1. Modifica los datos de la tabla anterior para obtener otro método “mejor” en los valores de x: 3, 4, 5. Dibuja la curva ROC en el mismo gráfico que a) y obtén conclusiones.
2. Se denomina AUC al área bajo la curva. Este valor cuanto más cercano a 1, mejor se considera el método de diagnóstico. También sirve para comparar entre dos métodos. Así, para un método, si el valor AUC se encuentra: [0.5, 0.6): malo, [0.6, 0.75): regular, [0.75, 0.9): bueno, [0.9, 0.97):muy bueno, : excelente. Calcula la AUC de los métodos dibujados en a) y b).
3. A la hora de escoger el valor x que mejor diagnostica, se debe buscar el valor más cercano a (0, 1), que es un valor que indica el diagnóstico correcto de todos los enfermos y de todos los sanos. SE denomina también Índice de Yauden, es el valor x para el cual se hace máxima la operación (sensibilidad+especificidad-1). ¿Cuál es el mejor valor, en este caso, según el índice de Youden?

```
#a)
x<-c(0,2,3,4,5,6)
E<-c(1,0.9, 0.8,0.6, 0.4, 0.1)
S<-c(0, 0.2, 0.3, 0.7, 0.9, 0.99)
plot(1-E, S,type="l",xlab="1-especificidad",ylab="sensibilidad")
abline(a=0,b=1,col="red")
#b)
S2<-c(0, 0.2, 0.4, 0.75, 0.93, 0.99)
lines(1-E, S2,type="l",col="blue")
```
```
#c)Hay métodos directos pero aquí debemos hacerlo a mano
auc<-0
auc2<-0
for (i in 2:length(x))
{
  auc<-auc+(E[i-1]-E[i])*(S[i-1]+0.5*(S[i]-S[i-1]))
  auc2<-auc2+(E[i-1]-E[i])*(S2[i-1]+0.5*(S2[i]-S2[i-1]))
}
print(c(auc, auc2))
```
`## [1] 0.5785 0.6110````
#d)
youden1<-which(E+S-1==max(E+S-1))
youden2<-which(E+S2-1==max(E+S2-1))
print(c("método1", x[youden1]))# Los valores 4 y 5 son elegibles, dependerá en la elección de qué es más costoso, una baja especificidad (más falsos positivos) o una baja sensibilidad (más falsos negativos)
```
`## [1] "método1" "5"``## [1] "método2" "4"`
**Ejercicio 3: Clasificación**

La regresión logística es una técnica muy utilizada en aprendizaje supervisado que combina las variables observadas en los individuos de la muestra para obtener la probabilidad de pertenencia a un grupo de los individuos.

Por ejemplo, en un estudio de mercado se observan diferentes variables químicas en vinos que proceden de uvas recogidas con dos técnicas diferentes de cultivo, una es novedosa y otra es la habitual (control). Se decide que todos aquellas catas cuya probabilidad predicha de pertenencia a la técnica novedosa sea superior a 0.7 se consideren cultivados con la técnica novedosa. Se obtiene la siguiente matriz de confusión tras la participación

| clasificación\realidad | novedosa | control | 
|---|---|---|
| novedosa | 35 | 10 | 
| control | 15 | 40 | 

1. Calcula la especificidad y la sensibilidad. 80%, 70%
2. Calcula el porcentaje de aciertos para cada técnica de cultivo 70%, 80%
3. Se denomina “exactitud” al porcentaje de aciertos sobre el total de decisiones y “precisión” al porcentaje de predicciones positivas correctas sobre el total de positivos predichos. Calcula ambas medidas. 75%, 35/45=77,7%

**Ejercicio 4: [avanzado] Cálculo de la potencia**

Consideramos el contraste . Supongamos que disponemos de dos muestras independientes de tamaño 100 cada una de ellas y observamos X en una de las muestras e Y en la otra. Las varianzas poblacionales tanto de X como de Y son iguales a 50. Supongamos que la diferencia REAL de las medias de ambas variables es ; si denotamos a la función de distribución de la normal estándar (N(0, 1)=Z)

1. Demuestra que la potencia se puede escribir como si el nivel de significación es .
2. Representa gráficamente la potencia según los valores que tome cuando e interpreta el gráfico.

**Solución**

Por ser grande el tamaño de muestra el estadístico de contraste se distribuye como una normal y al ser las varianzas conocidas tenemos que bajo : rechazamos cuando . En consecuencia, la potencia del contraste se puede calcular como


b)Si , entonces y la potencia se puede escribir como . Observa que cuando es cuando estamos bajo y, por tanto, el valor es . Asimismo, cualquier valor da lugar a un , por esa razón siempre asume el valor con el que más error de tipo I se puede cometer. Por otra parte, conforme toma valores altos, la potencia va creciendo puesto que la realidad (que es ) se hace más evidente para la técnica estadística.

```
a<-seq(-1,5,0.05)
y<-1-pnorm(1.64-a)
plot(a,y,type="l",xlab=paste("a=",expression(mu[x]-mu[y]>0)),ylab="potencia")
abline(h=0.05,col="red")
```
**Ejercicio 5: [avanzado] Cálculo de la potencia**

Consideramos el contraste , donde es un número positivo . Supongamos que disponemos de dos muestras independientes de tamaño 100 cada una de ellas y observamos X en una de las muestras e Y en la otra. Las varianzas poblacionales tanto de X como de Y son iguales a 50. Supongamos que la diferencia REAL de las medias de ambas variables es 2; si denotamos a la función de distribución de la normal estándar (N(0, 1)=Z)

1. Demuestra que la potencia se puede escribir como si el nivel de significación es 0.05
2. Utilizando el resultado de a), indica qué ocurre con la potencia del contraste cuando d toma valores en el intervalo (0, 2). Explica con tus propias palabras qué significa el comportamiento observado

**Solución**

Por ser grande el tamaño de muestra el estadístico de contraste se distribuye como una normal y al ser las varianzas conocidas tenemos: rechazamos cuando . En consecuencia, la potencia del contraste se puede calcular como

Si , entonces y la potencia se puede escribir como .

1. Observamos que como la función de distribución es creciente, va creciendo conforme va aumentando su valor y, por tanto, la potencia decrece. La potencia del contraste decrece de 0 a 2, es decir, conforme más se aproxima al valor real, lo cual es esperable ya que a la técnica estadística le cuesta más distinguir que los datos no se comportan como la realidad. Cuando llega a 2, la potencia es 0.05, el nivel de significación, pues la hipótesis nula es cierta.

## 1.4 Teoría de la estimación paramétrica

Recordemos que para estimar el parámetro de una distribución , de un modelo estadístico el procedimiento básico consiste en tomar individuos de la población y observar la variable de interés en dichos individuos. Con ello obtenemos observaciones . Estos valores los combinamos mediante una función que se denomina estadístico. Cuando utilizamos esta función para aproximar el estadístico se llama estimador de y se escribe . Al sustituir en esta función por los valores observados se obtiene una estimación del verdadero valor . Obviamente la función hay que escogerla adecuadamente para que la aproximación al valor desconocido sea buena. Observa que el azar es en última instancia quien proporciona los valores observados por lo que es una variable aleatoria.

En este apartado nos planteamos qué procedimiento existe para escoger frente a cualquier otro estimador de , . Hay dos propiedades que son deseables y son:


Se denomina sesgo a la diferencia y el estimador es centrado cuando el sesgo es cero. Estas dos propiedades deseables aparecen de manera conjunta en lo que se denomina Error Cuadrático Medio (ECM o MSE por sus siglas en inglés).

 Observa que si hay que comparar dos estimadores  y  preferiremos aquel con menor error cuadrático medio que se dice que es el *más eficiente*.

Hay un método que proporciona en muchos casos el estimador eficiente, es decir, el estimador con mínima varianza y sesgado de un parámetro . Se denomina el método de máxima verosimilitud y el estimador obtenido con este método se denomina estimador máximo verosímil de y se escribe MLE (maximum likelihood estimator) por sus siglas en inglés. El método sigue tres pasos:

- Paso 1: Obtener la función de verosimilitud


- Paso 2: se toman logaritmos en la expresión anterior (para facilitar el paso 3)
- Paso 3: se busca el valor que maximiza .

La idea detrás del método es que si el azar nos ha dado los valores es porque el valor de desconocido en la distribución es tal que los hace más verosímiles (probables). Así que el método de máximo verosimilitud para obtener estimadores de un parámetro responde a la pregunta ¿ cuál es el valor de que hace máxima la probabilidad (más verosímil) de obtener los valores observados por azar?

### 1.4.1 Ejercicios modelo

**Ejercicio 1: MLE para obtener el parámetro de una distribución discreta**

Obtén el estimador MLE para el parámetro de una distribución de Poisson

Obtén el estimador MLE para el parámetro de una distribución exponencial

**Solución**

Paso 1: Función de verosimilitud


Paso 2: Se toman logaritmos

Paso 3: Se obtiene el máximo


Para el caso de la exponencial

Paso 1: Función de verosimilitud


Paso 2: Se toman logaritmos

Paso 3: Se obtiene el máximo


**Ejercicio 2: [avanzado] Propiedades de los estimadores**

A continuación se proporciona una pareja de estimadores de y debes escoger uno de los dos siguiendo el criterio del mínimo ECM (error cuadrático medio). Dada una muestra aleatoria simple de tamaño 7, , .

**Solución**

Para resolver este ejercicio hay que tener en cuenta que la esperanza es un operador lineal y que la varianza de una suma de variables independientes es la suma de las variables:

Debemos obtener el ECM de cada estimador propuesto y se sigue con claridad que el más eficiente es .

Observa que ambos son centrados, en tal caso es el que tiene la varianza menor el que es más eficiente.

**Ejercicio 3: Exactitud y Precisión**

Los conceptos de sesgo y varianza son especialmente importantes en la calibración de instrumentos de medida en laboratorio. Reciben el nombre de exactitud y precisión, respectivamente. El siguiente ejercicio ilustra esta situación

Una muestra patrón de suero sanguíneo humano contine 42g. de albúmina por litro. Dos laboratorios A y B realizan cada uno seis determinaciones en el mismo día de la concentración de albúmina con los siguientes resultados en g/L

| Lab/Medición | 1 | 2 | 3 | 4 | 5 | 6 | 
| A | 42.1 | 41.9 | 42.2 | 41.1 | 42.5 | 41.6 | 
| B | 39.8 | 43.8 | 42.1 | 40.1 | 43.9 | 41.9 | 

**Solucion**

La exactitud mide la concordancia entre un valor medido y el valor verdadero (teórico). Es el concepto de sesgo, pues la medición es una estimación, , de dicho valor verdadero, ($\theta$). Calculamos por tanto para cada una de las mediciones, este valor se denomina error absoluto. Cuando no se dispone del valor verdadero se realizan los cálculos con la media.

Error absoluto medio o desviación absoluta media A: B: 1.33. Por lo que deducimos que es más inexacto el laboratorio B en sus mediciones. También se utiliza el error absoluto relativo que dividiría entre el error absoluto medio, en este caso se tendría Lab A: 0.9% y Lab. B: 3.1%. Observa que la definición que hemos dado de sesgo en la teoría es que es más aproximada al concepto de error absoluto medio.

En cuanto a la precisión, el concepto tiene que ver con la desviación. En el contexto de la medición en laboratorios se entiende como el grado en que un instrumento de medida proporciona el mismo resultado al realizar distintas mediciones de la misma magnitud. Se utiliza el coeficiente de variación o RSD (relative standard deviation): Lab A: o y Lab B: 0.042 o 4.2%.

Concluimos que el laboratorio A hecho mediciones más precisas y exactas que el laboratorio B.

En definitiva, en el análisis anterior hemos identificado


Cuando no hay comparaciones entre laboratorios sino que se trata de establecer si la exactitud y la precisión de las medidas es adecuada, se suele aceptar como buena una precisión inferior al 10% (buena reproducibilidad de la medida) y exactitud, medida con el error absoluto relativo, inferior también al 10% (alta exactitud). Aunque este valor del 10% depende de la exigencia establecidad en la correspondiente ISO a la que se acoge el laboratorio. También es cierto que la precisión no requiere del valor verdadero, por lo que es más fácil obtenerla que la exactitud.

## 1.5 Contrastes de ajuste de distribuciones. Contrastes de normalidad

En los ejercicios que hemos planteado hasta ahora en la materia de Estadística lo habitual es que el propio enunciado indique la distribución que sigue la variable: Poisson, exponencial, uniforme, normal, etc. Sin embargo, en la práctica, debe comprobarse mediante los datos observados qué distribución tiene la variable. En esta sección presentamos el procedimiento básico para hacer este tipo de estudios.

Las técnicas varían según la naturaleza de la variable lo que servirá de criterio para organizar la sección

### 1.5.1 Distribuciones Discretas: contraste chi-cuadrado

En este caso se considera una variable que toma un número finito de valores. La distribución de probabilidad nos indica con qué probabilidad toma cada uno de esos valores. La hipótesis nula del contraste, como en el resto de ajustes, estable la distribución de la variable.


En Estadística I ya se estudió este contraste en el caso de variables binarias. El estadístico del contraste se escribe:

donde, tras realizar la experimentación (el muestro), representa el número de veces que ha sucedido , es decir, es la frecuencia absoluta de .

***Ejemplo*** El control de calidad de una empresa establece que la producción de la empresa debe pararse cuando la proporción de productos defectuosos es del 2%. Cada hora, el servicio de calidad toma 300 productos y los analiza. Si encuentra nueve productos defectuosos, ¿tiene evidencias para dar la orden de parar la producción?

**Solución** La variable en estudio en este problema es X:ser el producto defectuoso. Esta variable es binaria y tenemos que . Nos planteamos el contraste con hipótesis alternativa .

```
## 
##  1-sample proportions test with continuity correction
## 
## data:  9 out of 300, null probability 0.02
## X-squared = 1.0629, df = 1, p-value = 0.1513
## alternative hypothesis: true p is greater than 0.02
## 95 percent confidence interval:
##  0.01630598 1.00000000
## sample estimates:
##    p 
## 0.03
```
El contraste NO es significativo, es decir, no hay evidencia para realizar el paro de la producción. Sin embargo lo que nos interesa aquí es observar que la salida de R está utilizando el test chi-cuadrado y no una distribución normal, como es esperable a partir de la teoría explicada en Estadística I. Sin embargo el siguiente razonamiento relaciona ambas distribuciones



Observa bien cómo se relacionan los estadísticos de contraste de ambos procedimientos, donde recuerda que es la proporción de éxitos:


De modo análogo se demuestra que cuando hay k posibles valores de la distribución, es decir, planteamos el contraste anterior al ejemplo se tiene


El test chi cuadrado mide en UNA sola medida la *distancia* de los datos a la distribución propuesta en la hipótesis nula, por lo que el error tipo 1 se reduce a . Observa que podríamos hacer  contrastes del tipo  , si todos se aceptan, la conclusión es que la distribución discreta es la propuesta. No obstante, cada vez que se hace un contraste se puede cometer un error de tipo I con probabilidad . En consecuencia, tras hacer los  contrastes se tiene que  luego la probabilidad de error tipo I global es la probabilidad de cometer un error tipo I en alguno de los contrastes, si suponemos que son independientes, se tendría:

Y este valor dispara el error tipo I conforme crece el valor de k. Este razonamiento se repetirá varias veces a lo largo del curso y, en cierto modo, es una idea que hay que tener en el trabajo inferencial. Cuantos más contrastes hacemos con los datos, mayor es la probabilidad de cometer un error tipo I, por esa razón hay que buscar procedimientos que engloben varios contrastes en uno, como en este caso.

**Ejercicio 1**

Nos planteamos si un dado está trucado. Para ello efectuamos 120 lanzamientos con los siguientes resultados del 1 al 6 respectivamente: 20, 14, 23, 12, 26, 25.

Observa que realmente se podría pensar que estamos haciendo 5 contrastes


Pero cada uno de estos contrastes tiene un error tipo 1 de 0.05, por lo que

El contraste chi-cuadrado hace un solo contraste por lo que el error tipo I es 0.05 (o con el que nosotros queramos trabajar, ). H0: El dado no está trucado (todas las caras igual probabilidad 1/6) H1: El dado está trucado (alguna cara no tiene probabilidad 1/6)

o bien, si se hacen n lanzamientos


```
## 
##  Chi-squared test for given probabilities
## 
## data:  c(20, 14, 23, 12, 26, 25)
## X-squared = 8.5, df = 5, p-value = 0.1307
```
### 1.5.2 Distribuciones Continuas: contraste Kolmogorov-Smirnov.

Este contraste se basa en la convergencia casi segura de la función de distribución empírica a la función de distribución teórica. Este resultado se denomina en muchos textos *Teorema Fundamental de la Estadística*.

La función de distribución empírica se construye como sigue:

1. Se ordenan los valores de la muestra de menor a mayor


2.- La función de distribución empírica se define como:


El teorema fundamental de la estadística (Glivenko-Cantelli) indica que conforme aumenta el tamaño de muestra, la función de distribución empírica converge a la función de distribución teórica en cualquier punto .


3.- Simulamos 30, 100, 200 valores de una distribucióne exponencial de tasa 1 y observamos se aproximan las correspondientes funciones de distribución empíricas a la función de distribución teórica de la .

```
xx<-seq(0,8,0.01)
set.seed(20)
simu<-rexp(200,1)
plot(xx,pexp(xx,1),type="l",col="black",lwd=2)
lines(ecdf(simu[1:30]),col="red")
lines(ecdf(simu[1:50]),col="green")
lines(ecdf(simu[1:100]),col="blue")
legend("bottomright",leg=c("teor", "n=30","n=50","n=100"),lty=1, col=c("black","red","green","blue"))
```
1. Se considera el estadístico , y con el valor observado se realiza el contraste kolmogorov-Smirnov, siempre que se tenga un tamaño de muestra adecuado. Vamos a efectuar el contraste con los 50 primeros datos y obtenemos un estadístico D=0.62 y el p-valor que acepta la distribución exponencial de tasa 1 pero no la de tasa 0.002.

```
## 
##  Exact two-sample Kolmogorov-Smirnov test
## 
## data:  simu[1:50] and pexp(1)
## D = 0.62, p-value = 0.7843
## alternative hypothesis: two-sided
```
```
## 
##  Exact two-sample Kolmogorov-Smirnov test
## 
## data:  simu[1:50] and pexp(0.002)
## D = 1, p-value = 0.03922
## alternative hypothesis: two-sided
```
#### 1.5.2.1 Distribuciones Continuas: contrastes de normalidad.

Los contrastes de bondad de ajuste más importantes de la teoría estadística son los de normalidad. Eso se debe a que muchas técnicas estadísticas requieren la hipótesis de normalidad de los datos para ser válidas.

Puesto que la normal es una distribución continua, el contraste de Kolmogorov-Smirnov es adecuado siempre que haya un número suficiente de datos para que se dé la convergencia del Teorema Fundamental. Como hay muchos estudios que por su coste no tienen la posibilidad de acumular un grán número de datos, se han desarrollado contrastes alternativos de gran potencia para cubrir los contrastes de normalidad con pocos datos.

- Si el contraste de Shapiro-Wilk es de los más potentes ( es una varianza ponderada por la cercanía a la normal)
- Si utilizamos el contraste de Kolmogorov-Smirnov que tabula el valor de , si este valor es muy grande, rechaza la hipótesis de normalidad. Si desconocemos la media y la desviación típica de la normal con la que contrastamos, se utiliza el test con la corrección de Lilliefords.

```
set.seed(20)
simu<-rnorm(100, 2,3)
library(nortest)#hay que cargar este paquete pues no está introducido en los comandos básicos.
shapiro.test(simu[1:20])#es el adecuado en este caso pues n=20<50
```
```
## 
##  Shapiro-Wilk normality test
## 
## data:  simu[1:20]
## W = 0.96356, p-value = 0.6172
```
`ks.test(simu[1:60], "pnorm")#sirve para contrastar otras continuas ("pt", "pexp",....), pero hay que proporcionar los valores de media y desviación````
## 
##  Exact one-sample Kolmogorov-Smirnov test
## 
## data:  simu[1:60]
## D = 0.48929, p-value = 9.104e-14
## alternative hypothesis: two-sided
```
```
## 
##  Lilliefors (Kolmogorov-Smirnov) normality test
## 
## data:  simu[1:60]
## D = 0.059407, p-value = 0.8634
```
**Gráficos prospectivos.**

Antes de plantear un contraste, especialmente si no hay ninguna información sobre la distribución de la variable de interés, es conveniente hacer algún gráfico que oriente al investigador sobre la hipótesis nula del contraste. Todos los gráficos son bien conocidos.

`## [1]  7 29``## [1]  7 29`
Nos detenemos brevemente en el gráfico qqPlot, que es muchas veces utilizado con el mismo rango que un contraste. La razón es que en el comando hay que explicitar una distribución de comparación. El fundamento teórico de este gráfico está muy relacionado, también, con el Teorema Fundamental de la Estadística. El gráfico qqplot relaciona los cuartiles de la distribución teórica que comparamos con la distribución empírica de los datos. Cada punto viene a representar , donde es el percentil de la distribución teórica aunque los software estadísticos hacen pequeñas modificaciones en torno a este percentil para hacer dibujos más robustos (por ejemplo, R calcula .

Si los puntos quedan sobre una línea recta es que la distribución propuesta es la adecuada. Obviamente, esto no sucede nunca en la práctica por lo que el software proporcina unas bandas de aceptación de modo que si más de un 5% de puntos salen de ellas, la distribución propuesta se rechaza. En el ejemplo se observa cómo se aceptaría el caso de la normal y no el de la exponencial, lo cual es correcto pues los datos que se representan proceden de una normal simulada.

**Transformaciones para obtener normalidad.**

Si una variable no tiene distribución normal, puede realizarse una transformación para que la nueva variable obtenida sí que tenga distribución normal. Esta operación no es recomendable que se aplique en la inferencia básica (intervalos y contrastes) puesto que si en general . En consecuencia, si no tiene distribución normal y un contraste sobre requiere normalidad, aunque encontramos una transformación tal que sea normal, un intervalo de confianza para no lleva a concluir que sea un intervalo de confianza para puesto que . Observa que el nuevo intervalo deja de ser centrado en con el efecto en el error del intervalo que es muy importante en la práctica.

Sin embargo, la transformaciones a la normalidad son habituales en la modelización estadística que estudiaremos en el siguiente tema. El objetivo de la modelización va más allá de estudiar parámetros concretos de la distribución de una variable, puesto que pretende formular modelos matemáticos con cierto error que permitan explicar y predecir fenómenos reales. La transformación a la normalidad más habitual es la denominada de Box-Cox. Aunque aparece de distintas maneras en los textos, esencialmente es


La mayoría de software estadísticos disponen de rutinas que buscan el valor adecuado. Observa que si hay que entender que no hay transformación posible a la normalidad pues la fórmula no cambia los datos originales. En este curso, y muchas veces en la práctica, consideraremos transformaciones que permitan interpretaciones fáciles como , , , y, sobre todo, , .

El siguiente ejemplo ilustra el procedimiento.

```
set.seed(20)
simul<-exp(rnorm(50))# trasnformamos con una exponencial los datos de una normal 0, 1
summary(powerTransform(simul, family="bcnPower"))#buscamos el valor lambda de la transformación box-cox
```
```
## bcnPower transformation to Normality 
## 
## Estimated power, lambda
##       Est Power Rounded Pwr Wald Lwr Bnd Wald Upr Bnd
## simul    0.0435           0      -0.2126       0.2996
## 
## Location gamma was fixed at its lower bound
##       Est gamma Std Err. Wald Lower Bound Wald Upper Bound
## simul       0.1       NA               NA               NA
## 
## Likelihood ratio tests about transformation parameters
##                              LRT df         pval
## LR test, lambda = (0)  0.1116321  1 7.382936e-01
## LR test, lambda = (1) 44.7539304  1 2.234180e-11
```
`## [1]  3 32``## [1]  7 29`
**Nota:** Una ventaja muy importante de la transformación logarítmica se encuentra en la interpretación de la pendiente cuando relacionamos linealmente una variable en datos brutos y en datos transformados logarítmicamente. Vamos a desarrollar esta idea.

Para dos parámetros y constantes, si escribimos sabemos que , es decir, informa de lo que varía por cada unidad de aumento de .

Si escribimos la misma ecuación en términos de logaritmos, entonces, asumiendo las condiciones adecuadas para hacer válidas las aproximaciones, se tiene Es decir, cuando relacionamos dos variables en términos logarítmicos, la pendiente nos informa de la elasticidad de la variable Y sobre la X, es decir, ante un 1% de variación de la variable la variable varía un |b|%. En teoría económica si decimos que la variable es inelástica respecto a la (Y:consumo de pan, X:precio del pan, como el pan es un bien básico, una variación de su precio generará una variación en menor proporción de su demanda), mientras que si es elástica (Y: consumo de coches eléctricos, X: precio del coche eléctrico, una variación del precio del coche eléctrico es esperable que genere una variación en mayor proporción de su consumo).

Es importante reflexionar sobre cómo interpretar en las siguientes situaciones: y .

## 1.6 Contraste de asociación

Es importante entender el concepto de asociacion entre dos variables cualitativas e por su gran uso en la práctica. Muchas informaciones que recibimos hacen uso de la asociación sin utilizar datos e, incluso, haciendo un mal uso del concepto. Fue la controversia sobre la eficacia de las vacunas contra el COVID la que evidenció el desconocimiento del concepto de asociación entre variables. Incluso fue necesario que los gobiernos publicaran notas de prensa para evitar los malosentendidos.

Aunque estudiaremos de modo más técnico el concepto de asociación, se puede entender bien a partir del gráfico. Observamos en el gráfico izquierdo que del total (36 figuras) hay 33 vacunados 33/36=91.7% y por tanto un 8.3% no está vacunado. En el gráfico central observamos que ingresados hay 7 (tienen la marca del covid), es decir, 7/36=19% del total, de los cuales 5 están vacunados: 5/7=71% está vacunado. El gráfico de la derecha indica que de los vacunados (33), 5 se han sido ingresados; esto es, 5/33=15%; mientras que de los no vacunados han sido ingresados el 66%=2/3.

Todos los porcentajes escritos son correctos, y cada uno ellos podría llevar a un titular de periódico. Por ejemplo, “el 71% de los ingresados está vacunado”, pero con esta frase NO se puede hacer una asociación entre vacuna e ingreso, hay que compararla con el porcentaje de vacunados que es 91.7%. Esto indica que el porcentaje de ingresados vacunados está muy por debajo del porcentaje total de vacunados que hay en la población. La asociación EXIGE una comparación entre dos porcentajes, uno del total de la población frente al porcentaje en un subgrupo de la población.

Otra manera de ver más clara la asociación sin duda es decir de la población se ingresa al 19%, pero dentro de la población de no vacunados ese porcentaje se eleva al 66%.

Primero hay que entender la forma en que se proporciona la información conjunta de dos variables cualitativas que es mediante el uso de la tabla de contingencia.

El contraste que nos interesa es H0: X e Y no están asociadas, o bien H_0: X e Y son independientes. Como sabemos de Estadística I, si e fueran independientes entonces para cualquier


De nuevo el estadístico de contraste es el ya que debemos comprobar casilla a casilla si es igual a la proporción que habría bajo independencia . En este caso los grados de libertad son .

### 1.6.1 Ejercicios modelo

**Ejemplo 1**

Si volvemos ahora al ejemplo de la noticia, vamos a dar un procedimiento que permita sistematizar el estudio de la asociación.

*Paso 1*: Los datos se introducen en una tabla de contingencia, como el gráfico es un pictograma, asumimos que cada figura representa a 10 personas (podría tomarse cualquier número, aunque hay que procurar que cada casilla de la tabla de contingencia tenga al menos 5 individuos para evitar errores en las aproximaciones)

Estamos relacionando las variables binarias estar vacunado , estar hospitalizado

```
tabla<-matrix(c(50, 280,20, 10), 2, 2, byrow=TRUE)#se introduce por filas
dimnames(tabla)<- list("A: vacunado"=c("A", "NoA"), "B: Hospitalizado"=c("B", "NoB"))#orden opcional, pero en este ejemplo viene bien para las explicaciones
print(tabla)
```
```
##            B: Hospitalizado
## A: vacunado  B NoB
##         A   50 280
##         NoA 20  10
```
*Paso 2*: Ahora debe confirmarse la asociación. El contraste  contrasta casilla a casilla si el número de individuos es compatible con una situación de no asociación, es decir 


Este estadístico se utiliza para resolver el contraste con “no hay asociación entre las variables”~“hay independencia entre las variables”

```
## 
##  Pearson's Chi-squared test with Yates' continuity correction
## 
## data:  tabla
## X-squared = 43.361, df = 1, p-value = 4.551e-11
```
Se tiene que proporciona un p-valor prácticamente nulo, es decir, hay evidencias de asociación. En tal caso hay que buscar el sentido de la asociación y se va al paso 3.

*Paso 3*: Observemos que la asociación entre dos sucesos significa  o , observa lo importante que es comparar estas dos cantidades de modo coherente, es un error grave comparar, por ejemplo,  con  o  con .

Ahora buscamos en las tablas la discrepancia mayor entre alguna de estas cantidades.

```
##          B  NoB Total
## A     13.9 77.8  91.7
## NoA    5.6  2.8   8.3
## Total 19.4 80.6 100.0
```
```
##            B: Hospitalizado
## A: vacunado    B  NoB Total Count
##         A   15.2 84.8   100   330
##         NoA 66.7 33.3   100    30
```
```
##            B: Hospitalizado
## A: vacunado     B   NoB
##       A      71.4  96.6
##       NoA    28.6   3.4
##       Total 100.0 100.0
##       Count  70.0 290.0
```
Hemos denotado A=*estar VACUNADO* y B=*estar HOSPITALIZADO*, entonces

POR FILAS: , ;la diferencia supera los 10 puntos e indica que el 19.4% del total está hospitalizado pero dentro de los NO VACUNADOS () este porcentaje se eleva hata el 66.7%, se deduce que la probabilidad de ser hospitalizado es mayor entre los no vacunados que en la población general.

POR COLUMNAS: , , la diferencia supera los 10 puntos e indica que el 91.7% de la población está vacunada, pero en el grupo de los hospitalizados este porcentaje se reduce hasta el 71.4%, de donde se sigue que la vacunación se relaciona con una reducción en el porcentaje de hospitalizados.

Por supuesto que hay otras muchas comparaciones, pero las dos que hemos escogido son suficientes para dar una buena visión de la asociación entre variables. Por ejemplo también podría escribirse y P(A^c| B )=28.6, el 8.3% de la población no está vacunada, pero en los hospitalizados esa proporción se eleva hasta el 28.6%, lo que indica un aumento del riesgo de que una persona esté no vacunada dentro de los hospitalizados que en la población general. Pero esta información quedaba bien recogida en las comparaciones seleccionadas más arriba.

**Ejemplo 2** Queremos estudiar si hay relación entre el tipo de instalación de las gasolineras (X: 1- básica; 2- estándar, 3- moderna) y la política de precios (Y: 1- agresiva, 2- neutral, 3- no agresiva).

| x | 1 | 2 | 3 | 
|---|---|---|---|
| 1 | 24 | 15 | 17 | 
| 2 | 52 | 73 | 80 | 
| 3 | 58 | 86 | 36 | 

```
tabla<-matrix(c(24,15,17,52,73,80,58,86,36), 3, 3, byrow=TRUE)#se introduce por 
chisq.test(tabla)#efectuamos el contraste de independencia
```
```
## 
##  Pearson's Chi-squared test
## 
## data:  tabla
## X-squared = 22.476, df = 4, p-value = 0.0001611
```
Observamos que se rechaza la independencia, es decir, hay asociación entre el precio en la gasolinera y las instalaciones que tiene. Ahora con los perfiles de fila o de columna se establece el sentido de la asociación.

```
library(Rcmdr)#Rcmdr tiene un procedimiento cómodo para obtener perfiles
#perfiles totales
totPercents(tabla)
```
```
##          1    2    3 Total
## 1      5.4  3.4  3.9  12.7
## 2     11.8 16.6 18.1  46.5
## 3     13.2 19.5  8.2  40.8
## Total 30.4 39.5 30.2 100.0
```
```
##      1    2    3 Total Count
## 1 42.9 26.8 30.4 100.1    56
## 2 25.4 35.6 39.0 100.0   205
## 3 32.2 47.8 20.0 100.0   180
```
```
##           1     2     3
## 1      17.9   8.6  12.8
## 2      38.8  42.0  60.2
## 3      43.3  49.4  27.1
## Total 100.0 100.0 100.1
## Count 134.0 174.0 133.0
```
```
##                                         Sum
##      5.442177  3.401361  3.854875  12.69841
##     11.791383 16.553288 18.140590  46.48526
##     13.151927 19.501134  8.163265  40.81633
## Sum 30.385488 39.455782 30.158730 100.00000
```
```
##          [,1]     [,2]     [,3]
## [1,] 42.85714 26.78571 30.35714
## [2,] 25.36585 35.60976 39.02439
## [3,] 32.22222 47.77778 20.00000
```
```
##          [,1]     [,2]     [,3]
## [1,] 17.91045  8.62069 12.78195
## [2,] 38.80597 41.95402 60.15038
## [3,] 43.28358 49.42529 27.06767
```
Si interpretamos con los perfiles fila observamos que en el total: el 30.4% de gasolineras tienen políticas agresivas, el 39.4% no agresivas y el 30.2% neutrales. Entonces, es claro que hay una asociación de gasolineras básicas con políticas agresivas pues hay más de 10 puntos porcentuales por encima de los esperados (42.9%). Finalmente, las de instalaciones modernas tienden a una menor política de precios “no agresivas” (20%) respecto a la proporción global (30.2%). Por otra parte en las gasolineras estándar hay una tendencia a la asociación con políticas no agresivas pues supera en 9 puntos porcentuales el valor global del 30.2%, aunque no llega a los 10 puntos que nos hemos marcado como diferencia.

De modo similar se haría el análisis con perfiles columna.

```
##          1    2    3 Total
## 1      5.4  3.4  3.9  12.7
## 2     11.8 16.6 18.1  46.5
## 3     13.2 19.5  8.2  40.8
## Total 30.4 39.5 30.2 100.0
```
```
##           1     2     3
## 1      17.9   8.6  12.8
## 2      38.8  42.0  60.2
## 3      43.3  49.4  27.1
## Total 100.0 100.0 100.1
## Count 134.0 174.0 133.0
```
```
##                                         Sum
##      5.442177  3.401361  3.854875  12.69841
##     11.791383 16.553288 18.140590  46.48526
##     13.151927 19.501134  8.163265  40.81633
## Sum 30.385488 39.455782 30.158730 100.00000
```
```
##          [,1]     [,2]     [,3]
## [1,] 17.91045  8.62069 12.78195
## [2,] 38.80597 41.95402 60.15038
## [3,] 43.28358 49.42529 27.06767
```
Por columnas, observamos que aunque en la población hay un 46% de gasolineras estándar, dentro de los que practican políticas no agresivas este porcentaje se dispara al 60%, lo que indica una asociación en el sentido de que las gasolineras estándar tienden a tener una mayor proporción de políticas de precios no agresivas.

En general hay que buscar la mayor divergencia que se pueda encontrar entre y , donde y son sucesos diferentes.

## 1.7 Estadística no paramétrica

En esta sección estudiaremos contrastes alternativos a los contrastes analizados en las dos primeras secciones. Los contrastes que hemos estudiado hasta el momento se refieren a la media ( o, en el caso de binarias, ). Ahora bien, estos contrastes, cuando el tamaño muestral es pequeño, requieren normalidad. Si no hay normalidad, como ya se ha indicado, no es conveniente la transformación de los datos para la normalidad porque las conclusiones pueden ser erróneas.

Las técnicas no paramétricas que aprenderemos en esta sección se aplican a variables continuas cuya distribución no sea excesivamente asimétrica.

Las técnicas paramétricas son, en general, más potentes que las no paramétricas; por lo que si se cumplen las condiciones deben aplicarse. En esta sección la hipótesis no se escribe con la media, como era de esperar, sino con la mediana .

Un rango es la posición que ocupa un dato de las observaciones muestrales cuando estas se ordenan de menor a mayor. Las técnicas que aprenderemos en esta sección no trabajan directamente con las observaciones sino con los rangos, por lo que se denominan también contrastes de rangos.


### 1.7.1 Wilcoxon para una variable

Nos planteamos si la distribución de una variable está centrada en el valor .

Ilustramos el procedimiento con un ejemplo

Tras realizar 3 experimentaciones obtenemos los valores . Nos planteamos el contraste .

Paso 1: Restamos a cada dato y obtenemos

Paso 2: Asignamos rangos a los valores absolutos de las diferencias

Paso3: Estadístico de Wilcoxon: es la suma de los rangos de los valores positivos en el paso 1.

Paso 4: Decisión: se debe obtener la tabla que calcula la distribución de masa de probabilidad de W.

| 1 | 2 | 3 | W | P | 
|---|---|---|---|---|
| - | - | - | 0 | 1/8 | 
| + | - | - | 1 | 1/8 | 
| - | + | - | 2 | 1/8 | 
| - | - | + | 3 | 1/8 | 
| + | + | - | 3 | 1/8 | 
| + | - | + | 4 | 1/8 | 
| - | + | + | 5 | 1/8 | 
| + | + | + | 6 | 1/8 | 

Si la hipótesis nula es cierta, tan probable es que salga un numero mayor que 4 que menor que 4, por lo que los signos son + o - con igual probabilidad. Cada ordenación tiene como probabilidad 1/8, por lo que . Con esto concluimos que el contraste no es significativo. En R se plantea de modo similar a un t.test.

```
## 
##  Wilcoxon signed rank exact test
## 
## data:  datos
## V = 3, p-value = 0.625
## alternative hypothesis: true location is greater than 4
```
Aprovecha este ejercicio sencillo para reflexionar sobre las ventajas e inconvenientes de las técnicas no paramétricas. Observa que apenas requiere condiciones,el procedimiento no descansa en resultados teóricos complejos y responde a una lógica sencilla. Sin embargo, pierde mucha información porque no trabaja con los valores originales, sino con los rangos; además, según el valor la tabla para obtener el p-valor cambia y se hace inmanejable a partir de 5 datos. Esto último conlleva a que deban ser resueltos con software. Por otra parte, conforme va creciendo la distribución del estadístico va siendo normal, por lo que la aproximación a la normal facilita el tiempo de cálculo. Asimismo, conforme crece va adquieriendo más potencia y llegan a ser tan potentes como los paramétricos.

### 1.7.2 Wilcoxon para observaciones pareadas

El procedimiento es similar al t.test de observaciones pareadas pues, usando la misma notación, debe calcularse la variable diferencia y, con las observaciones de , proceder como con el test de Wilcoxon con una variable para resolver . La hipótesis habitual es con que, literalmente, plantea si la variables y la variable tiene una misma distribución cuando se observan en una misma población.

### 1.7.3 Wilcoxon para observaciones independientes o contraste de Mann-Whitney

En este caso nos planteamos como se distribuye una variable en dos poblaciones distintas y . El planteamiento habitual es y literalmente se escribiría la variable se distribuye igual en ambas poblaciones. Si la alternativa es diríamos que la distribución de en la población se mueve a la derecha que en la población . Conviene reflexionar sobre esta frase, otra forma de entenderla es que la variable en toma con mayor probabilidad valores por encima de cualquier valor por encima de la mediana de .

### 1.7.4 Kruskal-Wallis y ANOVA: comparación de una variable en tres o más poblaciones

En este caso nos planteamos como se distribuye una variable en tres o más poblaciones distintas . Denotamos a la variable cuando se observa en la población , con . El contraste se plantea como sigue:

Para resolver el contraste anterior se puede aplicar una técnica paramétrica denominada ANOVA que impone las siguientes restricciónes:

R1: , se distribuye como una normal en cada población.

R2: La varianza de es la misma en todas las poblaciones.

Ambas restricciones son habituales en el contraste con observaciones independientes. La primera justifica el uso del estadístico varianza muestral para las comparaciones (como veremos más adelante en el curso, los contrastes no se hacen con la media, como podría indicar la intuición, sino con la varianza, de ahí el nombre de análisis de la varianza). Recuerda que para que podamos garantizar que es necesario que para cualquier tamaño de muestra. La segunda condición da potencia a la técnica pues, como vimos, comparar normales con distinta varianza da lugar a técnicas poco potentes. Existe un ANOVA donde R2 no se satisface, pero penaliza los grados de libertad dando lugar a una técnica menos potente; la idea es similar a la que vimos a utilizar la fórmula de Welch en el t.test con observaciones independientes.

En cualquiera de las dos técnicas, si se rechaza la hipótesis nula deben ordenarse las distribuciones, en el caso no paramétrico, o las medias, en el caso paramétrico. Esto supone que haya que realizarse contrastes dos a dos. Si hiciéramos todos los contrastes dos a dos iríamos aumentando el error tipo I; por lo que las conclusiones serían poco fiables. Se han propuesto muchas técnicas que permiten realizar este análisis manteniendo el error tipo I, , que deseemos. Este análisis posterior al rechazo del test se denomina post hoc.

Este curso aplicaremos la técnica que por defecto proporciona R, aunque hay otras muchas. Una de ellas, la más conservadora, se denomina de Bonferroni. Consiste en lo siguiente. Denotamos , suponiendo que hay contrastes, cada contraste se resuelve con un error tipo I , con ello se garantiza un error tipo I global menor o igual que

Esta técnica es muy conservadora en el sentido de que rechazar una igualdad de medias requerirá mucha evidencia ya que el error tipo I puede llegar a ser muy pequeño. Esto da lugar a post-hocs que, aunque se haya rechazado la igualdad de medias, después no se pueda dar una ordenación de distribuciones o medias. En absoluto es una contradicción, sino una consecuencia de la preservación del error tipo I ante múltiples contrastes.

Hay una técnica algo mejor, que usa R por defecto, que se denomina el método de Holt. Consiste en realizar todos los contrastes y ordenar los p-valores de menor a mayor. Si el más pequeño es menor que , se rechaza esa igualdad, y al siguiente p-valor basta con exigirle ser menor que , y así sucesivamente.

Observa que la mayoría de software lo que hacen es ajustar el p-valor, es decir, en el caso de Bonferroni multiplican todos los p-valores de cada contraste dos a dos por , y, de esta manera, se sacan conclusiones como siempre, comparando con . En el caso de Holt se hace de modo similar, el p-valor menor se multiplica por , el penúltimo por y así sucesivamente. Los p-valores que se llaman ajustados se comparan con , del modo habitual.

**Ejemplo (avanzado)** El siguiente ejemplo considera unos datos inventados en los que se visualiza el procedimiento ANOVA para resolver .

Consideramos tres grupos (A, B y C) de observaciones independientes. Queremos contrastar con la técnica ANOVA. Observa que como asumimos normalidad y varianzas iguales (), bajo todas tienen una misma media . Entonces, ,, son tres observaciones de una variable , ya que son el promedio de normales. Por otra parte, si denominamos a la varianza de los tres promedios, obtenemos que . Los tres grupos tienen la misma varianza muestral, por lo que la varianza muestral promedio es . Así que finalmente, el cociente de ambas resulta 48 y su distribución, por ser el cociente de dos es . El gráfico ilustra con claridad el proceso de comparación de varianzas, que es la base del ANOVA, y la salida ANOVA resume la conclusión

```
data<-data.frame(A=c(1,2,3), B=c(5,6,7),C=c(9,10,11))
aa<-mean(data$A)
ba<-sd(data$A)
ab<-mean(data$B)
bb<-sd(data$B)
ac<-mean(data$C)
bc<-sd(data$C)
data<-stack(data)
names(data)<-c("X","G")
plot( data$X,rep(0,9),  pch = 19, cex = 1.5,  col = c(rep("red",3),rep("blue",3),rep("green",3)))
legend("bottom",c("A","B","C"),pch=19, col=c("red", "blue","green"))
points(c(aa,ab,ac), c(0,0,0), pch=5,cex=2,col=c("red", "blue","green"))
legend(7,-0.-0.55,c(expression(bar(A)),expression(bar(B)),expression(bar(C))),pch=5, col=c("red", "blue","green"))
a<-aa
b<-ba
x<-seq(a-1.5*b, a+1.5*b, 0.05)
lines(x,dnorm(x,a,b),col="red",type="l")
a<-ab
b<-bb
x<-seq(a-1.5*b, a+1.5*b, 0.05)
lines(x,dnorm(x,a,b),col="blue",type="l")
a<-ac
b<-bc
x<-seq(a-1.5*b, a+1.5*b, 0.05)
lines(x,dnorm(x,a,b),col="green",type="l")
a<-mean(c(aa, ab, ac))
b<-sd(c(aa, ab, ac))*sqrt(3)
x<-seq(a-2*b, a+2*b, 0.05)
lines(x,5*dnorm(x,a,b),col="black",type="l")
b<-expression(3%*%S^2 / S[A]^2==48)
text(2,-0.5,b )
abline(h=0)
```
```
##             Df Sum Sq Mean Sq F value   Pr(>F)    
## data$G       2     96      48      48 0.000204 ***
## Residuals    6      6       1                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```
### 1.7.5 Friedman y ANOVA MR: comparación de tres o más variables en una misma población

Se trata de la extensión del contraste de dos variables con observaciones pareadas. El contraste de Friedman es no paramétrico y se puede plantear como el de Kruskal-Wallis, con la diferencia de que ahora cada subíndice representa una variable y NO una población.

El correspondiente contraste paramétrico se denomina ANOVA con medidas repetidas. Para poderlo aplicar también se deben comprobar previamente tres condiciones

R1: Normalidad de cada variable,

R2: esfericidad: corresponde con la idea de que no varíe la varianza de la variable diferencia de cualquier par de variables: para cualquier par y se comprueba con el contraste de Mauchly.

R3: si falla la esfericidad se puede aplicar la técnica pero los p-valores sufren una corrección, hay varias en la literatura estadística pero únicamente consideraremos la denominada Greenhouse-Geisser.

La normalidad se justifica por el uso de la normalidad en el estimador a la hora de comparar los grupos de poblaciones, como ocurre en el ANOVA con observaciones independientes. La esfericidad responde a la idea de que con observaciones pareadas las variables que se comparan son las diferencias entre cada par de variables, y todos los pares de diferencias deben tener la misma varianza. Cuando falla esta hipótesis hay correcciones como la indicada en R3 que siguen haciendo válida la técnica aunque con menor potencia.

Por supuesto, en ambos casos, si se rechaza la hipótesis nula habrá que realizar un contraste post-hoc con las mismas observaciones realizadas en el apartado anterior.

### 1.7.6 Correlación de Spearman

En lo que llevamos de sección hemos relacionado una variable cualitativa y otra cuantitativa (t.test, wilcox.test, ANOVA etc con observaciones independientes), dos variable cualitativas (test de igualdad de proporcionas, contrastes de asociación) y dos variables cuantitativas, (t.test, ANOVA, Friedman con medidas repetidas).

Es interesante extender la idea de asociación entre dos cualitativas, a la de dos cuantitativas que denotamos e . En este caso se denomina correlación de variables. Puesto que ambas variables son continuas, puede dibujarse para cada individuo observado el par , con lo que obtenemos una representación denominada diagrama de dispersión o nube de puntos. El concepto de correlación responde, de manera muy amplia, a la idea de cuánto se asemeja ese diagrama a una recta. Es claro que nunca será una recta, pero ¿se puede abstraer una recta del gráfico?. En Estadística I se estudió este concepto y se denominó recta de regresión a la mejor recta que podría ajustarse a la nube de puntos.

es la recta de regresión. La medida del grado de relación lineal entre ambas variables se denomina coeficiente de correlación de Pearson, . Este coeficiente toma valores entre -1 y 1, y nos informa de la proporcion de varianza de la variable que es recogida por la recta de regresión, por lo que cuanto más cercano sea a uno, mejor ajuste de la recta a la nube de puntos.

El ajuste de una nube de puntos a una recta no es más que un ejercicio de optimización que se estudia en un curso básico de Cálculo. No es un planteamiento plenamente estadístico. Este curso cobra una especial importancia porque nos planteamos no solo el ajuste sino la posibilidad de que efectivamente la variable explique a la linealmente con un error que controlaremos. Es la incorporación del término de error y su estudio lo que cambiará por completo el ajuste lineal a un modelo estadístico. Será el primer modelo estadístico que como tal se presentará a los estudiantes, aunque prácticamente todo lo estudiado hasta ahora son modelos lineales básicos que no se formulan como tal para facilitar la presentación de contenidos.

En esta sección nos planteamos si dos variables cuantitativas e están relacionadas directa o indirectamente, es decir, al aumentar una, la otra aumenta o dismimuye. Es un planteamiento NO paramétrico, puesto que no hay ningún modelo por detras que trate de relacionar ambas variables. Se trata de calcular una medida que se denomina coeficiente de correlación de Spearman y lo escribiremos .

El cálculo de consiste en asignar rangos a y a , que denotamos y , respectivamente. es el coeficiente de correlación de Pearson entre y .

**Ejemplo** Dos jueces realizan una ordenación de 3 candidatos asignándoles una puntuación de 0 a 10. Al candidato 1 le asignan las puntuaciones 3, 7; al candidato 2 las puntuaciónes 5, 4; al candidato 3 las puntuaciones 8, 6; donde se indica primero la calificación del juez 1. ¿Hay alguna relación entre ambas ordenaciones?

Observemos que los rangos de las calificaciones del juez 1 son 1, 2, 3 y las del juez 2 son 3, 1, 2. Una vez calculado obtenemos el valor -0.5 que, si hubiera que interpretarlo nos diría que hay una relación ténue e inversa entre las calificaciones de ambos jueces. Sin embargo, no todos los son susceptibles de interpretación. Es conveniente aplicar un contraste que nos indique si puede considerarse no nulo el valor obtenido y, en tal caso, interpretarlo.

El contraste no requiere ninguna condición para ser aplicado pues es un contraste de aleatorización que, con la capacidad de cálculo actual de los ordenadores, es una técnica cada vez más habitual en estadística.

El contraste es fácil de entender en este caso, por eso se aprovecha esta sección para presentarlos. La idea es considerar todas las posibles disposiciones de rangos y y calcular en cada una. Si la hipótesis nula es cierta, todas las disposiciones son igualmente probables, por tanto, ordenando todos los valores de veríamos la cola que deja a su izda (si es negativo) o a su derecha, si es positivo.

En nuestro problema como hay tres individuos, tenemos 3!*3!=36 posibles disposiciones de los rangos, cada una con un valor que habría que calcular.

| Rx | Ry | Rx | Ry | … | … | Rx | Ry | 
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 |  |  | 3 | 3 | 
| 2 | 2 | 2 | 1 |  |  | 2 | 2 | 
| 3 | 3 | 3 | 3 |  |  | 1 | 1 | 

Cada disposición, bajo la hipótesis nula de no relación, puede aparecer con igual probabilidad , luego . Es importante entender el procedimiento y la carga computacional que supone. Además, puede haber empates en las valoraciones, lo que implica modificaciones en la fórmula que todavía hacen más complejo el cálculo.

```
## 
##  Spearman's rank correlation rho
## 
## data:  x and y
## S = 6, p-value = 1
## alternative hypothesis: true rho is not equal to 0
## sample estimates:
##  rho 
## -0.5
```
Observamos que pero no puede interpretarse ya que no se rechaza la hipótesis . Si se interpretara reflejaría un relación débil e inversa entre ambas ordenaciones.

## 1.8 Cuestiones de investigación a partir de una base de datos

Como se indicó en la sección 1.1, este tema incorpora a las técnicas inferenciales aprendidas en Estadística I otras que, si bien siguen una misma filosofía, cubren situaciones que, por la naturaleza de los datos, impiden aplicar las técnicas básicas.

Para poder hacer frente a este planteamiento es necesario ponerse en una situación lo más realista posible en un contexto de investigación académica. Para ello, consideramos una base de datos suficientemente amplia que permita ilustrar el tipo de cuestiones que se plantean en un estudio y las limitaciones de las técnicas estadísticas aprendidas hasta el momento.

***Contexto del problema***: La enseñanza del español para extranjeros ha cobrado una gran importancia tanto a nivel cultural como económico. Los lingüistas tienen interés en establecer qué aspectos afectan a la motivación y al esfuerzo invertido en el aprendizaje de la lengua española.

***Características técnicas de la recogida de datos*** : se toma una muestra representativa de 97 estudiantes de español para extranjeros que responden a una encuesta. Estudiaremos algunas de las variables de dicha encuesta. Las variables continuas que aparecen en la tabla se obtienen tras sumar varios ítems que contestaron los estudiantes y que valoraban de 1 a 5 según el grado de acuerdo (de nada de acuerdo a total acuerdo).

| VARIABLE | Explicación | 
|---|---|
| motivacion | Mide el deseo por aprender el español: 11=ningún deseo a 55=mucho deseo | 
| GradoMotiv | Mide el esfuerzo realizado en el curso de aprendizaje del español: 7=ningún esfuerzo a 40=todo el esfuerzo posible | 
| AHE | Mide la actitud hacia España, toma valores de 4=mala a 28=excelente | 
| AHLE | Mide la actitud hacia la lengua española: de 4=mala a 28=excelente | 
| AHPE | Mide la actitud hacia los españoles, valores: de 4=mala a 28=excelente | 
| Zona | Zona de influencia cultural del estudiante (5 categorías): Brasil, Angsx= anglosajón, Europa, SEasia=Sudeste Asiático, Musulm=Musulmana | 
| Nivel | Nivel en la lengua española al comenzar el curso: A1, A2, B1, B2, C1 | 
| Uso | Uso de la lengua española fuera de las clases: bajo (menos del 20% de su tiempo), alto (más del 20% de su tiempo). | 
| Utilizacion | Utilización más detallada de la lengua española en su vida cotidiana: a_menos20=<20%, b_20_40=20%-40%, c_40_60=40%-60%, c_60_80=60%-80%, c_mas80=>80% | 

Asimismo, te presentamos a continuación las primeras líneas de la base de datos.

`| |Nivel | Utilizacion | Zona | motivacion | GradoMotiv | Uso | AHE | AHLE | AHPE | | 1 | B2 | c_40_60 | Angsx | 47 | 27 | alto | 24 | 19 | 22 |  | 2 | B1 | c_mas80 | Angsx | 46 | 21 | alto | 23 | 19 | 19 | | 3 | B2 | c_60_80 | Angsx | 53 | 27 | alto | 26 | 21 | 26 | | 4 | B2 | c_60_80 | Angsx | 44 | 15 | alto | 23 | 17 | 23 | | 5 | B2 | b_20_40 | Europa | 48 | 27 | alto | 25 | 21 | 24 |`
1. Variables Cualitativas: Nivel, Utilización (podrías considerarse ordinal), Zona, Uso (binaria)
2. Variables Cuantitativas: motivacion, GradoMotiv, AHE, AHLE, AHPE Hay que tener claro que el experto en este problema es un lingüista y se plantearía cuestiones más técnicas que algunas de las que plantearemos aquí. No obstante, el contexto resulta cercano como para poder plantear cuestiones. ***Ejercicio***

A continuación se presenta una batería de preguntas. Cada una debe responderse con la técnicas estadística más adecuada.

1. Cuestiones para el análisis univariante ¿Cuál es la zona cultural más habitual en el aprendizaje de español por extranjeros (AEE)? ¿Cómo se distribuye el nivel con el que se inscriben al AEE? ¿Qué criterios podrían utilizarse para establecer el colectivo más motivado y menos motivado ? ¿Se puede decir que el grado de motivación (que es un reflejo del aprovechamiento del programa) se distribuye siguiendo la clásica campana de Gauss (normalidad)?
2. Cuestiones que implican a más de una variable ¿El deseo de aprender español se distribuye igual en las zonas de influencia cultural? ¿Las variables AHE, AHLE tienen medias poblacionales iguales? ¿Los estudiantes con un Uso alto de la lengua tienen mejor actitud hacia la lengua española que los estudiantes con un uso bajo? ¿Las variable AHE, AHLE, AHPE tienen una distribución similar? ¿La actitud hacia la lengua española tiene una relación directa o inversa con la motivación? ¿Hay alguna asociación entre el nivel con el que se inscriben los estudiantes y la Utilización que hacen de la lengua en la vida cotidiana? Dentro de los estudiantes con un Uso alto de la lengua, los de nivel B1 están más motivados que los de nivel B2 pero esta situación es la contraria entre los estudiantes de Uso bajo de la lengua. ¿Interactúan las variables Uso y nivel? Una universidad quiere encontrar un modelo estadística que le permita predecir de manera lo más precisa posible el grado de motivación de un estudiante sabiendo su motivación, y su actitud hacia España, la Lengua Española y los españoles, respectivamente. Este modelo tendrá un peso importante en la admisión de un estudiante en el programa de lengua española para extranjeros. Se puede hacer una propuesta con buen soporte teórico? Todas las cuestiones anteriores deben responderse utilizando una técnica estadística que puede ser diferente ante una misma pregunta que implique a distintas variables ya que las técnicas estadísticas están sujetas a requerimientos teóricos que deben conocerse. Por ejemplo, la cuestión ¿se puede aceptar que la media poblacional de la variable grado de motivación es igual para cualquier nivel de utilización de la lengua?¿y la motivación?. Aunque ambas cuestiones son similares la técnica estadística a utilizar puede ser diferente según el comportamiento de las variables cuantitativas en cada grupo de la variable cualitativa. ```
## [1] "Nivel"       "Utilizacion" "Zona"        "motivacion"  "GradoMotiv" 
## [6] "Uso"         "AHE"         "AHLE"        "AHPE"
```
```
#¿Cuál es la zona cultural más habitual en el aprendizaje de español por extranjeros (AEE)?
barplot(table(data$Zona))
```
```
## 
##  Angsx Brasil Europa Musulm SEasia 
##     16      3     33     14     31
```
```
## 
## A1 A2 B1 B2 C1 
## 16 20 40 20  1
```
```
#¿Qué criterios podrían utilizarse para establecer el colectivo más motivado y menos motivado ?
boxplot(data$motivacion)
```
```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   29.00   39.00   44.00   43.45   48.00   55.00
```
```
##   5%  10%  25%  50%  75%  90%  95% 
## 32.8 36.0 39.0 44.0 48.0 51.0 52.2
```
```
#¿Se puede decir que el grado de motivación (que es un reflejo del aprovechamiento del programa) se distribuye siguiendo la clásica campana de Gauss (normalidad)?
library(nortest)
library(car)
lillie.test(data$GradoMotiv)
```
```
## 
##  Lilliefors (Kolmogorov-Smirnov) normality test
## 
## data:  data$GradoMotiv
## D = 0.098671, p-value = 0.02095
```
```
a<-mean(data$GradoMotiv)
b<-sd(data$GradoMotiv)
x<-seq(a-3*b, a+3*b, 0.05)
hist(data$GradoMotiv, freq =FALSE,xlim=c(a-3.5*b, a+3.5*b),ylim=c(0,0.12))
lines(x,dnorm(x,a,b),col="red",type="l")
```
`## [1] 49 43`

```
#¿El deseo de aprender español se distribuye igual en las zonas de influencia cultural?¿Y si no se considera Brasil?
    #quitar<-which(data$Zona=="Brasil")
a<-data$motivacion#[-quitar]
b<-data$Zona#[-quitar]
    by(a,b, shapiro.test)
```
```
## b: Angsx
## 
##  Shapiro-Wilk normality test
## 
## data:  dd[x, ]
## W = 0.94844, p-value = 0.4653
## 
## ------------------------------------------------------------ 
## b: Brasil
## 
##  Shapiro-Wilk normality test
## 
## data:  dd[x, ]
## W = 0.98684, p-value = 0.7804
## 
## ------------------------------------------------------------ 
## b: Europa
## 
##  Shapiro-Wilk normality test
## 
## data:  dd[x, ]
## W = 0.95814, p-value = 0.2289
## 
## ------------------------------------------------------------ 
## b: Musulm
## 
##  Shapiro-Wilk normality test
## 
## data:  dd[x, ]
## W = 0.96585, p-value = 0.8168
## 
## ------------------------------------------------------------ 
## b: SEasia
## 
##  Shapiro-Wilk normality test
## 
## data:  dd[x, ]
## W = 0.95808, p-value = 0.2594
```
```
## Levene's Test for Homogeneity of Variance (center = median)
##       Df F value Pr(>F)
## group  4  1.4936 0.2106
##       92
```
```
## 
##  Bartlett test of homogeneity of variances
## 
## data:  a by b
## Bartlett's K-squared = 4.7065, df = 4, p-value = 0.3188
```
```
##             Df Sum Sq Mean Sq F value Pr(>F)
## b            4    192   48.07   1.364  0.252
## Residuals   92   3242   35.24
```
```
  # ¿Las variables AHE, AHLE tienen medias poblacionales iguales?
    
    # no es necesario lillie.test(data$AHE-data$AHLE)
    summary(cbind(data$AHE,data$AHLE))
```
```
##        V1              V2       
##  Min.   :12.00   Min.   :12.00  
##  1st Qu.:22.00   1st Qu.:17.00  
##  Median :24.00   Median :19.00  
##  Mean   :23.47   Mean   :18.87  
##  3rd Qu.:25.00   3rd Qu.:21.00  
##  Max.   :28.00   Max.   :21.00
```
```
## 
##  Paired t-test
## 
## data:  data$AHE and data$AHLE
## t = 13.626, df = 96, p-value < 2.2e-16
## alternative hypothesis: true mean difference is greater than 0
## 95 percent confidence interval:
##  4.046534      Inf
## sample estimates:
## mean difference 
##        4.608247
```
```
    #pero el no paramétrico daría resultados similares
    wilcox.test(data$AHE, data$AHLE, alternative="greater",paired=TRUE)
```
```
## 
##  Wilcoxon signed rank test with continuity correction
## 
## data:  data$AHE and data$AHLE
## V = 4318.5, p-value = 1.627e-15
## alternative hypothesis: true location shift is greater than 0
```
```
   # ¿Los estudiantes con un Uso alto de la lengua tienen mejor actitud hacia la lengua española que los estudiantes con un uso bajo?
    table(data$Uso)
```
```
## 
## alto bajo 
##   75   22
```
```
## 
##  Lilliefors (Kolmogorov-Smirnov) normality test
## 
## data:  a
## D = 0.21787, p-value = 1.827e-09
```
```
## 
##  Shapiro-Wilk normality test
## 
## data:  b
## W = 0.87999, p-value = 0.01208
```
```
## 
##  Welch Two Sample t-test
## 
## data:  AHLE by Uso
## t = 1.5624, df = 32.751, p-value = 0.1278
## alternative hypothesis: true difference in means between group alto and group bajo is not equal to 0
## 95 percent confidence interval:
##  -0.2321085  1.7666540
## sample estimates:
## mean in group alto mean in group bajo 
##           19.04000           18.27273
```
```
## 
##  Welch Two Sample t-test
## 
## data:  AHLE by Uso
## t = 1.5624, df = 32.751, p-value = 0.0639
## alternative hypothesis: true difference in means between group alto and group bajo is greater than 0
## 95 percent confidence interval:
##  -0.06397991         Inf
## sample estimates:
## mean in group alto mean in group bajo 
##           19.04000           18.27273
```
`## Warning: package 'ez' was built under R version 4.4.3````
## 
##  Lilliefors (Kolmogorov-Smirnov) normality test
## 
## data:  data$AHE
## D = 0.1539, p-value = 6.313e-06
```
```
## 
##  Lilliefors (Kolmogorov-Smirnov) normality test
## 
## data:  data$AHLE
## D = 0.16907, p-value = 3.227e-07
```
```
## 
##  Lilliefors (Kolmogorov-Smirnov) normality test
## 
## data:  data$AHPE
## D = 0.09723, p-value = 0.02445
```
```
##       AHE             AHLE            AHPE      
##  Min.   :12.00   Min.   :12.00   Min.   :13.00  
##  1st Qu.:22.00   1st Qu.:17.00   1st Qu.:20.00  
##  Median :24.00   Median :19.00   Median :23.00  
##  Mean   :23.47   Mean   :18.87   Mean   :22.79  
##  3rd Qu.:25.00   3rd Qu.:21.00   3rd Qu.:26.00  
##  Max.   :28.00   Max.   :21.00   Max.   :28.00
```
```
    newdata<-stack(data[,7:9])
    names(newdata)<-c("response","factor")
    newdata$id<-rep(seq(1,length(data$AHE),1),3)#identificamos cada individuo para detectar la repetición
    ez<-ezANOVA(data=newdata, dv=response, wid=id, within=factor)
```
`## Warning: Converting "id" to factor for ANOVA.````
## $ANOVA
##   Effect DFn DFd        F            p p<.05       ges
## 2 factor   2 192 115.8323 1.006455e-33     * 0.3043885
## 
## $`Mauchly's Test for Sphericity`
##   Effect         W         p p<.05
## 2 factor 0.9881717 0.5682512      
## 
## $`Sphericity Corrections`
##   Effect     GGe       p[GG] p[GG]<.05      HFe        p[HF] p[HF]<.05
## 2 factor 0.98831 2.31971e-33         * 1.008963 1.006455e-33         *
```
```
## 
##  Friedman rank sum test
## 
## data:  as.matrix(data[, 7:9])
## Friedman chi-squared = 111.73, df = 2, p-value < 2.2e-16
```
```
## 
##  Pairwise comparisons using Wilcoxon signed rank test with continuity correction 
## 
## data:  newdata$response and newdata$factor 
## 
##      AHE     AHLE   
## AHLE 9.8e-15 -      
## AHPE 0.0085  2.4e-14
## 
## P value adjustment method: holm
```
```
## 
##  Pairwise comparisons using paired t tests 
## 
## data:  newdata$response and newdata$factor 
## 
##      AHE    AHLE  
## AHLE <2e-16 -     
## AHPE 0.044  <2e-16
## 
## P value adjustment method: holm
```
```
    #¿La actitud hacia la lengua española tiene una relación directa o inversa con la motivación?
      cor.test(data$AHLE, data$motivacion,method="spearman")
```
```
## Warning in cor.test.default(data$AHLE, data$motivacion, method = "spearman"):
## Cannot compute exact p-value with ties
```
```
## 
##  Spearman's rank correlation rho
## 
## data:  data$AHLE and data$motivacion
## S = 82722, p-value = 2.664e-06
## alternative hypothesis: true rho is not equal to 0
## sample estimates:
##       rho 
## 0.4561181
```
```
    #¿Hay alguna asociación entre el nivel con el que se inscriben los estudiantes y la Utilización que hacen de la lengua en la vida cotidiana?
      tabla<-table(data$Nivel, data$Utilizacion)
      tabla
```
```
##     
##      a_menos20 b_20_40 c_40_60 c_60_80 c_mas80
##   A1         7       7       1       1       0
##   A2         4      10       5       1       0
##   B1         7       8      13       4       8
##   B2         4       2       5       8       1
##   C1         0       0       1       0       0
```
`## Warning in chisq.test(tabla): Chi-squared approximation may be incorrect````
## 
##  Pearson's Chi-squared test
## 
## data:  tabla
## X-squared = 38.112, df = 16, p-value = 0.001459
```
```
##       a_menos20 b_20_40 c_40_60 c_60_80 c_mas80 Total
## A1          7.2     7.2     1.0     1.0     0.0  16.5
## A2          4.1    10.3     5.2     1.0     0.0  20.6
## B1          7.2     8.2    13.4     4.1     8.2  41.2
## B2          4.1     2.1     5.2     8.2     1.0  20.6
## C1          0.0     0.0     1.0     0.0     0.0   1.0
## Total      22.7    27.8    25.8    14.4     9.3 100.0
```
```
##        
##         a_menos20 b_20_40 c_40_60 c_60_80 c_mas80
##   A1         31.8    25.9       4     7.1     0.0
##   A2         18.2    37.0      20     7.1     0.0
##   B1         31.8    29.6      52    28.6    88.9
##   B2         18.2     7.4      20    57.1    11.1
##   C1          0.0     0.0       4     0.0     0.0
##   Total     100.0    99.9     100    99.9   100.0
##   Count      22.0    27.0      25    14.0     9.0
```
```
##     
##      a_menos20 b_20_40 c_40_60 c_60_80 c_mas80 Total Count
##   A1      43.8    43.8     6.2     6.2       0   100    16
##   A2      20.0    50.0    25.0     5.0       0   100    20
##   B1      17.5    20.0    32.5    10.0      20   100    40
##   B2      20.0    10.0    25.0    40.0       5   100    20
##   C1       0.0     0.0   100.0     0.0       0   100     1
```