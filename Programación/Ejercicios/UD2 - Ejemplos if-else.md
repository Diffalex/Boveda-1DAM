---
tags:
  - programacion
  - java
  - ud2
  - ejercicios
  - condicionales
asignatura: Programación
unidad: UD2
tema: Ejemplos if-else
---

# UD2 — Ejemplos if/else

Programas vistos en clase con la [[UD2 - Estructura condicional (if-else)|estructura condicional]] (proyecto `prog-ud2`).

## ParImpar — par o impar

```java
import java.util.Scanner;

//Pide un numero y dime si es par o impar

public class ParImpar {

    public static void main(String[] args){

        //Declaración de variables
        int num1;
        int resto;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Introduce un numero");
        num1 = teclado.nextInt();

        //Calculo
        resto = num1%2;

        //Salida de datos
        if (resto==1)
            System.out.println("El numero es Impar");
        else
            System.out.println("El numero es par");

        //Cierre Scanner
        teclado.close();

    }

}
```

> [!note]
> Es una "trampa" del ejercicio: si el resto es `1` el número es impar, pero si el resto `2%2 = 0` es par. Los números negativos dan resto también `0` o `1`, así que convendría comprobar `resto == 0`.

## MayorEdad — mayor o menor de edad

```java
import java.util.Scanner;

public class MayorEdad {

    public static void main(String[] args){

        //Decalaracion de variables
        int edad;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Introduce tu edad:");
        edad = teclado.nextInt();

        //Salida de datos
        if (edad >= 18)
            System.out.println("Eres mayor de edad");
        else
            System.out.println("Menor de edad");

        teclado.close();

    }

}
```

## EjercicioClase — nota a calificación

```java
/*Si la nota es menor de 5, la calificación será "INSUFICIENTE".
Si la nota es mayor o igual a 5 y menor que 6, la calificación será "SUFICIENTE".
Si la nota es mayor o igual a 6 y menor que 7, la calificación será "BIEN".
Si la nota es mayor o igual a 7 y menor que 9, entonces la calificación será "NOTABLE".
Si la nota es mayor o igual a 9 y menor o igual a 10, entonces la calificación será de "SOBRESALIENTE".*/

import java.util.Scanner;

public class EjercicioClase {

    public static void main(String[] args){
        //Declaracion de variables
        int nota;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Introduce la nota");
        nota = teclado.nextInt();

        //Salida de datos
        if (nota<5)
            System.out.println("INSUFICIENTE");
        else
            if (nota>=5 && nota<6)
                System.out.println("Suficiente");
            else
                if (nota>=6 && nota<7)
                    System.out.println("BIEN");
                else
                    if (nota>=7 && nota<9)
                        System.out.println("Notable");
                    else
                        if(nota>=9 && nota<=10)
                            System.out.println("SOBRESALIENTE");

    teclado.close();
    }

}
```

> [!tip]
> Este `else→if` anidado es equivalente a una cadena `else if` (más legible). Los límites exactos (`nota<6` frente a `nota>=5 && nota<6`) son equivalentes porque se evalúan en cascada.

## EjercicioClase2 — día laborable o festivo

```java
//Programa que lea por teclado un numero del 1 al 7, si el numero es el 1, 2, 3, 4 o 5
// que imprima laborable, si es 6 o 7 escriba festivo
import java.util.Scanner;

public class EjercicioClase2 {

    public static void main(String[] args){

        //Declaracion variables
        int dia;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Introduce un numero del 1 al 7");
        dia = teclado.nextInt();

        if ( dia == 1 )
            System.out.println("Lunes Laboral");
        else if ( dia == 2  )
            System.out.println("Martes Laboral");
        else if (  dia == 3  )
            System.out.println("Miercoles Laboral");
        else if ( dia == 4 )
            System.out.println("jueves Laboral");
        else if ( dia == 5 )
            System.out.println("Viernes Laboral");
        else if (dia == 6 )
            System.out.println("Sabado Festivo");
        else if (dia == 7 )
            System.out.println("Domingo dia del señor");
        else if (dia >=8 && dia<=0)
            System.out.println("No hay mas dias");
    teclado.close();
    }
}
```

> [!note] Error en el último `else if`
> La condición `dia >= 8 && dia <= 0` es **imposible** (un número no puede ser mayor o igual a 8 y a la vez menor o igual a 0), así que ese mensaje nunca se muestra. Debería ser `else` a secas, o `else if (dia < 1 || dia > 7)`.

## EjercicioClase3 — positivo o negativo

```java
//Programa que reciba por teclado un número e indique si es positivo.

import java.util.Scanner;

public class EjercicioClase3 {

    public static void main(String[] args){

        //Variables
        double num1;
        Scanner teclado = new Scanner(System.in);

        //entrada de datos
        System.out.println("Introduce un numero");
        num1 = teclado.nextDouble();

        if (num1 >=0)
            System.out.println("Tu numero es positivo");
        else
            System.out.println("Tu numero es negativo");

        teclado.close();
    }
}
```

> [!note]
> El `0` se considera positivo aquí (`num1 >= 0`). Matemáticamente el `0` no es ni positivo ni negativo.

## EjercicioClase5 — mayor de dos números

```java
//Programa que pide dos números por teclado e indica que valor es el mayor de los dos.

import java.util.Scanner;

public class EjercicioClase5 {

        public static void main(){
            //variables
            double num1, num2;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Introduce el primer numero");
            num1 = teclado.nextDouble();
            System.out.println("Introduce el segundo numero");
            num2 = teclado.nextDouble();

            if (num1>num2)
                System.out.println("numero 1 es mayor");
            else
                System.out.println("numero 2 es mayor");

        teclado.close();

        }

}
```

> [!warning] Falta `String[] args`
> El método principal debe ser `public static void main(String[] args)`. Como está escrito, `main()` sin parámetros **compila pero no arranca** (la JVM busca `main(String[])`). Los números iguales darían "numero 2 es mayor".

## BloqueSentencias — bloques y ámbito

```java
public class BloqueSentencias {

    public static void main(String[] args) {

            int num1 = 10;
            double num2 = 1.3;

        System.out.println(num1);
    }
}
```

## EjercicioClase8 — descuento (incompleto)

```java
//Programa que recibe por teclado el valor de un artículo. Si el valor es superior a 100€ se le aplicará un descuento del 10%.
// Se debe mostrar el valor que ha de pagar y controlar los posibles errores que se produzcan.

import java.util.Scanner;

public class EjercicioClase8 {

    public static void main(){

        //Entrada de datos
        double precio;
        int descuento = 10;
        Scanner teclado = new Scanner(System.in);

        
    }
}
```

> [!warning] Pendiente
> `EjercicioClase8` está **sin terminar**: declara las variables pero no lee el precio, no aplica el descuento ni controla errores. Además igual que `EjercicioClase5`, le falta `String[] args` en `main`. Falta por resolver.

## Ver también

- [[UD2 - Estructura condicional (if-else)|Estructura condicional]] — teoría de `if/else if/else`
- [[UD1 - Tipos de datos primitivos|Tipos primitivos]] — `int` y `double` en las condiciones
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — lectura de datos

---

← Volver a [[_Índice Programación]]