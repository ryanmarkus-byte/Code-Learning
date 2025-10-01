let num1 = 7;
let num2 = 10;

console.log("Foram declarados dois números: 7 e 10. Segue as operacoes artimeticas com estes números:\n");
console.log("Adicao(+):", num1 + num2);
console.log("Subtracao(-):", num1 - num2);
console.log("Multiplicacao(*):", num1 * num2);
console.log("Divisao(/):", num1 / num2);
console.log("Modulo(%):", num1 % num2);
console.log("Exponenciacao(**):", num1 ** num2, "\n");

//

const nome = "Ryan";
const nom_sobrenome = "Ryan Markus";

console.log("Temos nome e nome juntamente com sobrenome, vamos seguir com comparacoes entre essas duas variaveis\n");
console.log("Igualdade(==):", nome == nom_sobrenome);
console.log("Igualdade restrita(===):", nome === nom_sobrenome);
console.log("Diferenca(!=):", nome != nom_sobrenome);
console.log("Diferenca restrita(!==):", nome !== nom_sobrenome);
console.log("Maior que(>):", nome > nom_sobrenome);
console.log("Menor que(<):", nome < nom_sobrenome);
console.log("Maior ou igual a(>=):", nome >= nom_sobrenome);
console.log("Menor ou igual a(<=):", nome <= nom_sobrenome, "\n");

//

let ligado = true;
let desligado = false;

console.log("Vamos fazer operacoes logicas com as variaveis booleanas: ligado e desligado");
console.log("AND(&&)", ligado && desligado);
console.log("OR(||)", ligado || desligado);
console.log("NOT(!)", !ligado);