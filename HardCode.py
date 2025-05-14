# ------------------------------------------------------------
# PARTE 1: VARIÁVEIS E TIPOS DE DADOS
# ------------------------------------------------------------
print("\n=== VARIÁVEIS E TIPOS DE DADOS ===")

# Tipos de dados básicos
nome = "Maria"  # string
idade = 25      # inteiro
altura = 1.65   # float
estudante = True  # booleano

print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"Estudante: {estudante} (tipo: {type(estudante)})")

# Coleções
lista = [1, 2, 3, 4, 5]  # lista (mutável)
tupla = (1, 2, 3, 4, 5)  # tupla (imutável)
dicionario = {"nome": "João", "idade": 30}  # dicionário
conjunto = {1, 2, 3, 4, 5}  # conjunto (sem duplicatas)

print("\nTipos de Coleções:")
print(f"Lista: {lista} (tipo: {type(lista)})")
print(f"Tupla: {tupla} (tipo: {type(tupla)})")
print(f"Dicionário: {dicionario} (tipo: {type(dicionario)})")
print(f"Conjunto: {conjunto} (tipo: {type(conjunto)})")

# Operações com coleções
lista.append(6)
print("\nOperações com coleções:")
print(f"Lista após append: {lista}")
print(f"Elemento da tupla: {tupla[1]}")
print(f"Valor do dicionário: {dicionario['nome']}")
conjunto.add(6)
print(f"Conjunto após add: {conjunto}")

# ------------------------------------------------------------
# PARTE 2: CONDICIONAIS
# ------------------------------------------------------------
print("\n=== CONDICIONAIS ===")

# Estruturas if, elif e else
numero = 15

if numero > 20:
    print("O número é maior que 20")
elif numero > 10:
    print("O número está entre 11 e 20")
else:
    print("O número é menor ou igual a 10")

# Operadores de comparação e lógicos
a, b = 10, 5

print("\nOperadores de comparação:")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

print("\nOperadores lógicos:")
print(f"(a > 5) and (b < 10): {(a > 5) and (b < 10)}")
print(f"(a > 15) or (b < 10): {(a > 15) or (b < 10)}")
print(f"not (a > b): {not (a > b)}")

# ------------------------------------------------------------
# PARTE 3: LOOPS
# ------------------------------------------------------------
print("\n=== LOOPS ===")

# Loop for
print("\nLaço for com lista:")
for item in [1, 2, 3, 4, 5]:
    print(f"Item: {item}")

# Loop for com range
print("\nLaço for com range:")
for i in range(3):
    print(f"Índice: {i}")

# Loop while
print("\nLaço while:")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# Break e continue
print("\nLaço com break e continue:")
for i in range(1, 6):
    if i == 2:
        print("Pulando 2 (continue)")
        continue
    if i == 4:
        print("Interrompendo no 4 (break)")
        break
    print(f"Número: {i}")

# ------------------------------------------------------------
# PARTE 4: FUNÇÕES
# ------------------------------------------------------------
print("\n=== FUNÇÕES ===")

# Definição básica de função
def saudacao(nome):
    """Função simples que retorna uma saudação personalizada."""
    return f"Olá, {nome}!"

print(saudacao("Ana"))

# Argumentos posicionais e nomeados
def calcular_preco(valor, desconto=0, imposto=0):
    """Calcula o preço final com desconto e imposto."""
    valor_com_desconto = valor * (1 - desconto)
    valor_final = valor_com_desconto * (1 + imposto)
    return valor_final

# Chamadas com diferentes combinações de argumentos
print("\nCálculos de preço:")
print(f"Preço base: {calcular_preco(100)}")
print(f"Com desconto de 10%: {calcular_preco(100, 0.1)}")
print(f"Com desconto de 10% e imposto de 5%: {calcular_preco(100, 0.1, 0.05)}")
print(f"Com argumentos nomeados: {calcular_preco(valor=100, imposto=0.05, desconto=0.1)}")

# Escopo de variáveis
def demonstrar_escopo():
    """Demonstra o escopo de variáveis em funções."""
    variavel_local = "local"
    print(f"Dentro da função: {variavel_local}")
    return variavel_local

resultado = demonstrar_escopo()
print(f"Fora da função (retornada): {resultado}")
# print(f"Fora da função (inacessível): {variavel_local}")  # Isso causaria um erro

# ------------------------------------------------------------
# PARTE 5: PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
# ------------------------------------------------------------
print("\n=== PROGRAMAÇÃO ORIENTADA A OBJETOS ===")

# Definição de classe e construtor
class Pessoa:
    """Classe que representa uma pessoa."""
    
    def __init__(self, nome, idade):
        """Método construtor."""
        self.nome = nome  # Variável de instância
        self.idade = idade
    
    def apresentar(self):
        """Método que retorna uma apresentação da pessoa."""
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos."
    
    def aniversario(self):
        """Incrementa a idade da pessoa."""
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos."

# Criando objetos
pessoa1 = Pessoa("Carlos", 30)
pessoa2 = Pessoa("Lúcia", 25)

print(pessoa1.apresentar())
print(pessoa2.apresentar())
print(pessoa1.aniversario())

# Herança
class Estudante(Pessoa):
    """Classe que representa um estudante (herda de Pessoa)."""
    
    def __init__(self, nome, idade, curso):
        """Método construtor que estende o construtor da classe pai."""
        super().__init__(nome, idade)  # Chama o construtor da classe pai
        self.curso = curso
    
    def apresentar(self):
        """Sobrescreve o método da classe pai (polimorfismo)."""
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos e estudo {self.curso}."
    
    def estudar(self):
        """Método específico da classe Estudante."""
        return f"{self.nome} está estudando {self.curso}."

# Instância da classe derivada
estudante1 = Estudante("Pedro", 22, "Ciência da Computação")

print("\nDemonstrando herança e polimorfismo:")
print(estudante1.apresentar())  # Método sobrescrito
print(estudante1.estudar())     # Método específico
print(estudante1.aniversario()) # Método herdado

# Herança múltipla
class Trabalhador:
    """Classe que representa um trabalhador."""
    
    def __init__(self, profissao, salario):
        """Método construtor."""
        self.profissao = profissao
        self.salario = salario
    
    def trabalhar(self):
        """Método que indica que o trabalhador está trabalhando."""
        return f"Trabalhando como {self.profissao} por R$ {self.salario:.2f} por mês."

class EstudanteTrabalhador(Estudante, Trabalhador):
    """Classe que representa um estudante que também trabalha (herança múltipla)."""
    
    def __init__(self, nome, idade, curso, profissao, salario):
        """Método construtor que chama os construtores das classes pai."""
        Estudante.__init__(self, nome, idade, curso)
        Trabalhador.__init__(self, profissao, salario)
    
    def apresentar(self):
        """Sobrescreve o método apresentar para incluir informações de trabalho."""
        return (f"Olá, eu sou {self.nome}, tenho {self.idade} anos, "
                f"estudo {self.curso} e trabalho como {self.profissao}.")

# Instância da classe com herança múltipla
et = EstudanteTrabalhador("Ana", 28, "Engenharia", "Desenvolvedora", 4500)

print("\nDemonstrando herança múltipla:")
print(et.apresentar())
print(et.estudar())
print(et.trabalhar())
print(et.aniversario())

print("\n=== FIM DO SCRIPT ===")
