
# User Manual: Equivalence Calculator(Manual en español más abajo)
Access the site here [Equivalence Calculator](https://f2equivalentes.fly.dev/)

This is a Simple language made to calculate the Equivalence af capacitance or resistance in a circuit, it was done this way because when analyzing a the parallel or series of a circuit, you can see that it is
indeed just presedences and nesting, that makes it easy for us to develop a simple grammar to rerpresent this nestings in a more natural, simple and easier way, the goal of all of this is to sasve time, and reduce typical human error, and to forget about those large calculation inside a tiny calculator. 
The grammar can be found in the parsero.py file, It could have been different, building the whole AST object and then running it, but i think for this case let's just make it simple, for further collaborations, it might be more viable building the AST object and then running it.
This document serves as a guide to using the Equivalence Calculator, a tool designed to facilitate the calculation of equivalents in circuits, whether for resistances or capacitances.

## Contents

- [Initial Setup](#initial-setup)
- [Variable Assignment](#variable-assignment)
- [Equivalence Calculation](#equivalence-calculation)
  - [Parallel](#parallel)
  - [Series](#series)
  - [Nesting Operations](#nesting-operations)
- [Example](#example)

## Initial Setup

The application operates under two contexts:

- `contexto = C`: To work with **capacitances**.
- `contexto = R`: To work with **resistances**.

It's important to note that the application is *case sensitive*. This means that the use of uppercase and lowercase must be respected as shown in the examples.

## Variable Assignment

To assign a variable, the following syntax is used:

```
variable_id = value;
```

This structure adds a variable to the program's memory. As many variables as needed can be defined. For example:

```
C1 = 10;
R1 = 5.5;
```

## Equivalence Calculation

### Parallel

To calculate the equivalent in parallel between two values, the `par` instruction is used. The syntax is as follows:

```
par(value1, value2);
```

Values can be numbers, previously defined variables, or even other operations.

### Series

Similarly, to calculate the equivalent in series, `ser` is used:

```
ser(value1, value2);
```

Like with `par`, the values can be numeric, variables, or combinations of operations.

### Nesting Operations

The tool allows for nesting `ser` and `par` operations to represent more complex circuit configurations. For example:

```
ser(par(a, b), c);
```

This command means that the parallel between `a` and `b` is first calculated, and then the series with `c` is calculated. It's important to always use only two parameters within the parentheses and separate them with a comma.

## Example

To see an example of how to use the tool, simply press the **See Example** button in the application. This button will load a typical use case in the editor for your review and experimentation.
![Example of Use](https://github.com/betebetoven/usac_equivalentes/blob/main/example/pic1.png)
```
contexto = C;
C1 = 10;
C2 = 20;
C3 = 30;
C4 = 40;
C5 = 50;
ser(ser(par(par(C1,C2),C3),C4),C5);
```
or
```
contexto = C;
C1 = 10;
C2 = 20;
C3 = 30;
C4 = 40;
C5 = 50;
parallelC12 = par(C1,C2);
parallelC123 = par(parallelC12,C3);
seriesC1234 = ser(parallelC123,C4);
ser(seriesC1234, C5);

```
[Equivalence Calculator](https://f2equivalentes.fly.dev/)





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
serieC1234 = ser(paraleloC123,C4);
ser(serieC1234, C5);

```
[Calculadora de Equivalentes](https://f2equivalentes.fly.dev/)
