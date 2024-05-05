import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Declaración de variables:
        int añoLanzamiento = 1999;
        double calificacion = 4.5;
        boolean incluidoPlanBasico = true;
        String tituloPelicula = "Matrix";

        double promedioCalificacionUsuario = 0;

        System.out.println("Película: " + tituloPelicula);
        System.out.println("Año: " + añoLanzamiento);
        System.out.println("Calificación: " + calificacion + "/5");
        System.out.println("Incluido en el plan básico: " + incluidoPlanBasico);

        double promedioCalificacion = (4.5 + 4.8 + 3) / 3;
        System.out.println("Promedio de la calificación de " + tituloPelicula + " es: " + promedioCalificacion);

        if (añoLanzamiento >= 2023){
            System.out.println("Novedad popular");
        } else {
            System.out.println("Clásica popular");
        }

        for (int indice = 0; indice < 3; indice++) {
            Scanner teclado = new Scanner(System.in);
            System.out.println("Ingresa tu calificación para de la película: ");
            try {
            double calificacionUsuario = teclado.nextDouble();
            promedioCalificacionUsuario += calificacionUsuario;
            } catch (InputMismatchException e) {
            System.out.println("Entrada inválida. Ingresa una calificación válida (número decimal): ");
            teclado.next(); // Consume la entrada no válida
            indice--; // Decrementar el índice para que el usuario vuelva a ingresar la calificación
            }
        }
        System.out.println("El promedio de la calificación de los usuarios para " + tituloPelicula + " es: " + promedioCalificacionUsuario / 3);

    }
}