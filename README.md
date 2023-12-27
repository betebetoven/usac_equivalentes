
# Manual de Uso: Calculadora de Equivalentes
Ingresa al sitio aquí [Calculadora de Equivalentes](https://f2equivalentes.fly.dev/)


Este documento sirve como guía para utilizar la Calculadora de Equivalentes, una herramienta diseñada para facilitar el cálculo de equivalentes en circuitos, ya sean de resistencias o capacidades.

## Contenido

- [Configuración Inicial](#configuración-inicial)
- [Asignación de Variables](#asignación-de-variables)
- [Cálculo de Equivalencias](#cálculo-de-equivalencias)
  - [Paralelo](#paralelo)
  - [Serie](#serie)
  - [Anidación de Operaciones](#anidación-de-operaciones)
- [Ejemplo](#ejemplo)

## Configuración Inicial

La aplicación opera bajo dos contextos:

- `contexto = C`: Para trabajar con **capacitancias**.
- `contexto = R`: Para trabajar con **resistencias**.

Es importante notar que la aplicación es *case sensitive*. Esto significa que se debe respetar el uso de mayúsculas y minúsculas tal como se muestra en los ejemplos.

## Asignación de Variables

Para asignar una variable, se utiliza la siguiente sintaxis:

```
variable_id = valor;
```

Esta estructura añade una variable a la memoria del programa. Se pueden definir tantas variables como se necesiten. Por ejemplo:

```
C1 = 10;
R1 = 5.5;
```

## Cálculo de Equivalencias

### Paralelo

Para calcular el equivalente en paralelo entre dos valores, se utiliza la instrucción `par`. La sintaxis es la siguiente:

```
par(valor1, valor2);
```

Los valores pueden ser números, variables definidas previamente o incluso otras operaciones.

### Serie

De manera similar, para calcular el equivalente en serie se utiliza `ser`:

```
ser(valor1, valor2);
```

Al igual que con `par`, los valores pueden ser numéricos, variables o combinaciones de operaciones.

### Anidación de Operaciones

La herramienta permite anidar operaciones de `ser` y `par` para representar configuraciones más complejas de circuitos. Por ejemplo:

```
ser(par(a, b), c);
```

Este comando significa que primero se calcula el paralelo entre `a` y `b`, y al resultado se le calcula la serie con `c`. Es importante siempre utilizar solo dos parámetros dentro de los paréntesis y separarlos con una coma.

## Ejemplo

Para ver un ejemplo de cómo utilizar la herramienta, simplemente presione el botón **Ver Ejemplo** en la aplicación. Este botón cargará un caso de uso típico en el editor para su revisión y experimentación.
![Ejemplo de Uso](https://github.com/betebetoven/usac_equivalentes/blob/main/example/pic1.png)
```
contexto = C;
C1 = 10;
C2 = 20;
C3 = 30;
C4 = 40;
C5 = 50;
ser(ser(par(par(C1,C2),C3),C4),C5);
```
o bien 
```
contexto = C;
C1 = 10;
C2 = 20;
C3 = 30;
C4 = 40;
C5 = 50;
paraleloC12 = par(C1,C2);
paraleloC123 = par(paraleloC12,C3);
serieC45 = ser(C4,C5);
ser(paraleloC123,serieC45);

```
[Calculadora de Equivalentes](https://f2equivalentes.fly.dev/)