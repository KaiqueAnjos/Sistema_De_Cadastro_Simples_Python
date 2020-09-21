from lib.sistema import cabecalho


def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArq(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')
    finally:
        arq.close()


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arq.close()


def cadPessoa(arq, nome='<desconhecido>', idade=0):
    try:
        arq = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao cadastrar pessoa')
        else:
            print(f'Novo Registro de {nome} Cadastrado.')
            arq.close()

