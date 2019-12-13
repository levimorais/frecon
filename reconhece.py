from leitura import lerArquivos
import face_recognition
import cv2
import os

#definindo constantes
registradosFilePath = "/home/levi/dev/ap2/face-recon/registrados/"
desconhecidoFilePath = "/home/levi/dev/ap2/face-recon/desconhecido/desconhecido.jpg"
listaDeNomes = lerArquivos.leitorDeNomes("{}".format(registradosFilePath))
listaDeArquivos = lerArquivos.leitorDeArquivos("{}".format(registradosFilePath))
lista = listaDeArquivos
global resultado
resultado = []
biodadosConhecidos = []

def atualizarBanco():
  global listaDeArquivos, lista, listaDeNomes

  listaDeArquivos = lerArquivos.leitorDeArquivos("{}".format(registradosFilePath))
  listaDeNomes = lerArquivos.leitorDeNomes("{}".format(registradosFilePath))
  lista = listaDeArquivos

def efetuarCadastro(nome, url):
  nome = nome.title()
  retorno = True
  camera = cv2.VideoCapture(url)
  print("Digite <ESC> para sair / <s> para Salvar")

  loop = True
  while loop:
    retval, imagem = camera.read()
    cv2.imshow('Efetuando Cadastro', imagem)
    tecla = cv2.waitKey(100)

#usuário aperta esc
    if tecla == 27:
      loop = False
    
#usuario aperta s
    elif tecla == ord('s'):
      cv2.imwrite("{}{}.jpg".format(registradosFilePath, nome), imagem)
      loop = False

#verifica se na foto cadastrada contém uma face
  try:
    imagemNovoCadastro = face_recognition.load_image_file("{}{}.jpg".format(registradosFilePath,nome))
    biodadoNovoCadastro = face_recognition.face_encodings(imagemNovoCadastro)[0]

  except IndexError:
    os.remove("{}{}.jpg".format(registradosFilePath,nome))
    retorno = False

  cv2.destroyAllWindows()
  camera.release()

  atualizarBanco()

  return retorno

def capturarDesconhecido(url):
  os.remove("{}".format(desconhecidoFilePath))

  retorno = True
  camera = cv2.VideoCapture(url)
  print("Digite <ESC> para sair / <s> para Salvar")

  loop = True
  while loop:
    retorno, imagem = camera.read()
    cv2.imshow('Foto', imagem)
    tecla = cv2.waitKey(100)

#usuário aperta esc
    if tecla == 27:
      loop = False
    
#usuario aperta s
    elif tecla == ord('s'):
      cv2.imwrite("{}".format(desconhecidoFilePath), imagem)
      loop = False

#verifica se a foto cadastrada contém uma face
  try:
    imagemDesconhecido = face_recognition.load_image_file("{}".format(desconhecidoFilePath))
    biodadoDesconhecido = face_recognition.face_encodings(imagemDesconhecido)[0]

  except IndexError:
    os.remove("{}".format(desconhecidoFilePath))
    retorno = False

  cv2.destroyAllWindows()
  camera.release()
  
  atualizarBanco()

  return retorno

#preenche a lista de biodados conhecidos
def coletarBiodadosConhecidos():
  if len(lista) < 1:
    return False

  elif len(lista) == 1:
    imagem = face_recognition.load_image_file("{}{}".format(registradosFilePath, lista[0]))
    biodadosConhecidos.append(face_recognition.face_encodings(imagem)[0])

    atualizarBanco()

    return biodadosConhecidos

  else:
      indice = lista.pop(0)
      imagem = face_recognition.load_image_file("{}{}".format(registradosFilePath, indice))
      biodadosConhecidos.append(face_recognition.face_encodings(imagem)[0])

  return coletarBiodadosConhecidos()

def coletarBiodadoDesconhecido():
    try:
        imagemDesconhecido = face_recognition.load_image_file("{}".format(desconhecidoFilePath))
        biodadoDesconhecido = face_recognition.face_encodings(imagemDesconhecido)[0]
    
    except IndexError:
        return False

    return biodadoDesconhecido

#dada uma lista de biodaos e um biodado a ser reconhecido, cada elemento da lista é comparado com o desconhecido e o resultado é armazenado
def compararFaces(biodadosConhecidos, biodadoDesconhecido):
    resultado = []
    for i in range(len(biodadosConhecidos)):
        resultado.append(face_recognition.compare_faces([biodadosConhecidos[i]], biodadoDesconhecido, tolerance = 0.6))
    
    return resultado

#verifica se algum rosto foi reconhecido e mostra o resultado
def verificarResultado(listaDeResultado):
  global indiceDoReconhecido, resultado
  indiceDoReconhecido = -1
  print(resultado, listaDeResultado, sep = "\n")

  cont = 0
  for i in listaDeResultado:
    for j in i:
        if j == True:
            indiceDoReconhecido = cont
            return listaDeNomes[indiceDoReconhecido]
                        
        cont += 1
  
  return False