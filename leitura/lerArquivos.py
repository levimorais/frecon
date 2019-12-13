import os

def leitorDeArquivos(path):
    listaDeArquivos = os.listdir("{}".format(path))
    listaDeArquivos.sort()

    return listaDeArquivos

def leitorDeNomes(path):
    listaAuxiliar = []
    listaDeNomes = []

    listaDeArquivos = os.listdir("{}".format(path))
    listaDeArquivos.sort()

    for arquivo in listaDeArquivos:
        arquivo = arquivo.replace(".jpg", "")
        listaAuxiliar.append(arquivo)
    
    for item in listaAuxiliar:
        item = item.title()
        listaDeNomes.append(item)

    return listaDeNomes
