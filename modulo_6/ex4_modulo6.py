# Faça um programa que leia e valide as seguintes informações:
# 1. Nome: maior que 3 caractéres;
# 2. Idade: entre 0 e 150;
# 3. Salário: maior que 0;
# 4. Sexo: 'f' ou 'm';
# 5. Estado Civil: 's', 'c', 'v', 'd';

class Pessoa:
    
    def __init__(self, nome: str, idade: int, sexo: str, estado: str) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.estado = estado
      
    def checa_nome(nome):
        if len(nome) <= 3:
            raise ValueError('O nome não tem mais que 3 caracteres')
        return print(f'O nome {nome} foi verificado')

    def checa_idade(idade):
        if idade:
            print('Idade válida')
        else:
            print('Idade inválida')
        return print(f'A idade {idade} foi verfificada')

    def checa_sexo(sexo):
        if sexo == 'f':
            print('Sexo Feminino')
        elif sexo == 'm':
            print('Sexo Masculino')
        else:
            print('Sexo inválido')
        return print(f'O sexo {sexo} foi verificado')
    
    def checa_estado(estado):
        if estado == 's':
            print('Solteiro')
        elif estado == 'c':
            print('Casaco')
        elif estado == 'v':
            print('Vipuvo')
        elif estado == 'd':
            print('Divorsiado')
        else:
            print('Estado civil inválido')
        return print(f'O estado {estado} foi verificado')

no = input('Digite o nome da pessoa, ')
ide = int(input('Digite a idade: '))
so = input('Digite o sexo: ')
es = input('Digite o estado civil: ')


Pessoa.checa_nome(no)
Pessoa.checa_idade(ide)
Pessoa.checa_sexo(so)
Pessoa.checa_estado(es)

