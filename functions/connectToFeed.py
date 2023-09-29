import cv2

def connectToFeed():
  feed = cv2.VideoCapture("rtsp://admin:Guilherme2*@192.168.1.190:554/cam/realmonitor?channel=1&subtype=0")
  feed.set(cv2.CAP_PROP_BUFFERSIZE, 1)
  # define tamanho da captura
  feed.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
  feed.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);
  return feed # retorna o feed da câmera