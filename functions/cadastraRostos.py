import cv2 
import os # biblioteca para manipular arquivos e pastas

def cadastrarRostos():
  # abre a câmera para captura
  captura = cv2.VideoCapture(0);
  # tira uma foto
  resultado, foto = captura.read();
  # pede um nome para o usuário
  nome = input('Digite seu nome: ');
  # pede uma matrícula para o usuário
  matricula = input('Digite sua matrícula: ');
  
  #verifica se a pasta com o nome do usuário já existe
  if os.path.isdir('fotos/' + nome):
    print('Usuário já cadastrado');
    return
  else : # se não existir, cria a pasta
    os.mkdir('fotos/' + nome); 

  #mostra o path COMPLETO da pasta criada
  print('Pasta criada: ' + os.path.abspath('fotos/' + nome));

  # salva a foto na pasta criada usando a matrícula como nome do arquivo
  cv2.imwrite('fotos/' + nome + '/' + matricula + '.jpg', foto);
  # fecha a câmera
  captura.release();
  return

cadastrarRostos();