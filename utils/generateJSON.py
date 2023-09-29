# criar template de arquivo JSON para armazenar as configurações do sistema
import os  # biblioteca para manipular arquivos e pastas
import json


def pegarDados():
    path_fotos = input("Digite o nome da pasta para armazenamento das fotos: ")
    rtsp_address = input(
        "Digite o endereço RTSP da câmera seguindo o padrão: rtsp://admin:senha@ip:porta"
    )

    return path_fotos, rtsp_address


def generateJSON():
    path_fotos, rtsp_address = pegarDados()
    # criar dicionario com as configurações
    config = {"path_fotos": path_fotos, "endereco_rtsp": rtsp_address}

    # verificar se o JSON já existe
    if os.path.isfile("config.json"):
        print("Arquivo config.json já existe")
    else:
        # criar o arquivo
        with open("config.json", "w") as json_file:
            json.dump(config, json_file)
            print("Arquivo config.json criado")
    return


generateJSON()
