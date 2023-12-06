def menu():
    while True:
        nome = input('Digite o nome: ')
        if nome == str(0):
            print('Bye!')
            break        
        idade = int(input('Digite a idade: '))
        sexo = input('Digite o sexo (M ou F): ')
        telefone = int(input('Digite um telefone de contato: '))
        escrever_dados(nome, idade, sexo, telefone)
        ler_dados()


def escrever_dados(nome, idade, sexo, telefone):
    arquivo = open ('nomes_arquivos.txt','a', encoding= 'utf-8')
    arquivo.write(f'{nome} | {idade} | {sexo} |{telefone} \n')
    arquivo.close()

def ler_dados():
    arquivo = open ('nomes_arquivos.txt','r', encoding= 'utf-8')
    arquivo.read()
    print(arquivo.read())
    arquivo.close()


menu()
