from models.estudante import Estudante
import os


def menu():
    print('1. Adicionar um novo estudante.')
    print('2. Atualizar a nota de um estudante existente.')
    print('3. Visualizar informações de um estudante.')
    print('4. Listar todos os estudantes')
    print('5. Sair do programa.')
    return input('Informe sua opção: ')

def limpar_tela():
    """Limpa a tela, dependendo do sistema operacional."""
    if os.name == 'nt':  # Windows
        os.system('CLS')
    else: 
        os.system('clear')

def adicionar_estudante(estudantes_lista: list) -> None:
    limpar_tela()

    nome = input("Informe o nome do estudante: ")

    while True:
        try:
            idade = int(input('Informe a idade do estudante: '))
            break
        except ValueError:
            print('Idade inválidade, tente novamente.')

    while True:
        try:
            nota = float(input('Informe a nota do estudante: '))
            break
        except ValueError:
            print('Idade inválidade, tente novamente.')

    estudante = Estudante(nome, idade, nota)
    estudantes_lista.append(estudante)

def atualizar_nota(estudantes_lista: list) -> None:
    limpar_tela()
    aluno = input('Informe o nome do aluno que deseja alterar a nota: ')

    for estudante in estudantes_lista:
        if aluno == estudante.nome:
            while True:
                try:
                    nova_nota = float(input('Informe a nova nota do aluno: '))
                    estudante.nota = nova_nota
                    print('Nota alterada com sucesso.')
                    return
                except ValueError:
                    print('Nota inválida, tente novamente.')

    print('Aluno não está cadastrado.')

def visualizar_estudante(estudantes_lista: list) -> None:
    limpar_tela()
   
    aluno = input('Informe o nome do aluno que deseja visualizar: ')
    
    for estudante in estudantes_lista:
        
        if aluno == estudante.nome:
            print(f'Nome: {estudante.nome}, Idade: { estudante.idade}, Nota: {estudante.nota}')
            return
        
    print('Aluno não encontrado.')


def listar_estudantes(estudantes_lista: list) -> None:
    limpar_tela()
    if estudantes_lista:
        for estudante in estudantes_lista:
            print(f'Nome: {estudante.nome}, Idade: { estudante.idade}, Nota: {estudante.nota}')
    else:
        print('Nenhum estudante cadastrado.')
 

def main():

    estudantes_lista = []

    while True:
        limpar_tela()
        opc = menu()
        match opc:
            
            case '1':
                adicionar_estudante(estudantes_lista)
                os.system('PAUSE')

            case '2':
                atualizar_nota(estudantes_lista)
                os.system('PAUSE')

            case '3':
                visualizar_estudante(estudantes_lista)
                os.system('PAUSE')
                
            case '4':
                listar_estudantes(estudantes_lista)
                os.system('PAUSE')
                
            case '5':
                print('Obrigado por utilizar o programa...')
                break
            case _:
                print('Opção inválida...')


if __name__ == '__main__':
    main()