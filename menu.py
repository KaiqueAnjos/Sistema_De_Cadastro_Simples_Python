from lib import sistema
from lib import arquivos
from time import sleep

arq = 'cadPessoa.txt'

if not arquivos.arquivoExiste(arq):

    arquivos.criaArq(arq)

while True:
    opcao = sistema.menu(['Ver Pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if opcao == 1:
        # LISTAR DADOS DO ARQUIVO
        arquivos.lerArquivo(arq)
        sleep(2)

    elif opcao == 2:
        # CADASTRAR PESSOA
        sistema.cabecalho('CADASTRAR NOVA PESSOA:')
        nome = str(input('NOME: '))
        idade = sistema.leiaInt('IDADE: ')
        arquivos.cadPessoa(arq, nome, idade)
        sleep(2)

    elif opcao == 3:
        # SAINDO DO SISTEMA
        sistema.cabecalho('Saindo do Sistema... Até Logo!')
        break

    else:
        # OPCÃO INVÁLIDA
        print('ERRO! Digite uma opção válida!')
        sleep(2)

