'''
Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
chave (CPF), nome, idade, telefone.
O programa deve ler um número indeterminado de chaves, criar a agenda
e imprimir todos os dados do dicionário no formato chave: nome-idadefone.
'''


class Pessoa:
    def __init__(self, nome: str, idade: int, telefone: str, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf


class ListaDePessoas:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def apresentar_pessoas(self):
        for pessoa in self.pessoas:
            print('Nome: ', pessoa.nome)
            print('Idade: ', pessoa.idade)
            print('Telefone: ', pessoa.telefone)
            print('cpf: ', pessoa.cpf)
            print()


lista_de_pessoas = ListaDePessoas()
numero_pessoas = int(input('Digite quantas pessoas deseja inserir: '))

for i in range(numero_pessoas):
    print(f'{i+1} pessoa:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    telefone = input('Telefone: ')
    cpf = input('cpf: ')
    pessoa = Pessoa(nome, idade, telefone, cpf)
    lista_de_pessoas.adicionar_pessoa(pessoa)

print('As pessoas inseridas foram:')
lista_de_pessoas.apresentar_pessoas()
