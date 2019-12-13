from leitura import lerArquivos
import reconhece
import face_recognition

url = "http://192.168.1.2:8080/video"
filePath = "/home/levi/dev/ap2/face-recon/registrados"
biodadosConhecidos = []

def cabecalho():
  print("-"*30)
  print("FACE RECON")
  print("-"*30)
  print("")
  print("MENU DE OPÇÕES:\n  \n  1.Cadastrar Face\n  2.Reconhecer Face\n  3.Sair")

if __name__ == "__main__":
  opcao = 1
  while opcao != 3:
    cabecalho()
    opcao = int(input("\nInsira a opção desejada: "))

    if opcao == 1:
      nome = str(input("\nEstamos efetuando seu cadastro...\nInsira seu nome por favor: "))

      while nome == "":
        nome = str(input("\nInsira seu nome por favor: "))

      retorno = reconhece.efetuarCadastro(nome, url)
      if retorno == False:
        print("Erro: Não há rosto na imagem")
      
      else:
        print("\nCadastro efetuado com sucesso\n")
    
    elif opcao == 2:
      retornoDesconhecido = reconhece.capturarDesconhecido(url)
      if retornoDesconhecido == False:
        print("Erro: Não há rosto na imagem")
      
      else:
        biodadosConhecidos = reconhece.coletarBiodadosConhecidos()
        if biodadosConhecidos == False:
          print("Erro: Não há cadastro no banco de dados")

        else:
          biodadoDesconhecido = reconhece.coletarBiodadoDesconhecido()
          listaDeResultados = reconhece.compararFaces(biodadosConhecidos, biodadoDesconhecido)
          resultadoFinal = reconhece.verificarResultado(listaDeResultados) 

          if resultadoFinal != False:
            print("Conseguimos reconhecer {}".format(resultadoFinal))
            
          else:
            print("Erro: Não reconhecemos ninguém do banco de dados")

    else:
      print("\nOpção inválida")