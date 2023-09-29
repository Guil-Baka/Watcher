import os  # biblioteca para manipular arquivos e pastas
import json


def createBaseFolder():
    # ler o path das fotos do arquivo config.json
    with open("config.json", "r") as json_file:
        config = json.load(json_file)
        path_fotos = config["path_fotos"]

    # check if folder exists
    if os.path.isdir(path_fotos):
        print("Pasta de armazenamento já existe")
    else:
        # create folder
        os.mkdir(path_fotos)
        print("Pasta de armazenamento criada")
    return


createBaseFolder()
