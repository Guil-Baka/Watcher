import cv2
import json


def connectToFeed():
    # ler rtsp address do arquivo config.json
    with open("config.json", "r") as json_file:
        config = json.load(json_file)
        rtsp_address = config["endereco_rtsp"]
    feed = cv2.VideoCapture(rtsp_address)  # conecta à câmera usando o endereço rtsp
    feed.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    # define tamanho da captura
    feed.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    feed.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return feed  # retorna o feed da câmera
