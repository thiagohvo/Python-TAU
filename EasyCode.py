# Função que verifica se um número é par ou ímpar
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Função que retorna o fatorial de um número usando um laço for
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Classe para demonstrar conceitos de POO: herança, métodos e polimorfismo
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f"{self.nome} faz um som"

# Uma classe que herda de Animal e sobrescreve o método falar
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} late"

# Função para demonstrar polimorfismo com sobrescrita de método
def som_do_animal(animal):
    print(animal.falar())

# Demonstrando o uso de condicionais e laços
if __name__ == "__main__":
    # Verificando se é par ou ímpar
    num = 10
    print(f"{num} é {verificar_par_impar(num)}")

    # Calculando o fatorial
    num_fatorial = 5
    print(f"O fatorial de {num_fatorial} é {fatorial(num_fatorial)}")

    # Demonstrando polimorfismo
    cachorro = Cachorro("Buddy")
    som_do_animal(cachorro)

    # Demonstrando o laço com break e continue
    for i in range(1, 6):
        if i == 3:
            continue  # Pula o número 3
        if i == 5:
            break  # Para o laço quando i for igual a 5
        print(i)
