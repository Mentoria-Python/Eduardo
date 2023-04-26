'''
Crie um programa que cadastre informações de várias pessoas
(nome, idade e cpf) e depois coloque em um dicionário.
Depois remova todas as pessoas menores de 18 anos do
dicionário e coloque em outro dicionário.
'''


class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


class ListaDePessoas:
    def __init__(self):
        self.pessoas = []
        self.menor = []

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def apresentar_pessoas(self):
        for pessoa in self.pessoas:
            print('Nome: ', pessoa.nome)
            print('Idade: ', pessoa.idade)
            print('CPF: ', pessoa.cpf)
            print()

    def de_menor(self):
        for pessoa in self.pessoas:
            if pessoa.idade < 18:
                self.menor.append(pessoa)
                self.pessoas.remove(pessoa)
        return self.pessoas


lista_de_pessoas = ListaDePessoas()
numero_pessoas = int(input('Digite quantas pessoas deseja inserir: '))

for i in range(numero_pessoas):
    print(f'{i+1} pessoa:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cpf = input('cpf: ')
    pessoa = Pessoa(nome, idade, cpf)
    lista_de_pessoas.adicionar_pessoa(pessoa)


print('Os de menor')
lista_de_pessoas.de_menor()

print('As pessoas inseridas foram:')
lista_de_pessoas.apresentar_pessoas()
