


class Estudante:

    def __init__(self, nome: str, idade: int, nota: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__nota = nota

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:

        if not isinstance(novo_nome, str) or len(novo_nome.strip()) == 0:
            raise ValueError('Por favor, digite um nome válido.')
        
        self.__nome = novo_nome

    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade) -> None:
        if not isinstance(nova_idade, int) or nova_idade < 0:
            raise ValueError('Por favor, digite uma idade válida')
        
        self.__idade = nova_idade

    @property
    def nota(self) -> float:
        return self.__nota
    
    @nota.setter
    def nota(self, nova_nota):
        if not isinstance(nova_nota, float) or not (0 <= nova_nota <= 10):
            raise ValueError('Por favor, digite uma nota válida (número entre 0 e 10).')
        
        self.__nota = nova_nota