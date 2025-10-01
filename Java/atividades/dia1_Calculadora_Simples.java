import java.util.InputMismatchException;
import java.util.Scanner;

public class dia1_Calculadora_Simples {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double num1, num2, resultado;
        char operador;

        System.out.print("\n---- Bem vindo a Calculadora Básica em Java! ----");

        try {
            System.out.print("\n-    Digite o primeiro numero da operação: ");
            num1 = input.nextDouble();
        } catch (InputMismatchException e) {
            System.out.println("ERRO: O primeiro valor digitado não é um numero válido.");
            input.close();
            return;
        }

        try {
            System.out.print("-    Digite o operador(+,-,*,/): ");
            operador = input.next().charAt(0);
        } catch (InputMismatchException e) {
            System.out.println("ERRO: O primeiro valor digitado não é um numero válido.");
            input.close();
            return;
        }

        try {
            System.out.print("-    Digite o segundo numero da operacao: ");
            num2 = input.nextDouble();
        } catch (InputMismatchException e) {
            System.out.println("ERRO: O primeiro valor digitado não é um numero válido.");
            input.close();
            return;
        }

        switch (operador) {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                if (num2 == 0) {
                    System.out.println("Erro: Divisão por zero.");
                    return;
                } else {
                    resultado = num1 / num2;
                }
                break;
            default:
                System.out.println("Erro: Operador inválido.");
                return;
        }
        System.out.println("\n-    Resultado: "+ num1 + " " +operador + " " + num2 + " " + " = " + resultado);

        input.close();
    }
}