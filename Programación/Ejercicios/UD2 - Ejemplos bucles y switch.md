---
tags:
  - programacion
  - java
  - ud2
  - ejercicios
  - bucles
  - switch
asignatura: Programación
unidad: UD2
tema: Ejemplos bucles y switch
---

# UD2 — Ejemplos bucles y switch

Programas vistos en clase con [[UD2 - Bucles (while, do-while, for)|bucles]] y [[UD2 - Selección múltiple (switch)|`switch`]] (proyecto `prog-ud2`).

## EjercicioWhile — secuencia de números con `while`

```java
import java.util.Scanner;
//Escribe un programa que solicite dos números por teclado (inicio y fin, donde inicio debería ser menor o igual que fin)
// y muestre por pantalla todos los números que van desde inicio hasta fin, todos en una misma línea.

public class EjercicioWhile {

    public static void main(String[] args){
        //Decalaracion de variables

        int num1, num2;
        Scanner teclado = new Scanner(System.in);

        //entrada de datos
        System.out.println("Introduce el primer numero:");
        num1 = teclado.nextInt();
        System.out.println("Introduce el segundo numero: ");
        num2 = teclado.nextInt();

        System.out.println("tu secuencia de numeros es");

        if (num1 < num2) {
            while (num1 <= num2) {
                System.out.print(num1 + " ");
                num1++;
            }
        } else {
            while (num1 >= num2) {
                System.out.print(num1 + " ");
                num1--;
            }
        }

        teclado.close();

    }
}
```

> [!tip]
> Con `if/else` se decide si la secuencia **sube** (`num1++`) o **baja** (`num1--`). El enunciado asume `inicio <= fin`, así que el caso descendente (`inicio > fin`) es una solución de más que no rompe el programa.

## EjercicioResueltoFor — tabla del 7 con `for`

```java
//Al igual que se pedía en apartados anteriores, ahora vamos os vamos a pedir que
// realicéis el ejercicio de la tabla de multiplicar del número 7,
// pero usando un bucle una estructura repetitiva tipo for.

public class EjercicioResueltoFor {
    public static void main(String[] args) {

        int contador;
        int resultado = 0;
        int numero = 7;

        //Salida de datos

        System.out.println("Se va a mostrar la tabla del 7");

        for (contador = 1; contador <= 10; contador++) {
            resultado = contador * numero;
            System.out.println(numero + " x " + contador + " = " + resultado);
        }
    }
}
```

## Multiplicaciones — tabla de multiplicar del número pedido

```java
import java.util.Scanner;
//pide un numero y saca la multiplicacion de ese numero que se le pida al usuario

public class Multiplicaciones {

    public static void main(String[] args) {

        int contador;
        int resultado = 0;
        int numero;

        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Introduce un numero para sacar la multiplicacion");
        numero = teclado.nextInt();

        //Salida de datos
        if (numero<=10){
            System.out.println("Se va a mostrar la tabla del numero indicado");

            for (contador = 1; contador <= 10; contador++) {
                resultado = contador * numero;
                System.out.println(numero + " x " + contador + " = " + resultado);
            }
        }
        else {
            System.out.println("Numero fuera de las tablas del 1 al 10");
        }
    }
}
```

> [!note]
> Validación `if (numero <= 10)`: solo muestra la tabla si el número está entre las tablas del 1 al 10. No acota el mínimo (un negativo cumpliría la condición aunque no exista su "tabla").

## Asteriscos — 3 líneas de 4 asteriscos con `for` anidado

```java
//programa que dibuje por pantalla una linea de 4
//asteriscos seguidos

public class Asteriscos {

    public static void main(String[] args) {

        String asterisco = "*";
        int contador = 1;
        for (int contador1= 1; contador1<=3; contador1++) {
            for (contador = 1; contador <= 4; contador++) {
                System.out.print(" " + asterisco);
        }
        System.out.println();
    }
//
//    while (contador<=4){
//        System.out.print(" "+ asterisco);
//        contador++;
//    }
//
//    do{
//        System.out.print(" "+ asterisco);
//        contador++;
//    }while(contador<=4);

    }
}
```

> [!warning] Dos variables `contador`
> `contador` se declara como **variable local** (`int contador = 1;`) y además el `for` externo usa `contador1`. El `for` interno modifica la variable externa `contador`, mientras que el externo itera con `contador1`. Mejor usar variables distintas en cada `for`. Las variantes `while` y `do-while` quedaron **comentadas**.

## EjercicioBucles1 — entrada "modo cabezón" (incompleto)

```java
import java.util.Scanner;

//Programa que solicite por teclado un número par y lo siga solicitando hasta que realmente el número introducido sea par.
// Si introducimos un número par a la primera, no se nos pedirá más.
// Pero si introducimos un impar, nos estará pidiendo otra vez el número hasta que metamos finalmente un par.
// Es lo que llamábamos entrada de datos en "modo cabezón". Por muy "cabezón" que sea el usuario, nuestro programa lo será más.

public class EjercicioBucles1 {

    public static void main(String[] args) {

        //Declaracion de variables
        int num1;
        Scanner teclado = new Scanner(System.in);

        //Entrada de dato
        System.out.println("Introduce un numero par:");
        num1 = teclado.nextInt();

    }
}
```

> [!warning] Pendiente
> Está **sin terminar**: solo lee el número una vez, sin ningún bucle. Falta repetir la petición mientras `num1` sea impar, por ejemplo con `do-while`:
>
> ```java
> do {
>     System.out.println("Introduce un numero par:");
>     num1 = teclado.nextInt();
> } while (num1 % 2 != 0);
> ```

## EstacionMes — `switch` anidado

```java
import java.util.Scanner;

public class EstacionMes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Estación (1-4): ");
        int estacion = sc.nextInt();
        System.out.print("Mes de la estación (1-3): ");
        int mesEstacion = sc.nextInt();

        if (estacion < 1 || estacion > 4 || mesEstacion < 1 || mesEstacion > 3) {
            System.out.println("Valor inválido.");
        } else {
            String nombreEstacion = "";
            String nombreMes = "";

            switch (estacion) {
                case 1:
                    nombreEstacion = "Invierno";
                    switch (mesEstacion) {
                        case 1: nombreMes = "Diciembre"; break;
                        case 2: nombreMes = "Enero"; break;
                        case 3: nombreMes = "Febrero"; break;
                    }
                    break;
                case 2:
                    nombreEstacion = "Primavera";
                    switch (mesEstacion) {
                        case 1: nombreMes = "Marzo"; break;
                        case 2: nombreMes = "Abril"; break;
                        case 3: nombreMes = "Mayo"; break;
                    }
                    break;
                case 3:
                    nombreEstacion = "Verano";
                    switch (mesEstacion) {
                        case 1: nombreMes = "Junio"; break;
                        case 2: nombreMes = "Julio"; break;
                        case 3: nombreMes = "Agosto"; break;
                    }
                    break;
                case 4:
                    nombreEstacion = "Otoño";
                    switch (mesEstacion) {
                        case 1: nombreMes = "Septiembre"; break;
                        case 2: nombreMes = "Octubre"; break;
                        case 3: nombreMes = "Noviembre"; break;
                    }
                    break;
            }

            System.out.println("Estación: " + nombreEstacion + " → Mes: " + nombreMes);
        }

        sc.close();
    }
}
```

> [!tip]
> Validar el rango con `if` antes del `switch` evita que un valor inválido deje `nombreEstacion`/`nombreMes` vacíos. Los `break` de cada `case` son obligatorios para que no continúe al siguiente `case` (fallthrough).

## Ver también

- [[UD2 - Bucles (while, do-while, for)|Bucles]] — teoría de `while`, `do-while` y `for`
- [[UD2 - Selección múltiple (switch)|Selección múltiple]] — teoría del `switch`
- [[UD2 - Estructura condicional (if-else)|Condicionales]] — estructuras de control vistas antes
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — lectura de datos

---

← Volver a [[_Índice Programación]]