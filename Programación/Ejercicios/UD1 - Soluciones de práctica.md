---
tags:
  - programacion
  - java
  - ud1
  - ejercicios
  - resuelto
asignatura: Programación
unidad: UD1
tema: Soluciones de práctica
---

# UD1 — Soluciones de práctica

Los 19 ejercicios de práctica de la Unidad 1 resueltos en clase (proyecto `prog-ud1`). Enunciados en [[Programación/Ejercicios/UD1 - Enunciados de práctica|Enunciados de práctica]].

> [!note] Código del alumno
> Los programas se mantienen tal cual se escribieron en clase. Algunos (1, 2, 15, 16, 17, 18) no cierran el `Scanner`; según [[UD1 - Entrada de datos con Scanner#Cerrar el Scanner — `close()`|Anexo V]] conviene añadir `teclado.close()` al final.

## Ejercicio 1 — Nombre y saludo

```java
import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args){
       //declaración variables
        String nombre;
        Scanner teclado = new Scanner(System.in);

       // Entrada de datos
        System.out.println("Introduce tu nombre: ");
        nombre = teclado.nextLine();
        System.out.println("Hola, "+nombre+" ¿que tal el curso?");

    }
}
```

## Ejercicio 2 — Año de nacimiento y edad

```java
import java.util.Scanner;

public class Ejercicio2 {

    static public void main(String[] args){

        //Declaración variables
        int anio;
        Scanner teclado = new Scanner(System.in);
        int anioActual = 2026;

        //Entrada datos
        System.out.println("Introduce tu año de nacimiento");
        anio = teclado.nextInt();
        System.out.println("Tu edad actual es: " +(anioActual-anio));

    }

}
```

## Ejercicio 3 — Operaciones con dos números

```java
import java.util.Scanner;

//Ejercicio 3 Pide dos números y muestra su suma, resta, multiplicación y división.

public class Ejercicio3 {
    public static void main(String[] args){

        //Declaración variables
        double num1;
        double num2;
        Scanner teclado = new Scanner(System.in);
       // Scanner teclado2 = new Scanner(System.in); Comprobacion previa para comprobar si era necesario

        //Entrada de datos
        System.out.println("Introduce el primer número");
        num1 = teclado.nextDouble();
        System.out.println("Introduce el segúndo número");
        num2 = teclado.nextDouble();
        //Salida de datos
        System.out.println("Tus números sumados son: " + (num1+num2));
        System.out.println("Tus números restados son: " + (num1-num2));
        System.out.println("Tus números multiplicados son: " + (num1*num2));
        System.out.println("Tus números divididos son: " + (num1/num2));
        //Cerrar Scanner
        teclado.close();

    }

}
```

## Ejercicio 4 — Precio con IVA

```java
import java.util.Scanner;

// Ejercicio 4
// Lee el precio de un producto y calcula el precio final con un 21% de IVA.

public class Ejercicio4 {

    public static void main(String[] args) {

        // Declaración de variables
        double precio;
        double precioFinal;
        Scanner teclado = new Scanner(System.in);

        // Entrada de datos
        System.out.println("Vamos a calcular el precio final con IVA.");
        System.out.println("Introduce el precio del producto:");
        precio = teclado.nextDouble();

        // Calculos
        precioFinal = precio * 1.21;

        // Salida de datos
        System.out.println("El precio final con IVA es: " + precioFinal);

        //Cerrar Scanner
        teclado.close();

        }
    }
```

## Ejercicio 5 — Área y circunferencia del círculo

```java
import java.util.Scanner;

//Ingresa el radio de un círculo y calcula su área (A=π⋅r2) y circunferencia (C=2⋅π⋅r).

public class Ejercicio5 {
    public static void main(String[] args){

        //Declaración de variables
        double radio;
        double pi = 3.141592;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Introduce el radio");
        radio = teclado.nextDouble();

        //Salida de datos
        System.out.println("Su área es: " + ((radio*radio)*pi));
        System.out.println("Su circunferencia es: " + (2*pi*radio));

        //Cerrar Scanner
        teclado.close();

    }

}
```

## Ejercicio 6 — Euros a dólares

```java
import java.util.Scanner;

// Convierte una cantidad de euros a dólares.
// Pídele al usuario que ingrese la cantidad en euros y el tipo de cambio que se aplica en ese momento.

public class Ejercio6 {

        public static void main(String[] args){
            //Declaración de variables
            double euro;
            double dolarActual = 1.14;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Introduce cantidad en € a convertir");
            euro = teclado.nextDouble();

            //Salida de datos
            System.out.println("La cantidad de euros es: " + euro);
            System.out.println("En dólares a cambio actual 24/09/2026: " + (euro*dolarActual));

            //Cerrar Scanner
            teclado.close();

        }
}
```

> [!note] Archivo `Ejercio6.java`
> El archivo en el curso se llama `Ejercio6.java` (typo en el nombre), pero la clase y el código corresponden al ejercicio 6.

## Ejercicio 7 — Celsius a Fahrenheit

```java
import java.util.Scanner;

// Convierte una temperatura de grados Celsius a Fahrenheit (F=C⋅9/5+32).
public class Ejercicio7 {

        public static void main(String[] args){
            //Declaración de variables
            double celsius;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Introduce los °C para pasar a °F");
            celsius = teclado.nextDouble();

            //Salida de datos
            System.out.println("°C introducidos: " + celsius);
            System.out.println("°C convertidos a °F: " + (celsius*9/5+32));

            //Cerrar Scanner
            teclado.close();

        }
}
```

## Ejercicio 8 — Metros a km, cm y mm

```java
import java.util.Scanner;

// Pide una cantidad de metros y conviértela a kilómetros, centímetros y milímetros.

public class Ejercicio8 {

        public static void main(String[] args){
            //Declaración de variables
            double metros;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Introduce los metros a convertir");
            metros = teclado.nextDouble();

            //Salida de datos
            System.out.println("Metros en kilómetros: " + (metros/1000) + "km");
            System.out.println("Metros en centímetros: " + (metros*100) + "cm");
            System.out.println("Metros en milímetros: " + (metros*1000) + "mm");

            //Cerrar Scanner
            teclado.close();

        }

}
```

## Ejercicio 9 — Segundos a horas y minutos

```java
import java.util.Scanner;

// Convierte una cantidad de segundos a horas, minutos y segundos.

public class Ejercicio9 {

        public static void main(String[] args){
            //Declaracion de variables
            int segundos;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Introduce segundos a convertir");
            segundos = teclado.nextInt();
            System.out.println("Segundos en horas: " + (segundos/3600));
            System.out.println("Segundos en minutos: " + (segundos/60));

            //Cerrar Scanner
            teclado.close();

        }

}
```

> [!tip] Mejorable
> Este ejercicio solo desglosa horas y minutos; el ejercicio 16 es la versión completa con días/horas/minutos/segundos.

## Ejercicio 10 — Millas a kilómetros

```java
import java.util.Scanner;

// Ingresa una distancia en millas y conviértela a kilómetros.

public class Ejercicio10 {

        public static void main(String[] args){
            //Declaración de variables
            double millas;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Introduce las millas a convertir");
            millas = teclado.nextDouble();
            System.out.println("Millas en KM: " + (millas*1.609344));

            //Cerrar Scanner
            teclado.close();

        }
}
```

## Ejercicio 11 — Área del triángulo

```java
import java.util.Scanner;

//Pide la base y la altura de un triángulo y calcula su área (A=½⋅b⋅h)

public class Ejercicio11 {

    public static void main(String[] args){

        //Declaración de variables
        double base;
        double altura;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Para calcular el area de un triangulo se necesita lo siguiente");
        System.out.println("Introduce la base del triangulo: ");
        base = teclado.nextDouble();
        System.out.println("Introduce la altura del triangulo: ");
        altura = teclado.nextDouble();
        System.out.println("Su area es la siguiente: " + (base*altura/2));

        //Cerrar Scanner
        teclado.close();

    }

}
```

## Ejercicio 12 — Promedio de calificaciones

```java
import java.util.Scanner;

//Lee tres calificaciones de un estudiante y calcula su promedio final.

public class Ejercicio12 {

    public static void main(String[] args){

        //Declaracion de variables
        double cal1;
        double cal2;
        double cal3;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Para calcular la media necesito 3 notas");
        System.out.println("Introduce la primera calificación:");
        cal1 = teclado.nextDouble();
        System.out.println("Introduce la segunda calificacion: ");
        cal2 = teclado.nextDouble();
        System.out.println("Introduce la tercera calificación: ");
        cal3 = teclado.nextDouble();
        System.out.println("Tu promedio final es el siguiente: " + ((cal1+cal2+cal3)/3));

        //Cerrar Scanner
        teclado.close();

    }

}
```

## Ejercicio 13 — Área del trapecio

```java
import java.util.Scanner;

// Calcula el área de un trapecio conociendo
// la base mayor, la base menor y la altura (A=½⋅(b1+b2)⋅h)

public class Ejercicio13 {

        public static void main(String[] args){

            //Declaración de variables
            double mayor;
            double menor;
            double altura;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Vamos a calcular el area de un trapecio");
            System.out.println("Introduce la base mayor:");
            mayor = teclado.nextDouble();
            System.out.println("Introduce la base menor:");
            menor = teclado.nextDouble();
            System.out.println("Introduce la altura:");
            altura = teclado.nextDouble();
            System.out.println("El area de tu trapecio es la siguiente: " + ((mayor+menor)*altura/2));

            //Cerrar Scanner
            teclado.close();

        }
}
```

## Ejercicio 14 — Perímetro del triángulo

```java
import java.util.Scanner;

//Pide la longitud de los tres lados de un triángulo y calcula su perímetro.

public class Ejercicio14 {

        public static void main(String[] args){

            //Declaración de variables
            double lado1;
            double lado2;
            double lado3;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Vamos a calcular el perimetro conociendo los lados");
            System.out.println("Introduce la primera longitud:");
            lado1 = teclado.nextDouble();
            System.out.println("Introduce la segunda longitud:");
            lado2 = teclado.nextDouble();
            System.out.println("Introduce la tercera longitud:");
            lado3 = teclado.nextDouble();
            System.out.println("El perimetro de tu triangulo es el siguiente: " + (lado1+lado2+lado3));

            //Cerrar Scanner
            teclado.close();

        }

}
```

## Ejercicio 15 — Suma de los dígitos

```java
import java.util.Scanner;

//Lee un número de dos cifras y muestra la suma de sus dígitos.

public class Ejercicio15 {

        public static void main(String[] args){

            //Declaración de variables
            int numero;
            int decenas;
            int unidades;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Vamos a calcular la suma de los digitos de un numero de dos cifras");
            System.out.println("Introduce un numero de dos cifras:");
            numero = teclado.nextInt();

            //Calculo

            decenas = numero / 10;
            unidades = numero % 10;

            System.out.println("La suma de sus digitos es: " + (decenas + unidades));
        }
}
```

> [!tip] División entera y módulo
> `numero / 10` da las **decenas** (división entera) y `numero % 10` da las **unidades** (resto). Ver `%` en los operadores.

## Ejercicio 16 — Segundos desglosados

```java
import java.util.Scanner;

// Pide un valor en segundos y calcula cuántos días completos, horas, minutos y segundos son.
// Ejemplo: 90010 segundos son 1 día, 1 hora, 0 minutos y 10 segundos.

public class Ejercicio16 {

    public static void main(String[] args){

        //Declaracion de variables
        int segIntro;
        int seg;
        int min;
        int horas;
        int dias;
        Scanner teclado = new Scanner(System.in);

        //Entrada de datos
        System.out.println("Vamos a calcular dias completos, horas, minutos y segundos");
        System.out.println("Introduce los segundos:");
        segIntro = teclado.nextInt();

        //Calculos
        dias = segIntro / 86400;
        horas = (segIntro % 86400) / 3600;
        min = (segIntro % 3600) / 60;
        seg = segIntro % 60;

        //Salida de datos
        System.out.println("Tus dias completos, horas, minutos y segundos son los siguientes: " + dias + " dias " + horas + " horas " + min + " minutos " + seg + " segundos.");

    }

}
```

## Ejercicio 17 — Descuento

```java
import java.util.Scanner;

// Solicita el total de una compra y un porcentaje de descuento, y calcula el precio final.

public class Ejercicio17 {

        public static void main(String[] args){

            //Declaracion de variables
            double precio;
            double descuento;
            double precioDescontado;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Vamos a calcular tu descuento");
            System.out.println("Introduce precio de compra: ");
            precio = teclado.nextDouble();
            System.out.println("Introduce el descuento hecho: ");
            descuento = teclado.nextDouble();

            //Calculos
            descuento = descuento/100;
            precioDescontado = precio -(precio*descuento);

            //Salida de datoss
            System.out.println("Tu precio descontado es: " + precioDescontado);

        }
}
```

## Ejercicio 18 — Total con impuestos

```java
import java.util.Scanner;

// Lee el precio de un producto,
// la cantidad comprada y el porcentaje de impuestos que es necesario aplicar, y calcula el total a pagar.

public class Ejercicio18 {

        public static void main(String[] args){

            //Declaración de variables
            double precio;
            double cantidad;
            double impuestos;
            double totalProducto;
            double totalconImpuesto;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Vamos a calcular el valor total de la compra");
            System.out.println("Introduce el precio de compra:");
            precio = teclado.nextDouble();
            System.out.println("Introduce la cantidad de articulos:");
            cantidad = teclado.nextDouble();
            System.out.println("Introduce el porcentaje de impuestos:");
            impuestos = teclado.nextDouble();

            //Calculos
            totalProducto = precio*cantidad;
            totalconImpuesto = totalProducto + (impuestos/100*totalProducto);

            //Salida de datos
            System.out.println("Tu total con impuestos es el siguiente: " + totalconImpuesto);

        }
}
```

## Ejercicio 19 — Nota final ponderada

```java
import java.util.Scanner;

//Pide tres notas de exámenes y tres porcentajes de ponderación para cada nota. Calcula la nota final ponderada.

public class Ejercicio19 {

        public static void main(String[] args){

            //Declaración de variables
            double nota1;
            double nota2;
            double nota3;
            double porc1;
            double porc2;
            double porc3;
            double notaFinal;
            Scanner teclado = new Scanner(System.in);

            //Entrada de datos
            System.out.println("Vamos a calcular la media ponderada de notas.");
            System.out.println("Introduce la nota 1 de examen:");
            nota1 = teclado.nextDouble();
            System.out.println("Introduce el porcentaje de examen 1:");
            porc1 = teclado.nextDouble();
            System.out.println("Introduce la nota 2 de examen:");
            nota2 = teclado.nextDouble();
            System.out.println("Introduce el porcentaje de examen 2:");
            porc2 = teclado.nextDouble();
            System.out.println("Introduce la nota 3 de examen:");
            nota3 = teclado.nextDouble();
            System.out.println("Introduce el porcentaje de examen 3:");
            porc3 = teclado.nextDouble();

            //Calulos
            notaFinal = (((nota1*porc1)+(nota2*porc2)+(nota3*porc3))/(porc1+porc2+porc3));

            //Salida de datos
            System.out.println("Tu nota final ponderada es la siguiente: " + notaFinal);

            //Cerrar Scanner
            teclado.close();

        }
}
```

## Ver también

- [[Programación/Ejercicios/UD1 - Enunciados de práctica|Enunciados de práctica]] — el checklist de estos ejercicios
- [[Programación/Ejercicios/UD1 - Ejemplos java|Ejemplos de programas]] — los ejemplos vistos en clase
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — lectura de datos con `nextInt()`, `nextDouble()` y `nextLine()`

---

← Volver a [[_Índice Programación]]